import os
import time
import sys
import shutil


path = r"c:\users\joseph.mitambo\Downloads"
destination_directory = r"C:\Users\joseph.mitambo\Backups"
now = time.time()

for f in os.listdir(path):
    f_path = os.path.join(path, f)
    if os.path.isfile(f_path):
        if os.stat(f_path).st_mtime < now - 7 * 86400:
            shutil.copy(f_path, destination_directory)
            os.remove(f_path)
    print ("Success")