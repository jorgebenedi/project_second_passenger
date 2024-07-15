from instaloader import  Profile
import time
from instaloader import Profile
import os
from main import main
from banner import bannerX

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

def directoryDownload():
    directoryMain = "downloadposts"
    if not os.path.exists(directoryMain):
        os.makedirs(directoryMain)
    

    return directoryMain 

def DownloadPostsPhotosVideos(IG,usernameToScrape):
    print(f"\t{RED}[1]{RESET}{GREEN}--Download videos{RESET}")
    print(f"\t{RED}[2]{RESET}{GREEN}--Download photos{RESET}")
    
    option = input(f"{RED}Enter the option: {RESET}")
    
    print(f"{GREEN}Starting to download...{RESET}")
    profile = Profile.from_username(IG.context,usernameToScrape)
    directoryUser = directoryDownload()
    
    currentDir = os.getcwd() # guardamos directorio base
    os.chdir(directoryUser) # cambiamos de directorio
    
    count = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    if option == "1":
        name = "videos"
        for post in profile.get_posts():
            if post.is_video:
                    print(f"{RED}[+]{RESET}{GREEN}--Downloading video number: {count}{RESET}")
                    IG.download_post(post, target=usernameToScrape)
                    count += 1
                    if count % 5 == 0: # cada 5 publicaciones descargadas pausa de 5 segundos
                        print(f"{RED}[WAITING]--Sleeping for 10 seconds{RESET}")

                        time.sleep(10)
                    
        print(f"{RED}Finished downloading {name}{RESET}")
        
    elif option == "2":
        name = "photos"
        for post in profile.get_posts():
            if not post.is_video:
                print(f"{RED}[+]{RESET}{GREEN}--Downloading photo number: {count}{RESET}")
                IG.download_post(post, target=usernameToScrape)
                
                count += 1
                if count % 5 == 0:  # cada 5 publicaciones descargadas pausa de 10 segundos
                    print(f"{RED}[WAITING]--Sleeping for 10 seconds{RESET}")
                    time.sleep(10)
        print(f"{RED}Finished downloading {name}{RESET}")
    
    
        
    
    print(f"{RED}Posts downloaded to: {directoryUser}{RESET}")
    os.chdir(currentDir)
    enter = input(f"{RED}Press enter to continue{RESET}")
    main()
    return    
           
def downloadVideos(IG,profile,usernameToScrape):
    # de aqui lo quite
    #postsSortedByLikes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

    print(f"\t{RED}[1]{RESET}{GREEN}--Download posts{RESET}")
    print(f"\t{RED}[2]{RESET}{GREEN}--Download posts photos or videos{RESET}")
    print(f"\t{RED}[3]{RESET}{GREEN}--Exit to main menu{RESET}")
    option = input(f"{RED}Enter the option: {RESET}")
    if option == "1":
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            bannerX()
            IG.download_profile(usernameToScrape,profile_pic=True)
            directoryDownload()
            enter = input(f"{RED}Press enter to continue{RESET}")
            main()
        except Exception as error:
            print(f"{RED}[RISK]{RESET}{GREEN}--Instagram has detected suspicious behavior on your account, review it and accept the message or wait a few days{RESET} \n{RED}--> {error}{RESET}")  
    if option == "2":
        DownloadPostsPhotosVideos(IG,usernameToScrape)
    if option == "3":
        main() # llamamos a main() para regresar al menú principal
        return
        
                    
                        
                        


    
  

   
