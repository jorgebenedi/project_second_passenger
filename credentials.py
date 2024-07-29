import instaloader
import os
from banner import bannerX
import sys
from instaloader.exceptions import  ConnectionException, BadResponseException

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

def createSessionDirectory(username):
    directoryMain = "sessions"
    if not os.path.exists(directoryMain):
        os.makedirs(directoryMain)
        
    return directoryMain

def saveCrendentials(username,password):
    with open('credentials.txt','w') as file:
        file.write(f"{username}\n{password}")

def loadCredentials():
    if not os.path.exists('credentials.txt'):
        return None

    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None

def prompCredentials(): 
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    saveCrendentials(username, password)
    return username, password

def logicalCredentials():
    credentials = loadCredentials() 
     
    if credentials is None:
        username,password = prompCredentials()
    else:
        username, password = credentials
    
    print(f"\t{RED}[X]{RESET}{GREEN}--Extract private account(hight risk){RESET}")
    print(f"\t{RED}[XX]{RESET}{GREEN}--Extract public account{RESET}")
    option = input(f"{GREEN}Enter the option: {RESET}")
    
    if option == "X":
        try:
            IG = instaloader.Instaloader(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/126.0.0.0 Safari/537.36")
            IG.login(username, password)
        except instaloader.exceptions.BadCredentialsException:
            print(f"{RED}[!]{RESET}{GREEN}--Invalid username or password. Please check your credentials and try again.{RESET}")
            return None, None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None, None
        
    if option == "XX":
        try:
            try:
                IG = instaloader.Instaloader(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/126.0.0.0 Safari/537.36")
                IG.context.login(username, password)
                IG.load_session_from_file(username, f"sessions/{username}_session")
                print(f"Session for {RED}{username}.{RESET} {GREEN}loaded successfully.")
            except instaloader.exceptions.BadCredentialsException:
                print(f"{RED}[RISK]{RESET}{GREEN}--login error check it instagram account or file creedentials{RESET}")
                sys.exit(1) 
        except FileNotFoundError:
            print(f"No session found for {RED}{username}.{RESET} Logging in...")
            IG.context.login(username,password)
            session = createSessionDirectory(username)
            IG.save_session_to_file(f"{session}/{username}_session")
            print(f"Session for {RED}{username}{RESET} saved successfully.")
            
    usernameToScrape = input(f"{GREEN}Enter the username you want to scrape: {RESET}")
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    print(f"\t\t\t{RED}Second Passenger objective -->{RESET} {usernameToScrape}" )
    
    try:
        profile = instaloader.Profile.from_username(IG.context,usernameToScrape)
        return IG, profile, usernameToScrape     
    except (ConnectionException, BadResponseException, instaloader.exceptions.InstaloaderException) as error:
        print(f"{RED}[!]{RESET}{GREEN}-->User not found or not exist{RESET} \n {RED}-->{error}{RESET}")
    
    
