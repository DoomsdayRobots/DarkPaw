#!/usr/bin/python3
# File name   : setup.py
# Author      : David Metcalf
# Date        : 2020/5/30

import os
import time

curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

try:
	os.system('sudo touch //home/pi/startup.sh')
	with open("//home/pi/startup.sh",'w') as file_to_write:
		#file_to_write.write("#!/bin/sh \n sudo python3 " + thisPath + "/server/server.py") # original
                """
                screen bash \n
                cd DarkPaw/server/ \n
                sudo python3 server.py \n
                key CTRL
                
                
                """
		file_to_write.write(" ")
		
except:
	pass

os.system('sudo chmod 777 //home/pi/startup.sh')

try: #fix conflict with onboard Raspberry Pi audio
	os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
	with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
		file_to_write.write("blacklist snd_bcm2835")
except:
	pass

print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")
