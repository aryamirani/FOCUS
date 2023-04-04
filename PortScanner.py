# Module Import
import threading
import time
from functions import port_scanner

# Formatting Whitelist Ports
WhitelistedPortsFile = open('Whitelisted Ports.txt', 'r')
WhitelistedPortsList = WhitelistedPortsFile.readlines()
FormattedPortsList = []
for WPorts in WhitelistedPortsList:
    FormattedPortsList.append(WPorts.replace("\n", ""))

    # Converting Str List to Int List
    IntPortList = [eval(IntPort) for IntPort in FormattedPortsList]

# Port scanning via multi-thread distribution
start = time.time()  # Function Start Time
for port in range(1, 60000):
    if port in IntPortList:
        continue

    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()

end = time.time()  # Function End Time
print("")
print("")
print("Scan Complete!")
print(f"Time taken for scan: {end - start} Seconds")