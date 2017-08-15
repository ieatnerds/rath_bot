"""
This small module will simply check if a directory exists, if it does not
then it will create the directory.
"""

import os


def makeDir(filepath):
    """This function searches for the directory."""
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
