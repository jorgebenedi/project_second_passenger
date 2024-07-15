import os
from credentials import logicalCredentials
from banner import bannerX



RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    print(f"\t\t\t\t\t{RED}Created by Black_Code{RESET}")
    print(f"\t\t\t\t     {RED}Welcome to Second Passenger{RESET}")

    print(f"{RED}[1]{RESET}{GREEN}--Scraping data users{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}--Second passenger data intelligence{RESET}")
    print(f"{RED}[3]{RESET}{GREEN}--Exit{RESET}")
    optionMain = input(f"{RED}Enter__option: {RESET}")
    
    if optionMain == "1":
        
        IG,profile, usernameToScrape = logicalCredentials() 
        print(f"\t{RED}[1]{RESET}{GREEN}--Extract followers{RESET}")
        print(f"\t{RED}[2]{RESET}{GREEN}--Extract following{RESET}")
        print(f"\t{RED}[3]{RESET}{GREEN}--Download profile{RESET}")
        print(f"\t{RED}[4]{RESET}{GREEN}--Extract comments profile{RESET}")
        print(f"\t{RED}[5]{RESET}{GREEN}--Exit{RESET}")
        option = input(f"{RED}Enter__option: {RESET}")
        if option == "1" or option == "2":
            from followers import scrapeFollowers
            scrapeFollowers(profile, usernameToScrape,option)
        elif option == "3":
            from download import downloadVideos
            downloadVideos(IG,profile,usernameToScrape)
        elif option == "4":
            from comments import comments
            comments(profile,usernameToScrape)
        elif option == "5":
            exit

    elif optionMain == "2":
        print(f"\t{RED}[1]{RESET}{GREEN}--Compare followers{RESET}")
        print(f"\t{RED}[2]{RESET}{GREEN}--Spy profile{RESET}")
        option = input(f"{GREEN}Enter the option: {RESET}")
        if option == "1":
            from followers import compareFollowers
            compareFollowers()
        elif option == "2":
            from spyProfile import spyProfile
            spyProfile()
    elif optionMain == "3":
            exit
            

    
if __name__ == "__main__":
    main()