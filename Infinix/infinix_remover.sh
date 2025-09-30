#!/system/bin/sh

PACKAGES="
com.transsion.xclub
com.transsion.smartpanel
com.transsion.aura.gameassist
com.transsion.aia
com.infinix.xshare
com.infinix.xclub
com.transsion.phoenix
com.transsion.aha.games
com.transsion.xboom
com.transsion.calculator
"

echo "=============================="
echo "Infinix Bloatware Remover"
echo "=============================="

echo "Backing up package list to /sdcard/infinix_packages_backup.txt"
pm list packages > /sdcard/infinix_packages_backup.txt

echo "Removing selected packages"
for pkg in $PACKAGES; do
    pm uninstall --user 0 "$pkg" >/dev/null 2>&1 || pm disable-user --user 0 "$pkg"
done

echo "Complete"
