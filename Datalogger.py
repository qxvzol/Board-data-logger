import serial
import re

hide_timeout=False

#Configures ser to correct port
ser = serial.Serial(
        port='COM3',
        baudrate = 1200000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#Function to write information to file
def file_w(data,f_name):
        file_name=("C:/Users/ollie/Documents/python temporary/"+f_name+".txt")
        file_name=str(file_name)
        f=open(file_name,"a")
        f.write(data)
        f.close()

def sort_file(data,f_name,filter):
        if filter in data:
                file_w(data,f_name)

def search_regex(comment,regex,current_line):
        if re.findall(regex,current_line):
                return (current_line+" #"+comment)
        else:
                return ""
        
def add_filter(toggle,filter,filters_list,comment,comment_list):
        if toggle and (filter not in filters_list):
                filters_list.append(filter)
        elif not toggle and (filter in filters_list):
                filters_list.remove(filter)
        if toggle and (comment not in comment_list):
                comment_list.append(comment)
        elif not toggle and (comment in comment_list):
                comment_list.remove(comment)
        return filters_list,comment_list

comment=[]
regex=[]
filters=[]
comment_list=[]
#UPDATE FUNCTION ----------------------------------------------------------------
#Function to update file to current information from board
def update(bat,colour,hide_timeout,halt,loaded_data):
        global comment,regex,filters,comment_list
        #Opens files and converts data to readable format
        try:
                x=ser.readline()
                x=x.decode(encoding="utf-8")
        except:
                x=""
        #Writes data for raw output
        file_w(x,"Raw")

        #Removes data for timeouts or if recording has stopped
        if ("OnTimeout" in x) and hide_timeout:
                x=""
        elif halt:
                x=""

        #Sorts data into relevant files
        sort_file(x,"BAT","BAT")
        sort_file(x,"BAT","CHG")
        #Finds regex from loaded data
        comment=""
        (filters,comment_list)=add_filter(bat,"^BAT",filters,comment,comment_list)
        (filters,comment_list)=add_filter(bat,"^CHG",filters,comment,comment_list)

        present=False
        for i in loaded_data:
                present=False
                comment=re.findall("(?<=#)(.{1,})(?=##)",i)
                regex=re.findall("(?<=##)(.{1,})",i)
                try:
                    comment=comment[0]
                    regex=regex[0]
                    present=True
                    (filters,comment_list)=add_filter(present,regex,filters,comment,comment_list)
                except:
                    comment=""
                    regex=""



        if len(filters)>0:
                any_filter=True
        else:
                any_filter=False
        found=False
        if x!="":
                if any_filter:
                        if colour:
                                for i in filters:
                                        if re.findall(i,x):
                                                position=filters.index(i)
                                                comment=comment_list[position]
                                                return_data=[x,"red",comment]
                                                found=True
                                        elif not found:
                                                return_data=[x,"black",""]
                        else:
                                for i in filters:
                                        if re.findall(i,x):
                                                position=filters.index(i)
                                                comment=comment_list[position]
                                                return_data=[x,"red",comment]
                                                found=True
                                        elif not found:
                                                return_data=["","black",""]
                else:
                        return_data=[x,"black",""]

                return(return_data)
        else:
                return["","black",""]
