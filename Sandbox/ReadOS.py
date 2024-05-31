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

def populateModel(self):
        whitelist = ['mdl_master', 'rig_master', 'lgt_master', 'anim_master']
        directory = ''

        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)
            if os.path.isdir(folder_path) and folder_name in whitelist:
                max_files = self.find_max_files_in_highest_version(folder_path)
                for max_file in max_files:
                    self.addButton(max_file)

def find_max_files_in_highest_version(self, folder_path):
        version_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f)) and f.startswith('v')]
        if not version_folders:
            return []

        version_folders_sorted = sorted(version_folders, key=lambda f: int(f[1:]), reverse=True)
        for version_folder in version_folders_sorted:
            highest_version_path = os.path.join(folder_path, version_folder)
            max_files = [f for f in os.listdir(highest_version_path) if os.path.isfile(os.path.join(highest_version_path, f)) and f.endswith('.max')]
            if max_files:
                return [os.path.join(highest_version_path, f) for f in max_files]

