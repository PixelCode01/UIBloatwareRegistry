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
    print_colored $BLUE "Vivo Bloatware Remover for Shizuku"
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
    BACKUP_FILE="/sdcard/vivo_backup_$(date +%Y%m%d_%H%M%S).txt"
    pm list packages > "$BACKUP_FILE"
    if [ $? -eq 0 ]; then
        print_colored $GREEN "Backup created: $BACKUP_FILE"
    else
        print_colored $RED "Failed to create backup!"
        exit 1
    fi
}

SAFE_PACKAGES="
com.android.bbkcalculator:Calculator app
com.android.bbklog:Log collection service
com.android.bbkmusic:i Music player
com.android.bbksoundrecorder:Sound recorder
com.bbk.photoframewidget:Photo widget
com.bbk.scene.indoor:My House app
com.bbk.theme:i Theme customization
com.bbk.theme.resources:Theme Store
com.baidu.duersdk.opensdk:ViVoice assistant
com.baidu.input_vivo:Chinese keyboard
com.ibimuyu.lockscreen:Glance Lockfeed
com.vivo.collage:Photo collage maker
com.vivo.compass:Compass app
com.vivo.doubleinstance:App Clone feature
com.vivo.doubletimezoneclock:Timezone widget
com.vivo.dream.clock:Screensaver clock
com.vivo.dream.music:Screensaver music
com.vivo.dream.weather:Screensaver weather
com.vivo.easyshare:Easy Share
com.vivo.ewarranty:E-warranty service
com.vivo.favorite:Favorites app
com.vivo.floatingball:Floating ball assistant
com.vivo.FMRadio:FM Radio app
com.vivo.fuelsummary:Fuel summary
com.vivo.gamewatch:Game monitoring
com.vivo.globalsearch:Global search
com.vivo.hiboard:Hi Board service
com.vivo.vivokaraoke:Mobile KTV
com.vivo.livewallpaper.coffeetime:Coffee time live wallpaper
com.vivo.livewallpaper.coralsea:Coral sea live wallpaper
com.vivo.livewallpaper.floatingcloud:Floating cloud wallpaper
com.vivo.livewallpaper.silk:Silk live wallpaper
com.vivo.magazine:Lockscreen Magazine
com.vivo.mediatune:Media tune service
com.vivo.minscreen:Mini screen feature
com.vivo.motormode:Motor Mode
com.vivo.carmode:Driving Mode
com.vivo.numbermark:Number marking service
com.vivo.scanner:QR/Barcode scanner
com.vivo.smartshot:Smart screenshot
com.vivo.translator:Translation app
com.vivo.video.floating:Video floating widget
com.vivo.videoeditor:Video editor
com.vivo.website:Vivo website shortcut
com.vivo.widget.calendar:Calendar widget
com.vlife.vivo.wallpaper:Vivo live wallpaper
com.kikaoem.vivo.qisiemoji.inputmethod:Emoji keyboard
com.facebook.appmanager:Facebook App Manager
com.facebook.services:Facebook Services
com.facebook.system:Facebook System Service
com.google.android.apps.docs:Google Drive
com.google.android.apps.photos:Google Photos
com.google.android.apps.tachyon:Google Duo
"

CAUTION_PACKAGES="
com.android.BBKClock:Clock app
com.bbk.account:Vivo account service
com.bbk.calendar:Vivo Calendar
com.bbk.cloud:Vivo Cloud storage
com.bbk.SuperPowerSave:Power saver mode
com.iqoo.engineermode:Engineering Mode
com.iqoo.secure:i Manager security
com.vivo.appstore:Vivo App Store
com.vivo.assistant:Jovi Smart Scene
com.vivo.browser:Vivo Web Browser
com.vivo.email:Email app
com.vivo.gallery:Gallery app
com.vivo.safecenter:Security center
com.vivo.setupwizard:Setup wizard
com.vivo.sim.contacts:SIM contacts
com.vivo.smartmultiwindow:Multi-window feature
com.vivo.unionpay:Vivo Pay
com.vivo.weather:Weather app
com.vivo.weather.provider:Weather service
"

DANGEROUS_PACKAGES="
com.bbk.iqoo.logsystem:System logging
com.vivo.appfilter:App filtering service
com.vivo.pushservice:Push notification service
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
    print_colored $YELLOW "This will remove all SAFE Vivo bloatware packages."
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
    print_colored $BLUE "=== VIVO BLOATWARE REMOVER MENU ==="
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
            print_colored $GREEN "Exiting Vivo Bloatware Remover."
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
