import os


def move_file(source_path, destination_dir):
    new_path = os.path.join(destination_dir, os.path.basename(source_path))
    os.rename(source_path, new_path)
    return new_path