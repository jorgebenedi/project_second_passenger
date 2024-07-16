import os
import time
from banner import bannerX
from main import main

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

def createDirectoryVictim(targetUser,option):
    currentDate = time.strftime("%d-%m-%Y_%H-%M")

    directoryMain = "Followers"
    directorySecundary = f"{targetUser}"
    directories = os.path.join(directoryMain, directorySecundary)
    if not os.path.exists(directories):
        os.makedirs(directories)
    if option == "1":
        fileName = f"followers_{targetUser}_{currentDate}.txt"
        filePath = os.path.join(directories,fileName)
    else:
        fileName = f"following_{targetUser}_{currentDate}.txt"
        filePath = os.path.join(directories,fileName)
        
    return filePath


def DirectoryCommonFollowers(usernameToScrape):
    currentDate = time.strftime("%d-%m-%Y_%H-%M")

    directoryMain = "commonFollowers"
    directorySecundary = f"{usernameToScrape}"
    directories = os.path.join(directoryMain, directorySecundary)
    if not os.path.exists(directories):
        os.makedirs(directories)
    fileName = f"commonFollowers_{usernameToScrape}_{currentDate}.txt"
    filePath = os.path.join(directories,fileName)
    return filePath 

class CustomConnectionException(Exception):
    def __init__(self, message):
        super().__init__(message)
def scrapeFollowers(profile, usernameToScrape,option):
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    
    path = createDirectoryVictim(usernameToScrape, option)
    
    followersList = []
    
    count = 0
    
    followersExtract = 0
    
    
    followers = profile.followers
    following = profile.followees
    

    print(f"{RED}[+]--Starting extraction{RESET}")
    try:
        if option == "1":
                
                if (0 < followers <= 500):    
                    timeOuts = 10
                elif (500 < followers <= 1000):    
                    timeOuts = 15
                elif (1000 < followers <= 2000):
                    timeOuts = 20
                elif (2000 < followers <= 3000):
                    timeOuts = 25
                else:
                    timeOuts = 30
                    
                print(f"{RED}[!]{RESET}{GREEN}--Timeouts set to: {timeOuts} seconds{RESET}")
                for follower in profile.get_followers():
                    username = follower.username 
                    if username not in followersList: 
                        followersList.append(username)
                        count += 1
                        followersExtract += 1  
                        if count % 50 == 0: 
                            print(f"{RED}[+]{RESET}{GREEN}--followers extracted: {followersExtract}{RESET}")
                            print(f"{RED}[WAITING]--Sleeping for {timeOuts} second{RESET}")
                            time.sleep(timeOuts)
                            count =0
                with open(path, "a+") as file: 
                    for username in followersList:
                        file.write(username + "\n")           
                
                    
                
        elif option == "2":
                
            
            if (0 < following <= 500):    
                timeOuts = 10
            elif (500 < following <= 1000):    
                timeOuts = 15
            elif (1000 < following <= 2000):
                timeOuts = 20
            elif (2000 < following <= 3000):
                timeOuts = 25
            else:
                timeOuts = 30
                    
            with open(path, "a+") as file: 
                for follower in profile.get_followees():
                    username = follower.username 
                    if username not in followersList: 
                        followersList.append(username)
                        file.write(username + "\n")
                        count += 1
                        followersExtract += 1  
                        if count % 50 == 0: 
                            print(f"{RED}[+]{RESET}{GREEN}--followers extracted: {followersExtract}{RESET}")
                            print(f"{RED}[WAITING]--Sleeping for {timeOuts} second{RESET}")
                            time.sleep(timeOuts)
                            count =0   

                
                        
                       
    except Exception as error:
            print(f"{RED}[RISK]{RESET}{GREEN}--Instagram has detected suspicious behavior on your account, review it and accept the message or wait a few days{RESET} \n{RED}--> {error}{RESET}")
                         
    print(f"{GREEN}Total followers extracted: {followersExtract} saved in {path}{RESET}")
      
    if followersExtract == 0:
        print(f"{RED}[RISK]{RESET}{GREEN}--Followers extract 0 instagram has detected suspicious behavior on your account, review it and accept the message or wait a few days{RESET}")              

    
    enter = input(f"{RED}Enter for continue{RESET}")  
    main()  
        
   

def listDirectoriesUsers():
    currentPath = f'./Followers/' 
    directories = []    

    if not os.path.exists(currentPath):
        os.makedirs(currentPath)

    with os.scandir(currentPath) as entries: 
        for entry in entries:
            if entry.is_dir(): 
                directories.append(entry.name)
    return directories


