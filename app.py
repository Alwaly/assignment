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

