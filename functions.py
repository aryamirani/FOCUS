import platform, os, socket, requests, json, psutil

#Variable Assignment
Platform = platform.system()


def clear():
  if Platform == 'Linux':
    os.system("clear")

  elif Platform == 'Windows':
    os.system("cls")


OpenPorts = []
target = "127.0.0.1"
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"{port}")
        OpenPorts.append(port)
    except:
        pass
    


def PortCloser(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == port:
                    print(f"Process {proc.name()} (PID {proc.pid}) is using port {port}")
                    proc.terminate()
                    print('Process terminated')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
