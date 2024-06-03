import os
import json
import sys

sys.path.append(r'C:\Users\nghia.tran\Documents\Sandbox')

from Coconut import *

DATA_FILE = 'workfile_manager_data.json'
PROJECT_DIRECTORY = r'C:\Users\nghia.tran\Documents\Sandbox'
USER_DATA_DIRECTORY = r'C:\Users\nghia.tran\Documents\Sandbox\UserData'

def load_project_folders(directory):
     project_folders = []  # Changed: renamed to project_folders
     for item in os.listdir(directory):
         if os.path.isdir(os.path.join(directory, item)):
             project_folders.append(item)
     return project_folders

def load_child_folders(directory):
     child_folders = []  # Changed: renamed to child_folders
     for item in os.listdir(directory):
         if os.path.isdir(os.path.join(directory, item)):
             child_folders.append(item)
     return child_folders

def load_folders(directory):
    folders = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)) and not item.startswith('.'):
            folders.append(item)
    return folders


