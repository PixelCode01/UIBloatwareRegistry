#!/system/bin/sh

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
    print_colored $BLUE "OnePlus Bloatware Remover for Shizuku"
    print_colored $BLUE "Version 1.0"
    echo "=================================================="
    echo ""
    print_colored $YELLOW "WARNING: This script will remove applications from your device."
    print_colored $YELLOW "Always create a backup before proceeding."
    echo ""
}

check_environment() {
    if [ -z "$SHIZUKU_SERVER_VERSION" ] && [ "$(id -u)" != "2000" ]; then
        print_colored $RED "Warning: This script is designed for Shizuku environment."
        print_colored $YELLOW "Make sure you're running this through Shizuku terminal."
        echo ""
        read -p "Continue anyway? (y/n): " choice
        case "$choice" in
            y|Y) ;;
            *) exit 1 ;;
        esac
    fi
}

create_backup() {
    print_colored $BLUE "Creating backup of installed packages..."
    BACKUP_FILE="/sdcard/oneplus_backup_$(date +%Y%m%d_%H%M%S).txt"
    pm list packages > "$BACKUP_FILE"
    if [ $? -eq 0 ]; then
        print_colored $GREEN "Backup created: $BACKUP_FILE"
    else
        print_colored $RED "Failed to create backup!"
        exit 1
    fi
}

SAFE_PACKAGES="
com.oneplus.account:OnePlus Account service
com.oneplus.backuprestore:OnePlus Clone Phone
com.oneplus.brickmode:Brick mode service
com.oneplus.calculator:OnePlus Calculator
com.oneplus.camera:OnePlus Camera
com.oneplus.card:OnePlus Card service
com.oneplus.cloud:OnePlus Cloud storage
com.oneplus.compass:Compass application
com.oneplus.deskclock:Clock and alarm app
com.oneplus.filemanager:OnePlus File Manager
com.oneplus.gallery:OnePlus Gallery
com.oneplus.gamespace:Game Space
com.oneplus.iconpack.circle:Circle icon pack
com.oneplus.iconpack.square:Square icon pack
com.oneplus.market:OnePlus Store
com.oneplus.note:OnePlus Notes
com.oneplus.opsocialnetwork:OnePlus Community
com.oneplus.screenshot:Screenshot service
com.oneplus.skin:OnePlus themes
com.oneplus.soundrecorder:Sound recorder
com.oneplus.weather:OnePlus Weather
com.oneplus.widget:OnePlus widgets
com.oneplus.worklife:Work Life Balance
net.oneplus.commonlogtool:Common log tool
net.oneplus.odm:ODM service
net.oneplus.oemtcma:OEM TCMA service
net.oneplus.push:OnePlus push service
net.oneplus.weather:Weather service
com.google.android.apps.docs:Google Drive
com.google.android.apps.photos:Google Photos
com.google.android.apps.youtube.music:YouTube Music
com.google.android.music:Google Play Music
com.google.android.videos:Google Play Movies
com.google.android.youtube:YouTube
com.google.android.keep:Google Keep
com.google.android.apps.tachyon:Google Duo
com.google.ar.lens:Google Lens
com.google.android.feedback:Google Feedback
com.netflix.mediaclient:Netflix
com.netflix.partner.activation:Netflix activation
com.facebook.katana:Facebook
com.facebook.orca:Facebook Messenger
com.facebook.services:Facebook Services
com.facebook.system:Facebook System
com.instagram.android:Instagram
com.spotify.music:Spotify
com.qualcomm.qti.workloadclassifier:Workload classifier
com.qualcomm.qti.poweroffalarm:Power off alarm
com.qualcomm.qti.devicestatisticsservice:Device statistics
com.android.bips:Built-in Print Service
com.android.bookmarkprovider:Bookmark provider
com.android.printspooler:Print spooler
com.android.wallpaperbackup:Wallpaper backup
com.android.wallpapercropper:Wallpaper cropper
"

CAUTION_PACKAGES="
com.oneplus.contacts:OnePlus Contacts
com.oneplus.dialer:OnePlus Phone app
com.oneplus.launcher:OnePlus Launcher
com.oneplus.mms:OnePlus Messages
com.oneplus.music:OnePlus Music player
com.oneplus.setupwizard:Setup wizard
com.oneplus.systemui:System UI components
net.oneplus.launcher:OxygenOS Launcher
net.oneplus.opsystemhelper:System helper
com.google.android.apps.maps:Google Maps
com.google.android.gm:Gmail
com.google.android.googlequicksearchbox:Google Search
com.google.android.inputmethod.latin:Gboard
com.google.android.calendar:Google Calendar
com.qualcomm.qti.callenhancement:Call enhancement
com.qualcomm.qti.callfeaturessetting:Call features
com.qualcomm.qti.dynamicddsservice:Dynamic DDS service
com.qualcomm.qti.simsettings:SIM settings
com.android.chrome:Chrome browser
com.android.mms.service:MMS service
"

DANGEROUS_PACKAGES="
com.oneplus.framework:OnePlus framework
com.oneplus.opbugreportlite:Bug reporting service
com.oneplus.security:Security framework
net.oneplus.opdiagnose:System diagnostics
com.google.android.gms:Google Play Services
com.google.android.gsf:Google Services Framework
com.google.android.tts:Text-to-speech
com.qualcomm.qti.ims:IMS service for VoLTE
com.qualcomm.qti.telephonyservice:Telephony service
com.android.cellbroadcastreceiver:Emergency alerts
com.android.emergency:Emergency information
"

remove_packages() {
    local packages="$1"
    local category="$2"
    local count=0
    local failed=0

    print_colored $BLUE "Removing $category packages..."

    echo "$packages" | while IFS=':' read -r package desc; do
        if [ -n "$package" ] && [ "$package" != "" ]; then
            echo "Removing: $desc ($package)"

            pm uninstall --user 0 "$package" 2>/dev/null
            if [ $? -eq 0 ]; then
                print_colored $GREEN "Uninstalled: $package"
                count=$((count + 1))
            else
                pm disable-user --user 0 "$package" 2>/dev/null
                if [ $? -eq 0 ]; then
                    print_colored $YELLOW "Disabled: $package"
                    count=$((count + 1))
                else
                    print_colored $RED "Failed: $package"
                    failed=$((failed + 1))
                fi
            fi
        fi
    done

    echo ""
    print_colored $GREEN "Processed packages in $category category"
    echo ""
}

interactive_removal() {
    print_colored $BLUE "=== INTERACTIVE PACKAGE REMOVAL ==="
    echo ""

    print_colored $GREEN "SAFE packages (recommended to remove):"
    echo "$SAFE_PACKAGES" | grep -v '^$' | while IFS=':' read -r package desc; do
        if [ -n "$package" ]; then
            echo "  - $desc"
        fi
    done
    echo ""

    read -p "Remove SAFE packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        remove_packages "$SAFE_PACKAGES" "SAFE"
    fi

    print_colored $YELLOW "CAUTION packages (may affect functionality):"
    echo "$CAUTION_PACKAGES" | grep -v '^$' | while IFS=':' read -r package desc; do
        if [ -n "$package" ]; then
            echo "  - $desc"
        fi
    done
    echo ""

    read -p "Remove CAUTION packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        remove_packages "$CAUTION_PACKAGES" "CAUTION"
    fi

    print_colored $RED "DANGEROUS packages (NOT recommended):"
    echo "$DANGEROUS_PACKAGES" | grep -v '^$' | while IFS=':' read -r package desc; do
        if [ -n "$package" ]; then
            echo "  - $desc"
        fi
    done
    echo ""

    read -p "Remove DANGEROUS packages? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        print_colored $RED "WARNING: Removing these packages may break device functionality!"
        read -p "Are you absolutely sure? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            remove_packages "$DANGEROUS_PACKAGES" "DANGEROUS"
        fi
    fi
}

batch_removal() {
    print_colored $BLUE "=== BATCH REMOVAL (SAFE PACKAGES ONLY) ==="
    echo ""
    print_colored $YELLOW "This will remove all SAFE OnePlus bloatware packages."
    print_colored $YELLOW "These are apps that can be safely removed without affecting core functionality."
    echo ""

    read -p "Continue with batch removal? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        remove_packages "$SAFE_PACKAGES" "SAFE"
        print_colored $GREEN "Batch removal completed!"
    else
        print_colored $YELLOW "Batch removal cancelled."
    fi
}

list_all_packages() {
    print_colored $BLUE "=== ALL INSTALLED PACKAGES ==="
    echo ""
    print_colored $YELLOW "Listing all installed packages (this may take a moment)..."
    pm list packages -f | sort
    echo ""
    print_colored $GREEN "Package listing completed."
}

show_menu() {
    echo ""
    print_colored $BLUE "=== ONEPLUS BLOATWARE REMOVER MENU ==="
    echo "1. Interactive removal (recommended)"
    echo "2. Batch removal (remove all safe packages)"
    echo "3. List all installed packages"
    echo "4. Create backup only"
    echo "5. Exit"
    echo ""
    read -p "Choose an option (1-5): " choice

    case $choice in
        1)
            create_backup
            interactive_removal
            ;;
        2)
            create_backup
            batch_removal
            ;;
        3)
            list_all_packages
            ;;
        4)
            create_backup
            print_colored $GREEN "Backup created successfully!"
            ;;
        5)
            print_colored $GREEN "Exiting OnePlus Bloatware Remover."
            exit 0
            ;;
        *)
            print_colored $RED "Invalid option. Please choose 1-5."
            show_menu
            ;;
    esac
}

main() {
    print_header
    check_environment

    if ! command -v pm >/dev/null 2>&1; then
        print_colored $RED "Error: 'pm' command not found!"
        print_colored $YELLOW "Make sure you're running this in a Shizuku terminal with proper permissions."
        exit 1
    fi

    show_menu
}

main
