import os

USE_HOME_DIR = False 
TD_DIR_NAME = ".pytd"
TD_FILE = "pytd"
TD_PATH = (os.getcwd() if not USE_HOME_DIR else os.path.expanduser("~")) + "/" + TD_DIR_NAME
TD_FILE_PATH = f"{TD_PATH}/{TD_FILE}" 

def init():
    if not os.path.exists(TD_PATH):
        os.mkdir(TD_PATH)

    if not os.path.exists(TD_FILE_PATH):
        open(TD_FILE_PATH, "w+")
    

def write(msg: str):
    if not msg:
        return

    with open(TD_FILE_PATH, "a") as f:
        f.write(f"{msg}\n")

def read():
    lst = []
    with open(TD_FILE_PATH, "r") as f:
        lst = [line.strip('\n') for line in f]

    return lst
