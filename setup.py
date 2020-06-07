#!/usr/bin/python3

# File name   : setup.py
# Author      : David Metcalf
# Date        : 6/7/2020

import os
import time

def main():
    try:
        if os.name == 'nt':
            curpath = os.path.realpath(__file__)
            thisPath = "/" + os.path.dirname(curpath)
        
            #print("Current path: " + curpath)
            #print("This path: " + thisPath)
    
            print("We have detected that you are using a windows baised system.")
            print("We will now try and install dependancy libraries for a Windows baised system.")

            os.system("pip3 install -U pip \n pip3 install --upgrade luma.oled \n pip3 install adafruit-pca9685 \n pip3 install rpi_ws281x \n pip3 install mpu6050-raspberrypi \n pip3 install numpy \n pip3 install imutils \n pip3 install zmq \n pip3 install pybase64 \n pip3 install psutil \n pip3 install opencv-contrib-python==3.4.3.18")
            print("We are now finished installing dependancy libraries.")
    except:
        pass

        
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        if os.name != 'nt':
            curpath = os.path.realpath(__file__)
            thisPath = "/" + os.path.dirname(curpath)
            
            #print("Current path: " + curpath)
            
            print("We have detected that you are using a non windows baised system.")
            print("We will try and install dependancy libraries for a linux basied system instead.")
        
            def replace_num(file,initial,new_num):
                newline=""
                str_num=str(new_num)
                with open(file,"r") as f:
                    for line in f.readlines():
                        if(line.find(initial) == 0):
                            line = (str_num+'\n')
                            newline += line
                with open(file,"w") as f:
                    f.writelines(newline)
            
            for x in range(1,4):
                if os.system("sudo apt-get update") == 0:
                    break
        
            os.system("sudo apt-get purge -y wolfram-engine")
            os.system("sudo apt-get purge -y libreoffice*")
            os.system("sudo apt-get -y clean")
            os.system("sudo apt-get -y autoremove")

            for x in range(1,4):
                if os.system("sudo pip3 install -U pip") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo apt-get install -y vlc") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo -H pip3 install --upgrade luma.oled") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo apt-get install -y i2c-tools") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo pip3 install adafruit-pca9685") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo pip3 install rpi_ws281x") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo apt-get install -y python3-smbus") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo pip3 install mpu6050-raspberrypi") == 0:
                    break
            try:
                replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
            except:
                print('try again')
            for x in range(1,4):
                if os.system("sudo pip3 install numpy") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo pip3 install opencv-contrib-python==3.4.3.18") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo apt-get -y install libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo pip3 install imutils zmq pybase64 psutil") == 0:
                    break
            for x in range(1,4):
                if os.system("sudo git clone https://github.com/oblique/create_ap") == 0:
                    break
            try:
                os.system("cd " + thisPath + "/create_ap && sudo make install")
            except:
                pass
            try:
                os.system("cd //home/pi/create_ap && sudo make install")
            except:
                pass
            for x in range(1,4):
                if os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
                    break
            try:
                os.system("sudo touch //home/pi/wpa_supplicant.conf")
                with open("//home/pi/wpa_supplicant.conf","w") as file_to_write:
                    file_to_write.write("country=Us \n update_config=1 \n ctrl_interface=/var/run/wpa_supplicant \n \n network=( \n scan_ssid=1 \n ssid=\"DoomsDay Robots\" \n psk=\"PuppetsforGod198519772009!\" \n }")
            except:
                pass
            
            os.system('sudo chmod 777 //home/pi/wpa_supplicant.conf')

            try:
                os.system('sudo touch //home/pi/ssh')
            except:
                pass

            os.system('sudo chmod 777 //home/pi/ssh')

            try:
                os.system('sudo touch //home/pi/startup.sh')
                with open("//home/pi/startup.sh",'w') as file_to_write:
                    file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/server.py")
            except:
                pass

            os.system('sudo chmod 777 //home/pi/startup.sh')

            replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')

            #fix conflict with onboard Raspberry Pi audio
            try:
                os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
                with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
                    file_to_write.write("blacklist snd_bcm2835")
            except:
                pass
            
            print("We are now finished installing dependancy libraries.")
            print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
            print('restarting...')
            os.system("sudo reboot")
            
    except:
        pass

if __name__ == '__main__':
    main()

