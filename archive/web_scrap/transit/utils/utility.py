import os
import shutil

from pathlib import Path


def map_directory_structure():
    pass


def move_file(filename: str):
    """ copies file from storage location to current data directory """
    # Using Relative Path
    #* source = f"transit/gtfs/{filename}"
    #* destination = f"data/{filename}"
    
    # Using Absolute Path
    base_path = Path.cwd()

    source = base_path / f"gtfs/{filename}"
    destination = base_path / f"data/{filename}"

    # If target file doesnt exist
    if not os.path.isfile(source):
        print("Unable to find Source file")
        return

    # Check if file is already in current data directory
    if os.path.isfile(destination):
        # Delete already existing data
        print("Deleted already existing data")
        os.remove(destination)
    
    # Move file from destination to source
    os.rename(source, destination) # throws error if file exist in destination

    #? DEBUG
    #* print(f"Source: {source}")
    #* print(f"Destination: {destination}")

    #* data_files = os.listdir("data/")
    #* source_files = os.listdir("transit/gtfs/")

    #* print(data_files)
    #* print(source_files)


def get_data(filename: str, custom_datapath: str=None):
    file_no_ext = filename.split('.')[0]

    # Using Absolute Path
    base_path = Path.cwd()
    
    source = base_path / f"gtfs/{filename}"
    destination = base_path / f"data/{file_no_ext}"

    if custom_datapath is not None:
        destination = base_path / custom_datapath
    
    shutil.unpack_archive(source, destination)

