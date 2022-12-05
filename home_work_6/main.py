import shutil
import sys
import os
from pathlib import Path
from sort_file import name_folders
from sort_folder import sort_folders
from sort_file import sort_files

path_folder = Path(sys.argv[1])
list_path = list(path_folder.iterdir())
for new_folder in name_folders:
    path_new_dir = os.path.join(path_folder, new_folder)
    if not os.path.exists(path_new_dir):
        os.makedirs(path_new_dir)
    else:
        print("This folder already exists", path_new_dir)
for any_path in list_path:
    if any_path.is_dir():
        sort_folders(any_path)
        if any_path.name in name_folders:
            continue
        else:
            shutil.rmtree(any_path)
    else:
        sort_files(any_path)
print("You're welcome.")
