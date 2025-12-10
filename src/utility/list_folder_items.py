import os


def list_folder_items(folder_path, extension=".sav"):
    """
    Returns a list of save file names (not full paths) in the folder.
    """
    if not os.path.exists(folder_path):
        return []

    return [
        f
        for f in os.listdir(folder_path)
        if f.endswith(extension) and os.path.isfile(os.path.join(folder_path, f))
    ]
