import os
import sys
import shutil
from pathlib import Path
from normalize_file import normalize

path_folder = Path(sys.argv[1])
count = 0
name_folders = {
    "images": (".jpeg", ".jpg", ".png", ".svg"),
    "video": (".avi", ".mp4", ".mov", ".mkv"),
    "documents": (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"),
    "audio": (".mp3", ".ogg", ".wav", ".amr"),
    "archives": (".zip", ".gz", ".tar"),
    "unknown": None
}

def sort_files(path_file):
    name, ext = path_file.stem, path_file.suffix
    global count
    count += 1
    if ext in name_folders["images"]:
        new_path = os.path.join(path_folder, "images")    
    elif ext in name_folders["video"]:
        new_path = os.path.join(path_folder, "video")
    elif ext in name_folders["documents"]:
        new_path = os.path.join(path_folder, "documents")
    elif ext in name_folders["audio"]:
        new_path = os.path.join(path_folder, "audio")
    elif ext in name_folders["archives"]:
        shutil.unpack_archive(path_file, os.path.join(path_folder, "archives"))
        new_path = os.path.join(path_folder, "archives")    
    else:
        new_path = os.path.join(path_folder, "unknown")
    norm_name = normalize(name)
    new_name = f"{norm_name}{ext}"
    new_path_name = os.path.join(new_path, new_name)
    try:
        path_file.rename(new_path_name)
    except:
        new_name = f"{norm_name}_{count}{ext}"
        new_path_name = Path(os.path.join(new_path, new_name))
        path_file.rename(new_path_name)