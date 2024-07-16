from banner import bannerX
import os
from main import main

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"
 
def listDirectoriesUsers(basePath):
    directories = []    

    if not os.path.exists(basePath):
        os.makedirs(basePath)

    with os.scandir(basePath) as entries:
        for entry in entries:
            if entry.is_dir(): 
                directories.append(entry.name)
    return directories


def listFileInDirectory(directory,basePath):
    files = []
    full_path = os.path.join(basePath, directory)
    with os.scandir(full_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    return files


    
def readFollowersFromFile(filePath,basePath):
    followers = []
    try:
        if basePath == './commonFollowers/':
           with open(filePath, 'r', encoding='utf-8') as file:
                for index,line in enumerate(file):
                        followers.append(line.strip())
        else:
            with open(filePath, 'r', encoding='utf-8') as file:
                for index,line in enumerate(file):
                    if index % 2 == 0:
                        followers.append(line.strip())
        return followers
    except FileNotFoundError:
        print(f"File not found: {filePath}")
        return []  
    except PermissionError:
        print(f"Permission error: {filePath}")
        return []  
    
    
def countUsers(followers):
    countNames = {}
    for follower in followers:

        if follower in countNames:
            countNames[follower] += 1
        else:
            countNames[follower] = 1
    return countNames
  

def calculatePoints(nameCounts):
    namePoints = {name: count * 5 for name,count in nameCounts.items()}  
    
    return namePoints


def printResults(namePoints,commonFollowers):
    os.system('cls' if os.name == 'nt' else 'clear')

    bannerX()
    count = 1
    
    print(f"\t\t\t{RED}-----------User interaction ranking---------------{RESET}")
    sortedNamePoints = sorted(namePoints.items(),key=lambda x: x[1],reverse=True)
    print(f"\t\t\t\t    {RED}Interaction analysis{RESET}")
    for name, points in sortedNamePoints[:3]:
            followInfo = "they follow each other" if name in commonFollowers else "They don't follow each other"
            print(f"\t\t\t{RED}[{count}]{RESET}{GREEN}--{name}{RESET}{RED}--[+]{followInfo}{RESET}")
            
            count+=1
            
    next = input(f"{RED}Enter for continue{RESET}")
    main()
    
def spyProfile():
    print(f"{GREEN}Enter the files with compare usernames of instagram{RESET}")
    
    basePaths = ['./comments/','./commonFollowers/']
    
    commonFollowers = []
    
    allFollowers = []
    
    for basePath in basePaths:
        
        directoriesList = listDirectoriesUsers(basePath)
        
        print(f"{GREEN}List of users: {RESET}")
        count = 1
        for directory in directoriesList:
            print(f"{count}: {directory}")
            count += 1
        
        selection = input(f"{GREEN}Enter the number of user: {RESET}")
        selection = int(selection) - 1 
    
        if 0 <= selection < len(directoriesList):
            selectedDirectory = directoriesList[selection]
            files = listFileInDirectory(selectedDirectory,basePath)
            print(f"{GREEN}Select Directory '{selectedDirectory}' in {basePath}:{RESET}")
            for idx, file in enumerate(files, start=1):
                print(f"{idx}: {basePath}\\{selectedDirectory}\\{file}")
            
            fileSelection = input(f"{RED}Enter the number of file to read: {RESET}")
            fileSelection = int(fileSelection) - 1
            
            if 0 <= fileSelection < len(files):
                selectedFile = files[fileSelection]
                file_path = os.path.join(basePath, selectedDirectory, selectedFile)
                
                followers = readFollowersFromFile(file_path,basePath)
                
                if basePath == './commonFollowers/':
                    commonFollowers.extend(followers)
                else:
                    allFollowers.extend(followers)
            else:
                print(f"{RED}Invalid file selection{RESET}")
        else:
         print(f"{RED}Selection not valid{RESET}")
         
    nameCounts = countUsers(allFollowers)
    namePoints = calculatePoints(nameCounts)
    printResults(namePoints, commonFollowers)
