import os
from shutil import copy2, copytree
import shutil
import subprocess
import sys
import time
print("Python File Browser")
os.chdir("C:/")

def copy2_verbose(src, dst):
    print('Copying {0}'.format(src))
    copy2(src,dst)


def organize(path):
    filelist = os.listdir(path)
    answer = input("Organize " + os.getcwd() + "?(y or n)")
    if answer == "y":
        if "Org" not in filelist:
            os.mkdir("Org")
            os.mkdir("Org/pdfs")
            os.mkdir("Org/text")
            os.mkdir("Org/csv")
            os.mkdir("Org/images")
            os.mkdir("Org/exec")
            os.mkdir("Org/misc")
        for i in filelist:
            if ".pdf" in i:
                shutil.move(i, "Org/pdfs")
            elif ".csv" in i:
                shutil.move(i, "Org/csv")
            elif ".txt" in i or ".docx" in i or ".doc" in i or ".rtf" in i:
                shutil.move(i, "Org/text")
            elif ".PNG" in i or ".JPG" in i:
                shutil.move(i, "Org/images")
            elif ".exe" in i or ".bat" in i or ".cmd" in i:
                shutil.move(i, "Org/exec")
            elif "Org" in i:
                continue
            elif os.path.isdir(i):
                continue
            else:
                shutil.move(i, "Org/misc")
        print("Folder Organized")
    else:
        return

def find_all(name, path):
    result = []
    count = 0
    ccount = 0
    loadCount = 1
    for root, dirs, files in os.walk(path):
        print("Searching " + str(count) + " files" + ".    ", end='\r')
        count = count + len(files)
        ccount = ccount + 1
        if ccount % 1000:
            print("Searching " + str(count) + " files" + "..   ", end='\r')
            print("Searching " + str(count) + " files" + "...  ", end='\r')
            print("Searching " + str(count) + " files" + ".... ", end='\r')
            print("Searching " + str(count) + " files" + ".....", end='\r')
            print("Searching " + str(count) + " files" + ".... ", end='\r')
            print("Searching " + str(count) + " files" + "...  ", end='\r')
            print("Searching " + str(count) + " files" + "..   ", end='\r')
            print("Searching " + str(count) + " files" + ".  ", end='\r')
        
        
        if name in files:
            result.append(os.path.join(root, name))
    return result, count

def find2(name):
    os.system("Dir " + name + " /s /p")
def gitInit():
    os.system("git init")

def namedGitInit():
    name = input("Enter repository name: ")
    os.system("git init " + name)

def cloneRepo():
    repo = input("Enter project name: ")
    os.system("mkdir " + repo)
    os.system("cd " + repo)
    repo =repo.replace(" ", "_")
    repo = repo.lower()
    url = "https://git.gwl.bz/scm/ssm/" + repo + ".git"
    os.system("git clone " + url)
    print("Repository cloned")
    time.sleep(5)
    
def explore():
    
    folder = os.getcwd()
    folders = os.listdir(folder)
    count = 1
    
    if len(folders)==0:
        print("Empty Directory")
        
    else:
        print("Directory: " + folder)
        for i in folders:
            print(str(count) + ". " + i)
            count = count + 1
    choice = input("Enter choice: ")
    
    if choice == "..":
        os.chdir("..")
        
    elif choice == "find":
        file = input("Enter file to find: ")
        #searchCount = 0;
        #start = time.time()
        #foundPath, searchCount = find_all(file, os.getcwd())
        #end = time.time()
        #foundPath = "/".join(foundPath)

        #timeElapsed = end - start
        #print("Searched " + str(searchCount) + " files in " + str(timeElapsed) + " seconds")
        #print("File Path: " + foundPath)
        find2(file)
        x = input("Press enter to continue...")
        
    elif choice == "create":
        file = input("Enter dir name: ")
        os.mkdir(file)
        
    elif choice == "delete":
        choice = input("Enter choice to delete: ")
        p = folders[int(choice)-1]
        os.remove(p)
        
    elif choice == "backup":
        answer = input("Back up current directory?(y or n)")
        if answer == "y" or answer == "Y" or answer == "yes":
            backupname = input("Enter back up name: ")
            copytree(os.getcwd(), "C:/$BACKUP/"+backupname, copy_function=copy2_verbose)
        else:
            print("Exiting backup")
    elif choice == "organize":
        organize(os.getcwd())
    elif choice == "search":
        found = []
        sfor = input("Enter search: ")
        for i in folders:
            if sfor in i:
                print(i)
    elif choice == "git":
        print("1. Create repo from current directory")
        print("2. Create repo in new directory")
        print("3. Clone repo in current directory")
        c = input("Please choose an option: ")
        if c == "1":
            gitInit()
        elif c == "2":
            namedGitInit()
        elif c == "3":
            cloneRepo()
        else:
            print("invalid option")
                
    elif choice == "exit" or choice == "x":
        print("Exiting...")
        sys.exit()
    else:
        p = folders[int(choice)-1]
        if os.path.isfile(p):
            subprocess.Popen(p, shell=True)
        else:
            os.chdir(p)
            
    folders.clear()
    os.system('cls')

while True:
    explore()
