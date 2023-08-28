import time, threading
from functions import port_scanner, OpenPorts

print('Port scanner is Running...')
# Formatting Whitelist Ports
with open("Whitelisted Ports.txt", 'r') as WhitelistedPortsFile:
    WhitelistedPortsList = [int(port.strip()) for port in WhitelistedPortsFile.readlines()]

# Port scanning via multi-thread distribution
start = time.time()
for port in range(1, 65536):
    if port in WhitelistedPortsList:
        continue

    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()

end = time.time() 

#Message formatting
message = ''
for port in OpenPorts:
    message = message + str(port) + '\n'

if len(OpenPorts) == 0:
    print('No port detected.')
input('Scan Complete')
