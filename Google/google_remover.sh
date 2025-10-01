#!/system/bin/sh

PACKAGES="
com.google.android.apps.turbo
com.google.android.apps.wellbeing
com.google.android.apps.pixelmigrate
com.google.android.apps.videos
com.google.android.apps.podcasts
com.google.android.apps.youtube.music
com.google.android.apps.tachyon
com.google.ar.lens
"

CRITICAL="
com.google.android.apps.dialer
"

echo "=============================="
echo "Google Pixel Bloatware Remover"
echo "=============================="

echo "Backing up package list to /sdcard/google_packages_backup.txt"
pm list packages > /sdcard/google_packages_backup.txt

echo "Removing optional Google apps"
for pkg in $PACKAGES; do
    pm uninstall --user 0 "$pkg" >/dev/null 2>&1 || pm disable-user --user 0 "$pkg"
done

echo "Critical apps require confirmation"
for pkg in $CRITICAL; do
    read -p "Disable $pkg ? (y/n): " resp
    if [ "$resp" = "y" ]; then
        pm disable-user --user 0 "$pkg"
    fi
done

echo "Done"
