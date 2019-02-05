import datetime
import os
import subprocess as sp
import threading
import time
import Ip_Scaner

# Class_funcshen
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def Clear():
    sr = '\033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F'
    print(sr)

def Title():
    Clear()
    status, result = sp.getstatusoutput("pwd")
    f = open(result + "/Logo/AMA_S.txt", "r")
    next = f.read()
    while next != "":
        print(bcolors.FAIL + next + bcolors.ENDC)
        next = f.read()

def Print():
    arryAct = []
    arryDeAct = []
    arryLaAct = []
    Title()
    next = ''
    try:
        status, result = sp.getstatusoutput("pwd")
        f = open(result + "/Ip.txt", "r")
        next = f.readline()
    except:
        next = ''
    for i in range(9):
        ip = ''
        tm = ''
        if next != '':
            ip = next.split(' ')[0]
            ip = ip[0:15]
            tm = next.split(' ')[1]
            tm = tm[0:-2]
            try:
                next = f.readline()
            except:
                ip = ip
        arryAct.append(ip)
        print('\033[91m    ▐\033[0m' + ip.center(18,' ') + tm.center(18,' ') + '\033[91m▐                                 ▐\033[0m')
    print('\033[91m    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\033[0m')

# Print()
def Ip_Scan():
    while True:
        # status, result = sp.getstatusoutput("pwd")
        # os.system(result + '/Ip_Scaner.py')
        a = Ip_Scaner
        a.Serch('172.20.6.0', '172.20.7.255')
        # Ip_Scaner.Serch('192.168.1.0', '192.168.1.255')
        time.sleep(15)

processThread = threading.Thread(target = Ip_Scan)
processThread.start()



while True:
    Print()
    time.sleep(5)