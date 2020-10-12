import psutil
import socket

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
    
if checkIfProcessRunning('Firefox'):
    print('OK: nginx is running')
else:
    print('Warning: nginx is down')

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return "Connetion to 80 port ESTABLISHED"
   except:
      return "Port closed"

print(isOpen('127.0.0.1',80))
