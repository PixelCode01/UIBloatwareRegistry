#!/system/bin/sh
# Auto-generated from packages_registry.json

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_colored() {
    local color=$1
    local text=$2
    printf "${color}${text}${NC}\n"
}

print_header() {
    echo "=================================================="
    print_colored $BLUE "Samsung Bloatware Remover for Shizuku"
    print_colored $BLUE "Version 1.0"
    echo "=================================================="
    echo ""
    print_colored $YELLOW "WARNING: This script will remove applications from your device."
    print_colored $YELLOW "Always create a backup before proceeding."
    echo ""
}

SAFE_PACKAGES="
com.samsung.android.bixby.wakeup:Bixby wake up service
com.samsung.android.app.spage:Bixby homepage launcher
com.samsung.android.app.routines:Bixby Routines
com.samsung.android.bixby.service:Bixby features
com.samsung.android.visionintelligence:Bixby Vision
com.samsung.android.bixby.agent:Bixby Voice
com.samsung.android.email.provider:Samsung Email
com.sec.android.app.voicenote:Voice Recorder
com.samsung.android.scloud:Samsung Cloud
com.samsung.android.oneconnect:SmartThings
com.samsung.android.voc:Samsung Members
com.samsung.ecomm.global:Samsung Shop
com.vzw.hss.myverizon:My Verizon
com.att.myWireless:myAT&T
com.google.android.apps.docs:Google Docs
com.google.android.apps.photos:Google Photos
com.google.android.music:Google Play Music
com.test.app:Test Application
"

CAUTION_PACKAGES="
com.samsung.android.messaging:Samsung Messages
com.sec.android.app.sbrowser:Samsung Internet
com.samsung.android.calendar:Samsung Calendar
com.sec.android.app.popupcalculator:Samsung Calculator
com.samsung.android.samsungpass:Samsung Pass
com.samsung.vvm:Visual Voicemail
com.google.android.apps.maps:Google Maps
com.google.android.gm:Gmail
com.google.android.youtube:YouTube
"

DANGEROUS_PACKAGES="
com.samsung.android.spay:Samsung Pay
"

remove_packages() {
    local packages="$1"
    local category="$2"
    print_colored $BLUE "Removing $category packages..."
    echo "$packages" | while IFS=':'  read -r package desc; do
        if [ -n "$package" ] && [ "$package" != "" ]; then
            echo "Removing: $desc ($package)"
            pm uninstall --user 0 "$package" 2>/dev/null
            if [ $? -eq 0 ]; then
                print_colored $GREEN "Uninstalled: $package"
            else
                pm disable-user --user 0 "$package" 2>/dev/null
                if [ $? -eq 0 ]; then
                    print_colored $YELLOW "Disabled: $package"
                else
                    print_colored $RED "Failed: $package"
                fi
            fi
        fi
    done
    echo ""
}

interactive_removal() {
    print_colored $BLUE "=== INTERACTIVE PACKAGE REMOVAL ==="
    echo ""
    read -p "Remove SAFE packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        remove_packages "$SAFE_PACKAGES" "SAFE"
    fi
    read -p "Remove CAUTION packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        remove_packages "$CAUTION_PACKAGES" "CAUTION"
    fi
    read -p "Remove DANGEROUS packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        print_colored $RED "WARNING: This may break device functionality!"
        read -p "Are you sure? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            remove_packages "$DANGEROUS_PACKAGES" "DANGEROUS"
        fi
    fi
}

main() {
    print_header
    interactive_removal
}

main