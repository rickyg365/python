import os
from os import walk

from typing import List


""" 

"""


class DirectoryData:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        
        # All Content
        self.contents = list() # List or Dict
        
        # Split Content
        self.files = list() # List
        self.dirs = list() # Set?

        # Get Data
        self.get_current_data()

    def __str__(self) -> str:
        # Seperator
        sep = f"{'-'*40}"
        # Extract Data into String
        contents = "\n".join((f" {x}" for x in self.contents))
        directories = "\n".join((f" {x}" for x in self.dirs))
        files = "\n".join((f" {x}" for x in self.files))
        # Todo: Add cache for these string values

        # Check new strings
        content_check = contents != ''
        file_check = files != ''
        dir_check = directories != ''

        if not content_check and not file_check and not dir_check:
            return f"\n[{self.dir_path}] {'Found' if self.check_path() else 'Not Found'}:\n No Content"

        txt = f"""
[{self.dir_path}] {'Found' if self.check_path() else 'Not Found'}:
{sep}        
All Dirs:
{directories}

All Files:
{files if files != '' else ' '}

All Contents:
{contents if contents != '' else ' '}
{sep}"""
        return txt

    def check_path(self) -> bool:
        """ Check if directory exist """
        if os.path.isdir(self.dir_path):
            return True
        return False

    @staticmethod
    def get_abs_path(base_path: str, items: List[str]) -> List[str]:
        # Absolute Path
        abs_names = []
        for item in items:
            abs_names.append(f"{base_path}\{item}")

        return abs_names


    def get_current_data(self) -> None:
        """ Update data w/ latest dir contents """
        # Check to make sure the dir exists
        if self.check_path():
            # Walk through current path
            for (dirpath, dirnames, filenames) in walk(self.dir_path):
                """
                dirpath  # str
                dirnames # List[str]
                filenames # List[str]
                """
                # Get Absolute Paths
                abs_files = self.get_abs_path(dirpath, filenames)
                abs_dirs = self.get_abs_path(dirpath, dirnames)

                # Add Files and Directories to self.contents
                self.contents.extend(abs_dirs)
                self.contents.extend(abs_files)

                # Add Directories to self.dirs
                if dirnames is not None:
                    self.dirs.extend(dirnames)
                
                # Add Files to self.files
                if filenames is not None:
                    self.files.extend(filenames)


def main():
    return

if __name__ == '__main__':
    main()
