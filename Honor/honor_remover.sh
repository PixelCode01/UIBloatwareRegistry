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
    print_colored $BLUE "Honor Bloatware Remover for Shizuku"
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
    BACKUP_FILE="/sdcard/honor_backup_$(date +%Y%m%d_%H%M%S).txt"
    pm list packages > "$BACKUP_FILE"
    if [ $? -eq 0 ]; then
        print_colored $GREEN "Backup created: $BACKUP_FILE"
    else
        print_colored $RED "Failed to create backup"
        return 1
    fi
}

declare_safe_packages() {
    SAFE_PACKAGES="
com.hihonor.appmarket:Honor_AppGallery
com.hihonor.browser:Honor_Browser
com.hihonor.calculator:Honor_Calculator
com.hihonor.compass:Compass_app
com.hihonor.filemanager:File_Manager
com.hihonor.gameassistant:Game_Assistant
com.hihonor.gamecenter:Game_Center
com.hihonor.health:Honor_Health
com.hihonor.himovie:Honor_Video
com.hihonor.music:Honor_Music
com.hihonor.notepad:Notepad
com.hihonor.parentcontrol:Parental_Control
com.hihonor.scanner:AI_Scanner
com.hihonor.screenrecorder:Screen_Recorder
com.hihonor.search:Honor_Search
com.hihonor.tips:Tips_app
com.hihonor.translator:Translator
com.hihonor.vassistant:Voice_Assistant
com.hihonor.wallet:Honor_Wallet
com.hihonor.weather:Weather_app
com.hihonor.yoyo:YOYO_Assistant
com.hihonor.android.chr:User_Experience_Program
com.hihonor.android.karaoke:Karaoke_feature
com.hihonor.android.thememanager:Theme_Manager
com.hihonor.bd:Big_Data_service
com.hihonor.hiaction:HiAction_automation
com.hihonor.hicard:HiCard_service
com.hihonor.hifolder:HiFolder
com.hihonor.hitouch:HiTouch
com.hihonor.livewallpaper:Live_wallpapers
com.hihonor.motionservice:Motion_service
com.hihonor.nearby:Honor_Share
com.hihonor.stylus:Stylus_support
com.hihonor.magicui.smartcare:Smart_Care
com.hihonor.magicui.optimization:System_Optimization
"
}

declare_caution_packages() {
    CAUTION_PACKAGES="
com.hihonor.android.launcher:Honor_Launcher
com.hihonor.contacts:Contacts_app
com.hihonor.deskclock:Clock_app
com.hihonor.gallery:Gallery_app
com.hihonor.mms:Messages_app
com.hihonor.phone:Phone_app
com.hihonor.fastapp:Quick_App_Center
com.hihonor.intelligent:HiAssistant
com.hihonor.powergenie:Power_Genie
com.hihonor.magicui.assistant:Magic_UI_Assistant
"
}

declare_dangerous_packages() {
    DANGEROUS_PACKAGES="
com.hihonor.android.hms:Honor_Mobile_Services
com.hihonor.hwid:Honor_ID
com.hihonor.systemserver:System_Server
com.hihonor.android.pushagent:Push_service
com.hihonor.hwid.core:Honor_ID_Core
com.hihonor.systemmanager:System_Manager
"
}

declare_third_party_packages() {
    THIRD_PARTY_PACKAGES="
com.facebook.katana:Facebook
com.facebook.orca:Facebook_Messenger
com.instagram.android:Instagram
com.netflix.mediaclient:Netflix
com.spotify.music:Spotify
com.twitter.android:Twitter
com.whatsapp:WhatsApp
com.booking:Booking.com
com.tripadvisor.tripadvisor:TripAdvisor
"
}

is_package_installed() {
    local package=$1
    pm list packages | grep -q "package:$package"
}

remove_package() {
    local package=$1
    local description=$2

    print_colored $BLUE "Removing: $description ($package)"

    pm uninstall --user 0 "$package" 2>/dev/null
    if [ $? -eq 0 ]; then
        print_colored $GREEN "Successfully removed: $description"
        return 0
    fi

    pm disable-user --user 0 "$package" 2>/dev/null
    if [ $? -eq 0 ]; then
        print_colored $YELLOW "Disabled: $description (could not uninstall)"
        return 0
    fi

    print_colored $RED "Failed to remove: $description"
    return 1
}

show_package_category() {
    local category_name=$1
    local packages=$2
    local risk_color=$3
    local risk_level=$4

    echo ""
    print_colored $BLUE "=== $category_name ==="
    echo ""

    local count=0
    local installed_packages=""

    echo "$packages" | while IFS=: read -r package description; do
        if [ -n "$package" ] && [ -n "$description" ]; then
            if is_package_installed "$package"; then
                count=$((count + 1))
                printf "%2d. [%s%s%s] %s\n" "$count" "$risk_color" "$risk_level" "$NC" "$description"
                printf "    Package: %s\n" "$package"
                echo ""
                installed_packages="$installed_packages$count:$package:$description "
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        print_colored $YELLOW "No packages from this category are currently installed."
    fi

    return $count
}

