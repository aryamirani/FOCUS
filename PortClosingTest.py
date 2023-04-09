import psutil
import socket

# specify the port number you want to close
port = int(input('Enter port to be closed: '))

# find the process using the port
for proc in psutil.process_iter(['pid', 'name']):
    try:
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                print(f"Process {proc.name()} (PID {proc.pid}) is using port {port}")
                proc.terminate()
                print('Process terminated')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass