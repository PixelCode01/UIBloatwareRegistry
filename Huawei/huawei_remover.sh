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
    print_colored $BLUE "Huawei Bloatware Remover for Shizuku"
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
    BACKUP_FILE="/sdcard/huawei_backup_$(date +%Y%m%d_%H%M%S).txt"
    pm list packages > "$BACKUP_FILE"
    if [ $? -eq 0 ]; then
        print_colored $GREEN "Backup created: $BACKUP_FILE"
    else
        print_colored $RED "Failed to create backup!"
        exit 1
    fi
}

SAFE_PACKAGES="
com.huawei.appmarket:Huawei AppGallery
com.huawei.browser:Huawei Browser
com.huawei.calculator:Huawei Calculator
com.huawei.camera:Huawei Camera
com.huawei.compass:Compass app
com.huawei.desktop.explorer:File Manager
com.huawei.gameassistant:Game Assistant
com.huawei.gamebox:Game Center
com.huawei.health:Huawei Health
com.huawei.himovie:Huawei Video
com.huawei.hmusic:Huawei Music
com.huawei.magazine:Magazine Unlock
com.huawei.mirror:Mirror app
com.huawei.notepad:Notepad
com.huawei.parentcontrol:Parental Control
com.huawei.scanner:AI Scanner
com.huawei.screenrecorder:Screen Recorder
com.huawei.search:Huawei Search
com.huawei.tips:Tips app
com.huawei.translator:Translator
com.huawei.vassistant:Voice Assistant
com.huawei.wallet:Huawei Wallet
com.huawei.weather:Weather app
com.huawei.works:Docs app
com.huawei.android.chr:User Experience Program
com.huawei.android.karaoke:Karaoke feature
com.huawei.android.thememanager:Theme Manager
com.huawei.bd:Big Data service
com.huawei.hiaction:HiAction automation
com.huawei.hicard:HiCard service
com.huawei.hifolder:HiFolder
com.huawei.hitouch:HiTouch
com.huawei.livewallpaper.paradise:Live wallpapers
com.huawei.motionservice:Motion service
com.huawei.nearby:Huawei Share
com.huawei.stylus:Stylus support
com.google.android.apps.docs:Google Drive
com.google.android.apps.photos:Google Photos
com.google.android.music:Google Play Music
com.google.android.videos:Google Play Movies
com.google.android.youtube:YouTube
com.facebook.katana:Facebook
com.facebook.orca:Facebook Messenger
com.instagram.android:Instagram
com.netflix.mediaclient:Netflix
com.spotify.music:Spotify
com.twitter.android:Twitter
com.whatsapp:WhatsApp
"

CAUTION_PACKAGES="
com.huawei.android.launcher:Huawei Launcher
com.huawei.contacts:Contacts app
com.huawei.deskclock:Clock app
com.huawei.gallery:Gallery app
com.huawei.mms:Messages app
com.huawei.phoneservice:Phone app
com.huawei.android.internal.app:Internal apps
com.huawei.fastapp:Quick App Center
com.huawei.intelligent:HiAssistant
com.huawei.powergenie:Power Genie
com.google.android.gm:Gmail
com.google.android.googlequicksearchbox:Google Search
"

DANGEROUS_PACKAGES="
com.huawei.android.hwaps:Huawei Mobile Services
com.huawei.hwid.core:Huawei ID Core
com.huawei.systemserver:System Server
com.huawei.android.pushagent:Push service
com.huawei.hwid:Huawei ID
com.huawei.systemmanager:System Manager
com.google.android.gms:Google Play Services
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
    print_colored $YELLOW "This will remove all SAFE Huawei bloatware packages."
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
    print_colored $BLUE "=== HUAWEI BLOATWARE REMOVER MENU ==="
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
            print_colored $GREEN "Exiting Huawei Bloatware Remover."
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
