import subprocess

# List of package names to uninstall

package_names=[
    "net.bat.store",
    "com.gallery20",
    "com.transsion.calculator",
    "com.transsion.calendar",
    "com.transsion.deskclock",
    "com.transsion.compass",
    "com.transsion.aivoiceassistant",
    "com.talpa.hibrowser",
    "com.zaz.translate",
    "com.transsion.letswitch",
    "com.transsion.healthlife",
    "com.transsion.notebook",
    "com.transsion.scanningrecharger",
    "com.transsion.soundrecorder",
    "com.transsion.magicshow",
    "com.rlk.weathers",
    "cn.wps.moffice_eng",
    "com.talpa.share",
    "com.transsion.tecnospot",
    "com.transsnet.store",
    "com.transsion.filemanagerx"
]

# Function to uninstall an app using ADB

def uninstall_app(package_name):

    command = f"adb shell pm uninstall --user 0 {package_name}"

    subprocess.run(command, shell=True, check=True)

# Uninstall all the apps

for package_name in package_names:

    try:

        uninstall_app(package_name)

        print(f"Uninstalled: {package_name}")

    except subprocess.CalledProcessError:

        print(f"Failed to uninstall: {package_name}")
