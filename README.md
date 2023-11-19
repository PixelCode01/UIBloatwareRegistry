# UIBloatwareRegistry
UIBloatwareRegistry: A comprehensive repository listing UI bloatware for companies. Identify and understand pre-installed software that affects device performance.

# Bloatware Uninstaller

This repository contains Python scripts that automate the uninstallation of bloatware apps on various Android devices using the ADB (Android Debug Bridge) command-line tool.

## Supported Brands

- [Realme](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Realme)
- [Samsung](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Samsung)
- [Oppo](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Oppo)
- [Xiaomi](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Xiaomi)
- [Vivo](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Vivo)
- [Tecno](https://github.com/AnantMishra01/UIBloatwareRegistry/tree/main/Tecno)

More brands will be added in the future. Stay tuned!

For each supported brand, you will find the following files inside `<brand-name>` folder:

- `<brand>-uninstall.py`: The Python script that uninstalls bloatware apps for the specific brand.
- `<brand>-bloatware-list.md`: The list of package names of bloatware apps for the specific brand.

## Prerequisites

Before using the scripts, ensure that you have the following:

- ADB (Android Debug Bridge) installed on your computer.
- USB debugging enabled on your Android device.
- A USB cable to connect your device to the computer.
- Python installed on your computer.
## Usage

1. Connect your Android device to your computer using a USB cable.

2. Open a terminal or command prompt and navigate to the directory where the specific brand's uninstall script is located.

3. Modify the `package_names` list in the script to include the package names of the bloatware apps you want to uninstall. You can find the package names in the respective `<brand>-bloatware-list.md` file.

4. Run the script by executing the following command:
python 
`<brand>-uninstall.py`
  
  

The script will iterate through the list of package names and attempt to uninstall each app using the ADB command.

5. Monitor the terminal for the uninstallation progress. The script will print the status of each uninstallation attempt.

## [Contributing](https://github.com/AnantMishra01/UIBloatwareRegistry/blob/main/CONTRIBUTING.md)

Contributions to this repository are welcome! If you have any improvements, support for additional brands, or bug fixes, feel free to open a pull request.

## Disclaimer

Please note that uninstalling system apps can have unintended consequences and may affect the stability or functionality of your device. Use the scripts at your own risk. Make sure to review the list of package names and understand the implications before proceeding.

## License

This project is licensed under the [MIT License](LICENSE).
