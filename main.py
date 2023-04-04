from colorama import Fore
import threading, time, psutil, requests, json, webbrowser
from functions import port_scanner, clear
import matplotlib.pyplot as plt

while True:
    #Display project name
    clear()
    print("")
    print(f" 💦     {Fore.BLUE} ██████╗     █████╗    ██╗   ███╗   ██╗       💦")
    print(f"    💦  {Fore.BLUE} ██╔══██╗   ██╔══██╗   ██║   ████╗  ██║    💦")
    print(f" 💦     {Fore.BLUE} ██████╔╝   ███████║   ██║   ██╔██╗ ██║       💦")
    print(f"    💦  {Fore.BLUE} ██╔══██╗   ██╔══██║   ██║   ██║╚██╗██║    💦")
    print(f" 💦     {Fore.BLUE} ██║  ██║"f"{Fore.RED}██╗"f"{Fore.BLUE}██║  ██║{Fore.RED}██╗{Fore.BLUE}██║"f"{Fore.RED}██╗"f"{Fore.BLUE}██║ ╚████║{Fore.RED}██╗{Fore.BLUE}    💦")
    print(f"    💦  {Fore.BLUE} ╚═╝  ╚═╝"f"{Fore.RED}╚═╝"f"{Fore.BLUE}╚═╝  ╚═╝{Fore.RED}╚═╝{Fore.BLUE}╚═╝{Fore.RED}╚═╝{Fore.BLUE}╚═╝  ╚═══╝{Fore.RED}╚═╝{Fore.BLUE} 💦")
    print("")
    print(f"{Fore.YELLOW}ᴀ ᴄʏʙᴇʀꜱᴇᴄᴜʀɪᴛʏ ꜰʀᴀᴍᴇᴡᴏʀᴋ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ꜰᴏʀ ᴇɴᴛᴇʀᴘʀɪꜱᴇ ɴᴇᴛᴡᴏʀᴋ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
    print(Fore.RESET)

    #Display project options
    print(f"{Fore.CYAN}Options -")
    print("")
    print(f"{Fore.GREEN}1."f"{Fore.MAGENTA} Port Scanner")
    print(f"{Fore.GREEN}2."f"{Fore.MAGENTA} Network Analyzer [ML Beta]")
    print(f"{Fore.GREEN}3."f"{Fore.MAGENTA} Github Link")
    print('')
    print(f"{Fore.GREEN}0."f"{Fore.MAGENTA} Exit Program")

    print(f"{Fore.CYAN}")
    #Wait on user input
    UserInput1 = (input("Choose an Option: "))

    #Input Tree
    if UserInput1.strip() == '1':
        clear()
        print('Port scanner is Running...')
        # Formatting Whitelist Ports
        with open('Whitelisted Ports.txt', 'r') as WhitelistedPortsFile:
            WhitelistedPortsList = [int(port.strip()) for port in WhitelistedPortsFile.readlines()]

        # Port scanning via multi-thread distribution
        start = time.time()  # Function Start Time
        for port in range(1, 60000):
            if port in WhitelistedPortsList:
                continue

            thread = threading.Thread(target=port_scanner, args=[port])
            thread.start()

        end = time.time()  # Function End Time


        # Function to send Push Notification

        #def pushbullet_noti(title, body):
        #    TOKEN = 'o.cDR7EQue2balRRC56YoMuz0rENGyW5ec'  # Pass your Access Token here
        #    # Make a dictionary that includes, title and body
        #    msg = {"type": "note", "title": title, "body": body}
        #    # Sent a posts request
        #    resp = requests.post('https://api.pushbullet.com/v2/pushes',
        #                         data=json.dumps(msg),
        #                         headers={'Authorization': 'Bearer ' + TOKEN,
        #                                  'Content-Type': 'application/json'})
        #    if resp.status_code != 200:  # Check if fort message send with the help of status code
        #        raise Exception('Error', resp.status_code)
        #    else:
        #        print('Message sent')


        #message = ''
        #for port in OpenPorts:
        #    message = message + str(port) + '\n'

        #pushbullet_noti('Open Ports Detected:\n', message)
        print("")
        print("")
        print("Scan Complete!")
        print(f"Time taken for scan: {end - start} Seconds")
        print('Hit enter to continue...')
        input()

    elif UserInput1.strip() == '2':
        clear()
        UPDATE_DELAY = 1  # in seconds

        print(f"""{Fore.BLUE}
                  @@@@@@@@@@@@@@@@@@@@@@        
             @@@@@@@@                @@@@@@@    
          @@@@@@                         @@@@@ 
          @@@      @@@@@@@@@@@@@@@@@@@       @@@
                @@@@@@              @@@@@@      
               @@@                     @@@@     
                       @@@@@@@@@@@@@            
                    @@@@          @@@@      

                          @@@@@ 

                           @@@             """)
        print('')
        print('Network Analyser')
        time.sleep(2)
        clear()


        def get_size(bytes):
            """
            Returns size of bytes in a nice format
            """
            for unit in ['', 'K', 'M', 'G', 'T', 'P']:
                if bytes < 1024:
                    return f"{bytes:.2f}{unit}B"
                bytes /= 1024


        # get the network I/O stats from psutil
        io = psutil.net_io_counters()
        # extract the total bytes sent and received
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
        i = 0

        while True:
            i += 1
            # sleep for `UPDATE_DELAY` seconds
            time.sleep(UPDATE_DELAY)
            # get the stats again
            io_2 = psutil.net_io_counters()
            # new - old stats gets us the speed
            us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
            # print the total download/upload along with current speeds
            print(f"{Fore.RED}\n Upload: {get_size(io_2.bytes_sent)} \n"
                  f"{Fore.GREEN}Download: {get_size(io_2.bytes_recv)} \n"
                  f"{Fore.RED}Upload Speed: {get_size(us / UPDATE_DELAY)}/s \n"
                  f"{Fore.GREEN}Download Speed: {get_size(ds / UPDATE_DELAY)}/s \n"
                  f"{Fore.CYAN}----------------------------------------", end="\r")
            if i == 5:
                print('Hit enter to continue...')
                input()
                break
            # update the bytes_sent and bytes_recv for next iteration
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

    elif UserInput1.strip() == '3':
        clear()
        print(webbrowser.open('https://github.com/Friedlguana/R.A.I.N.'))

    elif UserInput1.strip() == '0':
        break

    else:
        clear()
        print('Invalid Input. Hit enter to return')
        input()