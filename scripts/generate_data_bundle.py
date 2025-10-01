from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from importlib import import_module
from pathlib import Path
from typing import Any, Iterable
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BRANDS = [
    ("Samsung", "Samsung.samsung_remover", "SamsungRemover"),
    ("Xiaomi", "Xiaomi.xiaomi_remover", "XiaomiRemover"),
    ("Oppo", "Oppo.oppo_remover", "OppoRemover"),
    ("Vivo", "Vivo.vivo_remover", "VivoRemover"),
    ("Realme", "Realme.realme_remover", "RealmeRemover"),
    ("Tecno", "Tecno.tecno_remover", "TecnoRemover"),
    ("OnePlus", "OnePlus.oneplus_remover", "OnePlusRemover"),
    ("Huawei", "Huawei.huawei_remover", "HuaweiRemover"),
    ("Honor", "Honor.honor_remover", "HonorRemover"),
    ("Motorola", "Motorola.motorola_remover", "MotorolaRemover"),
    ("Nothing", "Nothing.nothing_remover", "NothingRemover"),
    ("Asus", "Asus.asus_remover", "AsusRemover"),
    ("Google", "Google.google_remover", "GoogleRemover"),
    ("Infinix", "Infinix.infinix_remover", "InfinixRemover"),
    ("Lenovo", "Lenovo.lenovo_remover", "LenovoRemover"),
]

CATEGORY_OVERRIDES: dict[tuple[str, str] | str, str] = {
    ("samsung", "carrier_bloat"): "adware",
    ("samsung", "google_apps"): "telemetry",
    "ads": "adware",
    "preloads": "oem_tool",
    "gaming": "oem_tool",
    "services": "telemetry",
    "assistant": "telemetry",
    "pixel_features": "oem_tool",
    "system_tools": "oem_tool",
    "media": "adware",
}

RISK_SCORES = {"safe": 1, "caution": 2, "dangerous": 3, "unknown": 0}


def load_packages() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for brand_title, module_path, class_name in BRANDS:
        module = import_module(module_path)
        cls = getattr(module, class_name)
        remover = cls(test_mode=True)
        config = remover._get_default_packages()
        categories: dict[str, Iterable[dict[str, Any]]] = config.get("categories", {})
        for category_key, packages in categories.items():
            for item in packages:
                package_name = item.get("name")
                if not package_name:
                    continue
                risk = item.get("risk", "unknown").lower()
                risk_score = RISK_SCORES.get(risk, 0)
                description = item.get("description", "")
                normalized_category = category_key.replace("_", " ").title()
                group = CATEGORY_OVERRIDES.get((brand_title.lower(), category_key.lower()))
                if not group:
                    group = CATEGORY_OVERRIDES.get(category_key.lower(), "oem_tool")
                entries.append(
                    {
                        "brand": brand_title,
                        "platform": brand_title,
                        "package": package_name,
                        "description": description,
                        "risk": risk,
                        "risk_score": risk_score,
                        "category": normalized_category,
                        "category_slug": category_key,
                        "category_group": group,
                    }
                )
    entries.sort(key=lambda row: (row["brand"], row["category"], row["package"]))
    return entries


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate consolidated bloatware dataset")
    parser.add_argument("--out", default="build/data.json")
    parser.add_argument("--public", default="web/public/data.json")
    args = parser.parse_args()

    packages = load_packages()
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "package_count": len(packages),
        "brands": sorted({entry["brand"] for entry in packages}),
        "category_groups": sorted({entry["category_group"] for entry in packages}),
        "risks": RISK_SCORES,
        "packages": packages,
    }

    primary_path = Path(args.out)
    public_path = Path(args.public)
    write_json(payload, primary_path)
    write_json(payload, public_path)


if __name__ == "__main__":
    main()
