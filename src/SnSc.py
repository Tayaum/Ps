"""SnSc(SnowScript) is a version of Snow Programing launguage"""
# importing modules...
import os
from sys import argv
import httpx
import basic
from rich.console import Console
console = Console()
print = console.print

# Set CWD(Current Workind Directory) to the Dir of __file__
os.chdir(os.path.dirname(__file__))
# Making a Folder and Change Directory To that Directory If it does not Exists
# else, SnSc is A Directory Delete The Snow and Snow_data Files if Snow and Snow_data Files Exist
if not os.path.exists("SnSc"):
    os.mkdir("SnSc")
    os.chdir("SnSc")
elif os.path.exists("SnSc") and os.path.isdir("SnSc"):
    os.chdir("SnSc")
    if os.path.exists('SnSc_Main.snow'):
        os.remove('SnSc_Main.snow')

try:
    # Making a Function that Downloads the Files
    def download_files(input_str: str):
        """Downloads the Snow File"""
        get_request = httpx.get(input_str)
        with open("SnSc_Main.snow", 'w', encoding="utf-8") as file:
            file.write(get_request.text)
    # Downloading The File
    download_files(argv[0])
 
    # Running The File
    result, error = basic.run('[blue]<SnSc>[/]', 'run("SnSc_Main.snow")')

    if error:
        print("[red]" + error.as_string(), highlight=False)
    elif result:
        if len(result.elements) == 1:
            result = result.elements[0]
            print(result, highlight=False)
        else:
            result = result
            print(result, highlight=False)

except IndexError:
    print("[red]Please Add the URL To the Command")
except httpx.UnsupportedProtocol:
    print("[red]Please Add 'http://' or 'https://' protocol after URL")
except httpx.ConnectError:
    print("[red]Can't Send Get Request to This URL")
except KeyboardInterrupt:
    exit(2)
