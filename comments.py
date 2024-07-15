import time
import os
from banner import bannerX
from main_one import main

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

def createDirectory(usernameToScrape):
    os.system('cls' if os.name == 'nt' else 'clear')
    bannerX()
    currentDate = time.strftime("%d-%m-%Y_%H-%M")

    directoryMain = "comments"
    directorySecundary = f"{usernameToScrape}"
    directories = os.path.join(directoryMain, directorySecundary)
    if not os.path.exists(directories):
        os.makedirs(directories)
        
    fileName = f"comments_{usernameToScrape}_{currentDate}.txt"
    filePath = os.path.join(directories,fileName)
    
        
    return filePath


def comments(profile,usernameToScrape):
    path = createDirectory(usernameToScrape)
    countComments =0
    try:
      with open(path, "a+",encoding="utf-8") as file: #Abrimos el archivo de salida para escribir los nombres de los seguidores
        for i,post in enumerate(profile.get_posts(),start=1):
            postComments = post.get_comments()
            print(f"{RED}[i]{RESET}{GREEN}--Post[{i}]{RESET}")
            for comments in postComments:
                    file.write(comments.owner.username + "\n")
                    file.write(comments.text + "\n")
                    countComments += 1
                    if countComments % 5 == 0: # cada 5 publicaciones descargadas pausa de 5 segundos
                        print(f"{RED}[+]{RESET}{GREEN}--Extracted comments: {countComments}{RESET}")
                        print(f"{RED}Sleeping comments for 10 second{RESET}")
                        time.sleep(10)
    except Exception as error:
            print(f"{RED}[RISK]{RESET}{GREEN}--Instagram has detected suspicious behavior on your account, review it and accept the message or wait a few days{RESET} \n{RED}--> {error}{RESET}")
            
    enter = input(f"{RED}Enter for continue{RESET}")  # Pausa para permitir que el usuario continúe
    main()  # Llama a la función principal para continuar            

