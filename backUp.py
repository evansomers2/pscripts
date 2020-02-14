import os
import shutil

print("Python Backup v1.0")
path = input("Enter folder path: ")

backup = input("Enter backup folder name: ")

backupPath = "C:/"+backup

shutil.copytree(path, backupPath)

print("Back up completed")
