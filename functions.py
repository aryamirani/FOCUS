#Module Import
import platform
import os
import socket

#Variable Assignment
Platform = platform.system()

#Function 1
def clear():
  if Platform == 'Linux':
    os.system("clear")

  elif Platform == 'Windows':
    os.system("cls")

#Function 2
target = "127.0.0.1"
OpenPorts = []
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"Port {port} is open")
        OpenPorts.append(port)
    except:
        pass