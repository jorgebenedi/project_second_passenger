# Second Passenger
![image](https://github.com/user-attachments/assets/dfb1409a-c27d-4555-905f-109f46f92c1f)
### Description
```
=========================================================================================================
            Hello everyone, I’ve created a tool to extract user data from Instagram.
=========================================================================================================
If anyone knows how to guide the tool towards future improvements, feel free to reach out to me!
=========================================================================================================

We will begin by explaining how to use the tool in a guided and simple way.
As soon as you start, you will find a menu that asks if you want to:

[1]Extract user information                                                   [2]Second passenger data intelligence
      |                                                                                      | 
      |                                                                                      |
      | --> Extract all the possible information that we will later use in the second option.|                                                      
                                                                                             |
                                                                                             |
Once the data from a profile is extracted, we will apply the data intelligence functions <-- |
which help identify the most recent people who have followed the user and common followers.
Subsequently, we can perform a local scan to find out which users the victim interacts with the most, quite accurately.

Recommendations
----Do not use your personal account, there is a risk of permanent account closure.
----Use accounts with which you have interacted with other users,
this makes Instagram less likely to suspect you during scans.
----Use saved sessions to avoid multiple logins,
this will help reduce the risk of being banned.
----Do not scan multiple users in a short period of time if Instagram is warning you,
take some time between scans (several days).
----Change accounts used for scanning in credentials.txt.
```
### Example of data extraction
![Captura de pantalla 2024-07-15 2](https://github.com/user-attachments/assets/d17a80d5-1a6a-480a-b69c-f4572bb47b9a)

### Technologies
```
python3
instaloader
```
### Installation Guide
```
apt update && apt install git
apt install python3
git clone https://github.com/jorgebenedi/project_second_passenger.git
cd project_second_passenger
apt install pip
pip install -r requirements.txt
python3 main.py
```