interactive_removal() {
    print_colored $BLUE "Interactive Removal Mode"
    print_colored $YELLOW "Only showing packages that are currently installed on your device"
    echo ""

    declare_safe_packages
    declare_caution_packages
    declare_dangerous_packages
    declare_third_party_packages

    show_package_category "SAFE PACKAGES (Can be removed safely)" "$SAFE_PACKAGES" "$GREEN" "SAFE"
    safe_count=$?

    show_package_category "CAUTION PACKAGES (May affect some features)" "$CAUTION_PACKAGES" "$YELLOW" "CAUTION"
    caution_count=$?

    show_package_category "DANGEROUS PACKAGES (Critical system components)" "$DANGEROUS_PACKAGES" "$RED" "DANGEROUS"
    dangerous_count=$?

    show_package_category "THIRD-PARTY PACKAGES (Pre-installed bloatware)" "$THIRD_PARTY_PACKAGES" "$GREEN" "SAFE"
    third_party_count=$?

    total_count=$((safe_count + caution_count + dangerous_count + third_party_count))

    if [ $total_count -eq 0 ]; then
        print_colored $YELLOW "No bloatware packages found on your device."
        return
    fi

    echo ""
    print_colored $BLUE "Found $total_count removable packages"
    echo ""
    print_colored $YELLOW "You can enter:"
    echo "- Individual numbers: 1,3,5"
    echo "- Ranges: 1-5"
    echo "- Mixed: 1,3-5,7"
    echo "- 'all' to select all SAFE packages only"
    echo "- 'quit' to exit"
    echo ""

    read -p "Enter your selection: " selection

    if [ "$selection" = "quit" ]; then
        exit 0
    fi

    if [ "$selection" = "all" ]; then
        print_colored $YELLOW "Removing all SAFE packages..."
        remove_safe_packages
    else
        print_colored $YELLOW "Manual selection processing not fully implemented in this version."
        print_colored $YELLOW "Use 'all' for safe packages or try batch mode."
    fi
}

remove_safe_packages() {
    declare_safe_packages
    declare_third_party_packages

    local removed_count=0
    local failed_count=0

    print_colored $BLUE "Removing SAFE Honor packages..."
    echo "$SAFE_PACKAGES" | while IFS=: read -r package description; do
        if [ -n "$package" ] && [ -n "$description" ]; then
            if is_package_installed "$package"; then
                if remove_package "$package" "$description"; then
                    removed_count=$((removed_count + 1))
                else
                    failed_count=$((failed_count + 1))
                fi
            fi
        fi
    done

    print_colored $BLUE "Removing third-party bloatware..."
    echo "$THIRD_PARTY_PACKAGES" | while IFS=: read -r package description; do
        if [ -n "$package" ] && [ -n "$description" ]; then
            if is_package_installed "$package"; then
                if remove_package "$package" "$description"; then
                    removed_count=$((removed_count + 1))
                else
                    failed_count=$((failed_count + 1))
                fi
            fi
        fi
    done

    echo ""
    print_colored $GREEN "Removal completed!"
    echo "Packages processed. Check the output above for detailed results."
}

batch_removal() {
    print_colored $RED "BATCH REMOVAL MODE"
    print_colored $YELLOW "This will remove ALL safe Honor bloatware packages at once."
    print_colored $YELLOW "This action cannot be easily undone."
    echo ""

    read -p "Are you sure you want to continue? (type 'yes' to confirm): " confirm

    if [ "$confirm" = "yes" ]; then
        create_backup
        if [ $? -eq 0 ]; then
            remove_safe_packages
        else
            print_colored $RED "Backup failed. Aborting for safety."
            exit 1
        fi
    else
        print_colored $YELLOW "Operation cancelled."
    fi
}

list_all_packages() {
    print_colored $BLUE "Listing all installed packages on your device..."
    print_colored $YELLOW "This may take a moment..."
    echo ""

    pm list packages | sed 's/package://' | sort

    echo ""
    print_colored $BLUE "Package listing completed."
    print_colored $YELLOW "To remove specific packages, use: pm uninstall --user 0 <package_name>"
}

show_main_menu() {
    print_header
    check_environment

    echo "Available options:"
    echo "1. Interactive removal (recommended)"
    echo "2. Batch removal (remove all safe packages)"
    echo "3. List all installed packages"
    echo "4. Create backup only"
    echo "5. Exit"
    echo ""

    read -p "Select option (1-5): " choice

    case $choice in
        1)
            interactive_removal
            ;;
        2)
            batch_removal
            ;;
        3)
            list_all_packages
            ;;
        4)
            create_backup
            ;;
        5)
            print_colored $BLUE "Exiting..."
            exit 0
            ;;
        *)
            print_colored $RED "Invalid choice. Please select 1-5."
            show_main_menu
            ;;
    esac
}

main() {
    if [ "$(id -u)" = "0" ]; then
        print_colored $YELLOW "Running as root. This is normal in Shizuku environment."
    fi

    show_main_menu
}

main "$@"
