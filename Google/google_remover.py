import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover


class GoogleRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('Google', 'Google/google_config.json', test_mode, use_registry=use_registry)

    def _get_default_packages(self):
        return {
            "categories": {
                "pixel_features": [
                    {"name": "com.google.android.apps.turbo", "description": "Google Pixel Adaptive Battery", "risk": "dangerous"},
                    {"name": "com.google.android.apps.wellbeing", "description": "Digital Wellbeing suite", "risk": "caution"},
                    {"name": "com.google.android.apps.pixelmigrate", "description": "Pixel data transfer tool", "risk": "caution"},
                ],
                "media": [
                    {"name": "com.google.android.apps.videos", "description": "Google TV", "risk": "safe"},
                    {"name": "com.google.android.apps.podcasts", "description": "Google Podcasts", "risk": "safe"},
                    {"name": "com.google.android.apps.youtube.music", "description": "YouTube Music", "risk": "caution"},
                ],
                "assistant": [
                    {"name": "com.google.android.apps.tachyon", "description": "Google Meet", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"},
                    {"name": "com.google.android.apps.dialer", "description": "Google Phone dialer", "risk": "dangerous"},
                ],
            }
        }


def main():
    remover = GoogleRemover()

    print("Google Pixel Bloatware Removal Tool")
    print("1. Interactive removal (recommended)")
    print("2. List all apps and select what to remove")
    print("3. Manually remove by package or app name")
    print("4. Remove all configured packages")
    print("5. Exit")

    choice = input("Select option (1-5): ").strip()

    if choice == '1':
        remover.interactive_removal()
    elif choice == '2':
        print("This will list all installed applications on your device.")
        if input("Continue? (y/n): ").lower() == 'y':
            remover.list_all_apps_removal()
    elif choice == '3':
        remover.manual_package_removal()
    elif choice == '4':
        if input("This will remove ALL configured packages. Continue? (y/n): ").lower() == 'y':
            remover.remove_packages()
    elif choice == '5':
        print("Exiting...")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
