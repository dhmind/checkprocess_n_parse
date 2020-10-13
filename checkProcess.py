from psutil import process_iter
from subprocess import check_output
import psutil

def getPid(name):
    return int(check_output(["pidof","-s",name]))

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
