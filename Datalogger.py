import time
import serial
import re

#Configures ser to correct port
ser = serial.Serial(
        port='COM3',
        baudrate = 1200000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)


#Function to update file to current information from board
def update():
        f=open("Documents/python temporary/Text.txt","a")
        x=ser.readline()
        x=x.decode(encoding="utf-8")
        if "OnTimeout" in x:
                x=""
        if re.findall("^seq:",x):
                x=""
        f.write(x)
        f.write('\n')
        f.close()

        if re.findall("^BAT|CHG",x):
                        b=open("Documents/python temporary/BAT.txt","a")
                        b.write(x)
                        b.write('\n')
                        b.close()