def listFileInDirectory(directory, basePath):
    files = []
    full_path = os.path.join(basePath, directory)
    with os.scandir(full_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    return files

def readFollowersFromFile(filePath):
    try:
        with open(filePath, 'r') as file:
            return set (file.read().splitlines())
    except FileNotFoundError:
        print(f"File not found: {filePath}")
        return set
    except PermissionError:
        print(f"File not found: {filePath}")
        return set


def listFilesUsers(directory):
    files = [] 
    with os.scandir(directory) as entries: 
        for entry in entries:
            if entry.is_file: 
                files.append(entry.name)
    return files

def compareFollowers():
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    print(f"{GREEN}Enter the files with compare usernames of instagram")
    directoriesList = listDirectoriesUsers()
    print("List of users: ")
    count = 1
    for directory in directoriesList:
        print(f"[{count}]--{directory}")
        count += 1
    
    selection = input(f"{RESET}{RED}Enter the number of user: {RESET}")
    selection = int(selection) - 1

    if 0 <= selection < len(directoriesList):
        selectedDirectory =  directoriesList[selection]
        basePath = './Followers'

        files = listFileInDirectory(selectedDirectory,basePath)        
        if not files:
            print("No files found in the selected directory.")
            return

    print(f"{GREEN}Select user '{selectedDirectory}':")

    print(f"{RED}[1]{RESET}{GREEN}--Common followers{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}--Last followers{RESET}")
    option = input(f"{RED}Enter option: {RESET}")
    countFiles = 1
    
    for file in files:
            print(f"[{countFiles}] {selectedDirectory}\{file}")
            countFiles +=1
    
      
    if option == "1":
        file1 = input(f"{RESET}{RED}Enter the followers: {RESET}")
        file1 = int(file1) - 1
        
    if option == "1":
        file2 = input(f"{RESET}{RED}Enter the followers: {RESET}")
        file2 = int(file2) - 1
        
            
    if option == "2":
        file1 = input(f"{RED}Enter the first date: {RESET}")
        file1 = int(file1) - 1
    
    if option == "2":
        file2 = input(f"{RED}Enter the second date: {RESET}")
        file2 = int(file2) - 1
    
    
    if 0 <= file1 < len(files):
        selectedFile1 = os.path.join(basePath, selectedDirectory, files[file1])
    else:
        print("Invalid file selection.")
        return
        
    
        
    if 0 <= file2 < len(files):
        selectedFile2 = os.path.join(basePath, selectedDirectory, files[file2])
    else:
        print("Invalid file selection.")
        return
    
    followers1 = readFollowersFromFile(selectedFile1)

    followers2 = readFollowersFromFile(selectedFile2)

    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        bannerX()
        commonFollowers = followers1 & followers2
        followersNotFollowYou = (followers1 - followers2)
        followersNotFollowThem = (followers2 - followers1)   
        if commonFollowers:                            
            countCommons = 1
            print(f"\n\t\t\t\t{RED}--------Common Followers---------{RESET}")
            for follower in commonFollowers:
                print(f"\t\t\t\t{RED}[{countCommons}]{RESET}{GREEN}--{follower}{RESET}")
                path = DirectoryCommonFollowers(selectedDirectory)
                with open(path, "a+") as file: 
                    file.write(follower + "\n")
                countCommons+=1
        
            
        if followersNotFollowYou:
            countfollowersNotFollowYou = 1
            print(f"\n\t\t\t\t{RED}--------followers who follow him but you have followed him---------{RESET}")
            for follower in followersNotFollowYou:
                print(f"\t\t\t\t{RED}[{countfollowersNotFollowYou}]{RESET}{GREEN}--{follower}{RESET}")

                countfollowersNotFollowYou+=1
        if followersNotFollowThem:
            countfollowersNotFollowThem = 1
            print(f"\n\t\t\t\t{RED}--------followers who follow him but you have followed him---------{RESET}")
            for follower in followersNotFollowThem:
                print(f"\t\t\t\t{RED}[{countfollowersNotFollowThem}]{RESET}{GREEN}--{follower}{RESET}")
                countfollowersNotFollowThem+=1
        else:
            print(f"{RED}No common followers found.{RESET}")
      
        print(f"{RED}Data in {path}{RESET}")   
    elif option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        bannerX()   
        uniqueFollowers = followers2 - followers1
        print(f"\t\t\t\t{RED}--------Unique Users in First File---------{RESET}")
        if uniqueFollowers:
            for follower in uniqueFollowers:
                print(f"\t\t\t\t{RED}Users found: {RESET} {GREEN}{follower}{RESET}" )
        else:
            print(f"{RED}No unique users found in the first file.{RESET}")
            
    
    input(f"{RED}Press enter to exit{RESET}")
    main()
  
