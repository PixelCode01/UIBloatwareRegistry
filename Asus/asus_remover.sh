#!/system/bin/sh

PACKAGES_SAFE="
com.asus.launcher
com.asus.mobilemanager
com.asus.filemanager
com.asus.weather
com.asus.gamecenter
com.asus.rogtheme
com.facebook.katana
com.instagram.android
"

PACKAGES_CAUTION="
com.asus.gamingfan
com.netflix.partner.activation
"

echo "=============================="
echo "Asus Bloatware Remover"
echo "=============================="

echo "Creating package backup to /sdcard/asus_packages_backup.txt"
pm list packages > /sdcard/asus_packages_backup.txt

echo "Removing safe packages"
for pkg in $PACKAGES_SAFE; do
    pm uninstall --user 0 "$pkg" >/dev/null 2>&1 || pm disable-user --user 0 "$pkg"
done

echo "Processing caution packages"
for pkg in $PACKAGES_CAUTION; do
    read -p "Handle $pkg ? (y/n): " resp
    if [ "$resp" = "y" ]; then
        pm uninstall --user 0 "$pkg" >/dev/null 2>&1 || pm disable-user --user 0 "$pkg"
    fi
done

echo "Done"
