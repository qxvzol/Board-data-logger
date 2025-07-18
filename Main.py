from Datalogger import update
from GUI import UI

#Clears the previous files
def file_clear():
        files=["BAT","Raw","Text"]
        for i in files:
            file_name=("C:/Users/ollie/Documents/python temporary/"+i+".txt")
            file_name=str(file_name)
            f=open(file_name,"w")
            f.write("")
            f.close()

#Function to search and get data from file
def get_data(data,search_name,search_position):
    matching = [s for s in data if search_name in s]
    try:
        data=matching[-1]
        data=data.split(" ")
        return(data[search_position])
    except:
        return 0
    
#Function to read selected file and split lines
def read_file(f_name):
    file_name=("C:/Users/ollie/Documents/python temporary/"+f_name+".txt")
    file_name=str(file_name)
    f=open(file_name,"r")
    data=f.read()
    f.close()
    data=data.splitlines()
    return data

#Clears files
file_clear()

#RUNNING LOOP ----------------------------------------------------------------------------------------------------------

#Recieves data from the board using update function
#Runs GUI function to update window (currently unused)
i=0
bat=False
colour=False
hide=False
halt=False
loaded_data=[]
while True:
    #Resets file after certain number of runs to prevent file getting too large
    i+=1
    if i>=500:
        #file_clear()
        i=0
    #Runs data logger function   
    x=update(bat,colour,hide,halt,loaded_data)

    #Reads from BAT file to search for specific data pieces relating to battery/charge data
    BAT=read_file("BAT")
    voltage=get_data(BAT,"battery_calc_power_amount",2)
    current=get_data(BAT,"battery_calc_power_amount",5)
    current_set=get_data(BAT,"CHG set_current ",2)
    voltage_set=get_data(BAT,"CHG set voltage ",3)
    eoc_set=get_data(BAT,"CHG set_eoc ",2)

    #Reads from TEST LOG file to search for data
    LOG=read_file("TEST_LOG")
    plh1=get_data(LOG,"test1",2)
    plh2=get_data(LOG,"test2",0)
    plh3=get_data(LOG,"test3",1)
    plh4=get_data(LOG,"test4",4)
    plh5=get_data(LOG,"test5",2)
    #Runs loop to control UI
    bat,colour,hide,halt,loaded_data=UI(voltage,current,current_set,voltage_set,eoc_set,plh1,plh2,plh3,plh4,plh5,x)
