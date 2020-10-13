from psutil import process_iter
import psutil

def getPid(name):
    for p in process_iter():
        if p.name() == "nginx":
            print("OK: nginx pid founded")
            return p.pid

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if checkIfProcessRunning('nginx'):
    print("OK: nginx is running")
else:
    print("WARNING: nginx is not running")
    
r = getPid("nginx")

for proc in process_iter():
    for conns in proc.connections(kind='inet'):
        if conns.laddr.pid == r and  conns.laddr.port == 80:
            print("OK: nginx is running on 80 port")
        if conns.laddr.pid == r and conns.laddr.port != 80:
            print("WARNING: nginx not at 80's port")
