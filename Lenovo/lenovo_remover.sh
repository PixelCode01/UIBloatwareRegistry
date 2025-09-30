#!/system/bin/sh

PACKAGES_BASE="
com.lenovo.anyshare.gps
com.lenovo.safecenter
com.lenovo.smartassistant
com.lenovo.lps
com.lenovo.email
com.lenovo.calendar
com.lenovo.fmradio
"

CRITICAL="
com.lenovo.ota
com.lenovo.lsf
"

echo "=============================="
echo "Lenovo Bloatware Remover"
echo "=============================="

echo "Backup saved to /sdcard/lenovo_packages_backup.txt"
pm list packages > /sdcard/lenovo_packages_backup.txt

echo "Removing optional Lenovo apps"
for pkg in $PACKAGES_BASE; do
    pm uninstall --user 0 "$pkg" >/dev/null 2>&1 || pm disable-user --user 0 "$pkg"
done

echo "Critical services require confirmation"
for pkg in $CRITICAL; do
    read -p "Disable $pkg ? (y/n): " resp
    if [ "$resp" = "y" ]; then
        pm disable-user --user 0 "$pkg"
    fi
done

echo "Done"
