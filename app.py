import os
import nbformat as nbf
import subprocess


def create_folder(name: str):
    os.mkdir(name)

def create_file(name: str, content=""):
    fd = os.open(name, os.O_RDWR|os.O_CREAT)
    os.write(fd, content.encode())

def create_first_rank_file():
     for file in files:
        create_file(file)

def create_first_rank_folder_subfolders_and_subfiles():
     for i in range(len(folders_names)):
        create_folder(folders_names[i]['folder']["nom"])
        try:
            for k in folders_names[i]['folder']["subfolder"]:
                create_folder(os.path.join(folders_names[i]['folder']["nom"], k))
        except:
            try:
                for file in folders_names[i]['folder']["file"]:
                    create_file(os.path.join(folders_names[i]['folder']["nom"], file))
            except:
                continue

