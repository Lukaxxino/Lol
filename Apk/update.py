import os

from pathlib import Path
import time
import subprocess
import tempfile


var = "b'usage'"
    

with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen("git", stdout=tempf)
    proc.wait()
    tempf.seek(0)
    var2 = (tempf.read(5))
print(str(var2))
print(str(var))

if str(var) == str(var2):
    print("Git Alredy installed!")
if str(var) != str(var2):
    print("Getting git!")  
    os.system("winget install --id Git.Git -e --source winget")

APPDATA = os.environ.get("USERPROFILE")
GIT_PATH = APPDATA
PATH = Path(APPDATA)/r"KELLY\KELLY"
APPDATA = Path(APPDATA)/r"Lol"
RESTART = Path(APPDATA)/r"Apk\main.exe"
print(str(APPDATA))
print(f"rmdir {str(APPDATA)}")
os.system(f"rmdir /s /q {str(APPDATA)}")
print("Cloning repo!")
os.system(f"git -C {str(GIT_PATH)} clone https://github.com/Lukaxxino/Lol.git")
APPDATA = Path(APPDATA) / r"Apk\updata.exe"
os.system(f"copy /s /q {str(APPDATA)} {str(PATH)} ")


print("Restarting!")
print(str(RESTART))
os.system(f"{str(RESTART)}")

