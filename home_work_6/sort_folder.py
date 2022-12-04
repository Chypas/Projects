from sort_file import sort_files

def sort_folders(path_folder):
    list_path_subfolder = list(path_folder.iterdir())
    if not list_path_subfolder:
        return 
    else:
        for file_folder in list_path_subfolder:
            if file_folder.is_dir():
                sort_folders(file_folder)
            else:
                sort_files(file_folder)
    return