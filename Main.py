from Datalogger import update
from GUI import UI

#Clears the previous file
f=open("Documents/python temporary/Text.txt","w")
f.write("")
f.close()
b=open("Documents/python temporary/BAT.txt","w")
b.write("")
b.close()



#Recieves data from the board
for i in range(0,100):
    update()
    UI(2)


print("PROCESS FINISHED")

b=open("Documents/python temporary/BAT.txt","r")
BAT=b.read()
BAT=BAT.splitlines()
matching = [s for s in BAT if "battery_calc_power_amount" in s]
data_bat=matching[-1]
print(data_bat)
b.close()
