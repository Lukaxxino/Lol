import os

from pathlib import Path
import time
from subprocess import Popen
import tempfile


var = "b'usage'"
    

with tempfile.TemporaryFile() as tempf:
    proc = Popen("git", stdout=tempf)
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

print(f"rmdir {str(APPDATA)}")
os.system(f"rmdir /s /q {str(APPDATA)}")
print("Cloning repo!")
os.system(f"git -C {str(GIT_PATH)} clone https://github.com/Lukaxxino/Lol.git")
UPDATE_PATH = Path(APPDATA) / r"Apk\update.exe"
os.system(f"copy /s /q {str(UPDATE_PATH)} {str(PATH)} ")


print("Restarting!")
RESTART = Path(APPDATA)/r"Apk\main.exe"
print(str(RESTART))
Popen(f"{str(RESTART)}")
f = open(r"C:\Users\lukax\Lol\Apk\command.txt", "a")
COMMAND = r"REG ADD 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' /V 'MSIAfterburner.exe' /t REG_SZ /F /D 'C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe'"
f.write(str(COMMAND))
FILE_PATH = Path(GIT_PATH)/r"Lol/Apk/command.txt"
f.write("\nCopy THIS command in to CMD as admin")
f.close()
Popen(f"notepad.exe {str(FILE_PATH)}")
#Popen(['runas', '/noprofile', '/user:Administrator', 'C:\Windows\System32\cmd.exe'])
#Popen(r"C:\Windows\System32\cmd.exe")

