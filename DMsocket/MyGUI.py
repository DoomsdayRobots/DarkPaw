#!/usr/bin/python
# -*- coding: UTF-8 -*-
# File name    : client.py
# Description  : client
# Author       : David Metcalf
# Date         : 6/9/2020

# bare minimum
import socket
import time
import numpy as np
import tkinter as tk

# optional addons
"""
import cv2
import zmq
import base64
import sys
import threading as thread
"""

tcpClicSock =""


#When this function is called, this client commands the robot to move forward.
def call_forward(event):

    command_forward = 0
    if command_forward == 0:
        #s.send(('forward').encode())
        command_forward = 1


#Call this function to connect with the server
def socket_connect():
    global connected
    
    ip_adr = E1.get()  #Get the IP address from Entry

    if ip_adr != "":
        connected = True

        #ip = ip_adr    #Define ip address
        #SERVER_PORT = 10223   #Define port serial
        #port = 5555    #Define port serial
        #BUFSIZE = 1024         #Define buffer size
        #address = (ip, port)
        #s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Sets the connection values for the socket

    #If no input, then the IP address in entry equils the default IP
    if ip_adr == "":
        connected = False
        
        
        
def loop():
    global connected
    
    """
    global command_forward
    global tcpClicSock
    global root
    global E1
    global connect
    global l_ip_4
    global l_ip_5
    global colour_btn
    global colour_text
    global colour_text
    global Btn14
    global CPU_TEP_lab
    global CPU_USE_lab
    global RAM_lab
    global canvas_ultra
    global var_R
    global var_B
    global var_G
    global Btn_Steady
    global Btn_FindColour
    global Btn_WatchDog
    global Btn_Fun4
    global Btn_Fun5
    global Btn_Fun6
    global Btn_Switch_1
    global Btn_Switch_2
    global Btn_Switch_3
    global Btn_Smooth
    global stat
    """
    
    while True:
        colour_bg="#000000"          #set the background colour
        colour_text="#E1F5FE"        #set the text colour
        colour_btn="#0277BD"         #set the button colour
        colour_line="#01579B"        #set the line colour
        colour_can="#212121"         #set the canvas colour
        colour_oval="#2196F3"        #set the oval colour
        colour_target="#FF6D00"      #set the target colour
        colour_entry_fg="#eceff1"    #set the label entry forground colour
        colour_entry_bg="#37474F"    #set the label background colour

        tk_w = 565                  #Main window width
        tk_h = 510                  #Main window height
        
        #convert these integers to a string that the tk will accept
        geostr = str(tk_w) + "x" + str(tk_h) 
        
        root = tk.Tk()              #defines the main window named root
        root.title("Dark Stalker")  #main window title
        root.geometry(geostr)       #main window size
        root.config(bg=colour_bg)    #Main window colour
            
        #lets make some labels...
        l_ip_5=tk.Label(root,width=10,text="IP Address",fg=colour_text,bg=colour_btn)
        E1 = tk.Entry(root,show=None,width=16,bg=colour_entry_bg,fg=colour_entry_fg)

        #lets place the labels acordingly
        l_ip_5.place(x=tk_w/2.85,y=tk_h/8)           #Define a Label and put it in position
        E1.place(x=tk_w/2,y=tk_h/8)    #Define a data entry label and put it in position



	#lets make some buttons...
        Btn0 = tk.Button(root,width=8,text="Forward",fg=colour_text,bg=colour_btn,relief="ridge")

        #lets place the buttons acordingly
        Btn0.place(x=tk_w/2.25,y=tk_h/3)



        #Logicly we should have some kind of logic for those buttons.
        Btn0.bind("<ButtonPress-1>", call_forward)

        #update the sockets
        root.bind('<Return>', socket_connect)

        #finally its time to draw everything
        canvas_cover=tk.Canvas(root,bg=colour_bg,height=tk_h,width=tk_w,highlightthickness=0)
        canvas_cover.place(x=30,y=420)

        # Ensure the mainloop runs only once
        if stat == 0:
            root.mainloop()  # Run the mainloop()
            stat = 1           # Change the value to '1' so the mainloop() will not run forever.
        
if __name__ == '__main__':
    try:
        loop()
    except:
        tcpClicSock.close()    # Close the socket or it may not connect with the server again.
        pass
        
