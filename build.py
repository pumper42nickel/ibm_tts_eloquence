#!/usr/bin/python

import os,re,sys
if (sys.version_info < (3, 0)):
    raise Exception("Python 3 required")
import urllib.request
import shutil
import tempfile
import zipfile

ORIGINAL_FILE_NAME = "eloquence_original.nvda-addon"
DRIVER_DIR = "NVDA-IBMTTS-Driver"
SYNTH_DIR = os.path.join(DRIVER_DIR, "addon", "synthDrivers", "ibmtts")


if not os.path.exists(ORIGINAL_FILE_NAME):
    print("Downloading dependencies...")
    with urllib.request.urlopen('https://jeff.tdrealms.com/Add-Ons/Eloquence.nvda-addon') as response:
        with open(ORIGINAL_FILE_NAME, "wb") as f:
            shutil.copyfileobj(response, f)
for util_file in ["msgfmt.exe", "xgettext.exe"]:
    shutil.copyfile(util_file, os.path.join(DRIVER_DIR, util_file))
if not os.path.exists(SYNTH_DIR):
    os.makedirs(SYNTH_DIR)    
with zipfile.ZipFile(ORIGINAL_FILE_NAME, 'r') as zin:
    for entry_name in zin.namelist():
        if entry_name.startswith("synthDrivers/eloquence"):
            file_name = entry_name.split("/")[-1]
            if len(file_name) == 0:
                continue
            if file_name.endswith(".py"):
                continue
            print(f"Extracting {file_name}")
            with zin.open(entry_name) as zf:
                with open(os.path.join(SYNTH_DIR, file_name), "wb") as fout:
                    shutil.copyfileobj(zf, fout)
os.chdir(DRIVER_DIR)
os.system("scons -c")
code = os.system("scons")
if code != 0:
    raise Exception(f"Scons returned error code {code}.")
print(f"scons successful, look for output file in f{DRIVER_DIR}")
