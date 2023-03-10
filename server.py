import sqlite3
import hashlib
import socket
import threading
import time
import sys
import os
import urllib.request
import click
import requests

print("Checking BitLogics services...")
def check_internet():
    try:
        urllib.request.urlopen('https://dev0logics.github.io/BitLogics/')
        return True
    except:
        return False

if check_internet():
    clear = lambda: os.system('cls')
    clear()
else:
    clear = lambda: os.system('cls')
    clear()
    print("\x1b[33;49m[warning] BitLogics services are unreachable, check your connection!")
clear = lambda: os.system('cls')
clear()
os.system("title BitLogics - Login phase")
print("\u001b[0mBitLogics - Login phase\n")
print("Enter your ID to the BitLogics BOT on Telegram to access your account.")
print("Forgot your ID or don't have it? Visit \x1b[33;49mhttps://dev0logics.github.io/BitLogics/")
print("BOT: \x1b[33;49m@BitLogics_bot - \x1b[33;49mhttps://t.me/BitLogics_bot\n")
print("\x1b[36;49;1m[i]\u001b[0m After submitting your ID to the the bot, this page will autoatically refresh!")
print("\x1b[36;49;1m[i]\u001b[0m If after successful login the bot receives an incorrect code, the program will close automatically.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2025))

server.listen()


def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
   
    
    if cur.fetchall():
        c.send("Login successful!".encode())
        clear = lambda: os.system('cls')
        clear()
        os.system("title BitLogics")
        print("\u001b[0mBitLogics ~ Home")
        print("Logged as \x1b[36;49;1mID: \x1b[36;49m%s\n\u001b[0m" % (username))
        print("Type /commands to print a list of available commands.\n")

        def type():
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()
        def commands_function():
            print("""\n\x1b[33;49mHere are all the available commands:\u001b[0m 
#1 /commands [print a list of all available commands]
#2 /info [print informations about this program and BitLogics contacts]        
#4 /soic [start SOIC - DoS Tool]
#5 /cscan [start C-SCAN - Port Scanner Tool]
#6 /ovkl [start OVKL - Reverse Shell]
#7 /soip [start SOIP - IP Geolocation]
#8 /clear or /cls [cleans the window]
#9 /exit [exit the program]\n""")
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()

        def info_function():
            print("""\n\x1b[33;49m*INFORMATIONS SECTION*\u001b[0m
\u001b[0mInformations about this application:
\x1b[36;49;1m[i]\u001b[0mThis program is developed to work correctly with python 3.11.2.
\x1b[36;49;1m[i]\u001b[0mTo navigate through the program options use the commands.
Text in square brackets indicates: \x1b[36;49;1m[i] \u001b[0minformation\x1b[39;49m; \x1b[31;49;1m[!] error\x1b[39;49m; \x1b[33;49m[warning] warning\n
Contacts:
\x1b[36;49;1m[i]\u001b[0m To contact BitLogics you can write us an email at bitlogics.help@gmail.com or send a telegram message to the developer @Keinser.
\x1b[36;49;1m[i]\u001b[0m To follow our projects join the telegram channel @BitLogics.
\x1b[36;49;1m[i]\u001b[0m To confirm access to the program send your ID to our telegram bot @BitLogics_bot\n""")
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                command = input("""\x1b[31;49m[!] Error, invalid command!\n \x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ """ % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()
              
                
        def soic_function():
            print("""\n\x1b[33;49m*SOIC - REQUESTS FLOODER*\u001b[0m""")
            #codice qui
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()
                
                
        def cscan_function():
            print("""\n\x1b[33;49m*C-SCAN - PORT SCANNER*\u001b[0m""")
            #codice qui
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()
                
                
        def ovkl_function():
            print("""\n\x1b[33;49m*OVKL - REVERSE SHELL*\u001b[0m""")
            #codice qui
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()   

        
        def ipgeolocation_function():
            #true
                print("""\n\x1b[33;49m*SOIP - IP GEOLOCATION*\u001b[0m""")
                os.system("title BitLogics")
              
                def get_ip_location(ip_address):
                    url = f"http://ip-api.com/json/{ip_address}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        if data['status'] == 'success':
                            return {
                                'ip': data['query'],
                                'country': data['country'],
                                'region': data['regionName'],
                                'city': data['city'],
                                'latitude': data['lat'],
                                'longitude': data['lon']
                            }
                    return None

                ip_address = input("Enter an IP address: ")
                location = get_ip_location(ip_address)
                if location is not None:
                    print(f"IP: {location['ip']}")
                    print(f"Country: {location['country']}")
                    print(f"Region: {location['region']}")
                    print(f"City: {location['city']}")
                    print(f"Latitude: {location['latitude']}")
                    print(f"Longitude: {location['longitude']}\n")
                    type()
                else:
                #false
                    print("\x1b[31;49;1m[!] Error, failed to get location data for the IP address.\n")
                    ipgeolocation_function()  


        def clear_function():
            #codice qui
            clear = lambda: os.system('cls')
            clear()
            print("\u001b[0mBitLogics ~ Login>Home")
            print("Logged as \x1b[36;49;1mID%s\n\u001b[0m" % (username))
            print("Type /commands to print a list of available commands.\n")
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()       
                
        def cls_function():
            #codice qui
            clear = lambda: os.system('cls')
            clear()
            print("\u001b[0mBitLogics ~ Login>Home")
            print("Logged as \x1b[36;49;1mID%s\n\u001b[0m" % (username))
            print("Type /commands to print a list of available commands.\n")
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()


        def exit_function():
            print("\u001b[0mClosing...")
            os._exit(0)
                

        commands_dict = {
            '/commands': commands_function,
            '/info': info_function,
            '/soic': soic_function,
            '/cscan': cscan_function,
            '/ovkl': ovkl_function,
            '/soip': ipgeolocation_function,
            '/clear': clear_function,
            '/cls': cls_function,
            '/exit': exit_function
            
        }

        def main():
            command = input("\x1b[36;49;1m%s\u001b[0m@BitLogics ~ $ " % (username))
            if command in commands_dict:
                commands_dict[command]()
            else:
                print("\x1b[31;49;1m[!] Error, invalid command!\n")
                type()

        if __name__ == '__main__':
            main()
   

        
    else: 
        c.send("Login failed: the ID entered does not exist in the database!".encode())
        os.system("title BitLogics\n")
        print("""\n\x1b[31;49mLogin attempt detected:\n[!] Login failed: the ID entered does not exist in the database!""")
        print("The program will be closed in a few seconds!")
        def countdown1(p,q):
            i=p
            j=q
            k=0
            while True:
                if(j==-1):
                    j=59
                    i -=1
                if(j > 9):  
                    print(str(k)+str(i)+":"+str(j), end="\r")
                else:
                    print(str(k)+str(i)+":"+str(k)+str(j), end="\r")
                time.sleep(1)
                j -= 1
                if(i==0 and j==-1):
                    break
            if(i==0 and j==-1):
                time.sleep(1)
        countdown1(0,5) #countdown(minutes,seconds)
        os._exit(0)

#countdown
       
        

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
