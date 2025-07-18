#Import modules
import tkinter as tk
from tkinter import *
import tkdial as td
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#Constants
checks=["BAT","CHG"]
#max length of buffer
length=45
write=0
colour_code=False
buffer=[]
loaded_data=[]


#Sets up GUI root windows
root = tk.Tk()
root2 =tk.Toplevel()
root_file = tk.Toplevel()
root_file.title('Tkinter Open File Dialog')
root_file.geometry('200x100+400+850')

root.geometry("400x400+0+0")
root.title("Variables")
root2.geometry("800x800+400+0")
root2.title("Raw Output")

root_comment=tk.Toplevel()
root_comment.geometry("200x100+600+850")
root_comment.title("Comment editor")

#Sets up comment entry button
tk.Label(root_comment, text="Input Comment").grid(row=0)
tk.Label(root_comment, text="Input REGEX").grid(row=1)

comment=tk.Entry(root_comment)
regex=tk.Entry(root_comment)

comment.grid(row=0, column=1)
regex.grid(row=1, column=1)

selected=()
#Sets up save to listbox button
def save_list():
    global selected
    global list_comment
    global list_regex
    global mylist
    global buffer
    selected=mylist.curselection()


    if len(selected)>0:
        prev_data=mylist.get(selected[0],selected[0])
        prev_data=prev_data[0]
        prev_data=prev_data.rstrip("\n")
        list_comment=comment.get()
        list_regex=regex.get()
        inserted_data=(prev_data+"#"+list_comment+"##"+list_regex+"\n")
        mylist.insert(selected[0],inserted_data)
        mylist.delete(selected[0]+1)
        mylist.itemconfigure(selected,foreground="red")
        buffer[selected[0]]=inserted_data


tk.Button(root_comment, 
          text='Save', command=save_list).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

#Define function for opening file button
def select_file():
    global state_halt
    if state_halt:
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        f=open(filename,"w")
        for i in buffer:
            f.write(i)
        f.close()

#Define function for loading file button
def load_file():
    global loaded_data
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    f=open(filename,"r")
    loaded_data=f.read()
    f.close()
    loaded_data=loaded_data.splitlines()

# open button
open_button = ttk.Button(
    root_file,
    text='Open a File',
    command=select_file
)
# load button
load_button = ttk.Button(
    root_file,
    text='Load a File',
    command=load_file
)


#Sets variables
name1="var1"
name2="var2"
name3="var3"
name4="var4"
name5="var5"
mode=""
#function for button press to switch mode
def set_BAT():
    global name1,name2,name3,name4,name5,mode
    name1="current: "
    name2="voltage: "
    name3="current set: "
    name4="voltage set: "
    name5="eoc set: "
    mode="BAT"
    #etc.

def set_PLH():
    global name1,name2,name3,name4,name5,mode
    name1="plh1: "
    name2="plh2: "
    name3="plh3: "
    name4="plh4 "
    name5="phl5: "
    mode="TEST"
    #etc.

#Button label
BAT_button = tk.Button(root,
    text="Refresh BAT info.",
    command=set_BAT)

PLH_button = tk.Button(root,
    text="Refresh Placeholder info.",
    command=set_PLH)


#Creates output labels

text_var1= tk.StringVar()
text_var1.set("Hello, World!")
label1 = tk.Label(root, 
textvariable=text_var1)

text_var2= tk.StringVar()
text_var2.set("Hello, World!")
label2 = tk.Label(root, 
textvariable=text_var2)

text_var3= tk.StringVar()
text_var3.set("Hello, World!")
label3 = tk.Label(root, 
textvariable=text_var3)

text_var4= tk.StringVar()
text_var4.set("Hello, World!")
label4 = tk.Label(root, 
textvariable=text_var4)

text_var5= tk.StringVar()
text_var5.set("Hello, World!")
label5 = tk.Label(root, 
textvariable=text_var5)



#Sets up scrollable window
scrollbar = tk.Scrollbar(root2)
scrollbar.pack( side = tk.LEFT, fill=Y )

mylist = tk.Listbox(root2, yscrollcommand = scrollbar.set, width=600, fg="red" )
   
   
mylist.pack( side = tk.LEFT, fill = tk.BOTH)
scrollbar.config( command = mylist.yview )


#Sets up dial (test only)
app = tk.Tk()
app.geometry("400x400+0+450")
app.title("Current set dial")


dial = td.Dial(app,end=200)
dial.grid(padx=10, pady=10)


#Sets up togglable buttons
state_bat=False
state_colour=False
state_hide=False
state_halt=False
#Battery toggle
def toggle_bat():
    global state_bat
    if state_bat:
        state_bat=False
        bat_toggle.config(text="Battery False",fg="black")
    else:
        state_bat=True
        bat_toggle.config(text="Battery True",fg="red")

bat_toggle = tk.Button(root,
    text="Battery False",
    command=toggle_bat)
#Colour coding toggle
def toggle_colour():
    global colour_code
    if colour_code:
        colour_code=False
        colour_toggle.config(text="Colour False",fg="black")
    else:
        colour_code=True
        colour_toggle.config(text="Colour True",fg="red")

colour_toggle = tk.Button(root,
    text="Colour False",
    command=toggle_colour)
#Hide timeouts toggle
def toggle_hide():
    global state_hide
    if state_hide:
        state_hide=False
        hide_toggle.config(text="Hide False",fg="black")
    else:
        state_hide=True
        hide_toggle.config(text="Hide True",fg="red")

hide_toggle = tk.Button(root,
    text="Hide False",
    command=toggle_hide)
#Halt display
def toggle_halt():
    global state_halt
    if state_halt:
        state_halt=False
        halt_toggle.config(text="Halt Display False",fg="black")
    else:
        state_halt=True
        halt_toggle.config(text="Halt Display True",fg="red")

halt_toggle = tk.Button(root,
    text="Halt Display False",
    command=toggle_halt)

for i in range(0,length):
    buffer.append("")
    mylist.insert(i,"")

#MAIN GUI LOOP -----------------------------------------------------------------------------------------------
#Runs to update window
def UI(voltage, current, current_set, voltage_set, eoc_set,plh1,plh2,plh3,plh4,plh5, current_line):
    global app
    global mode
    global write
    global buffer
    global loaded_data

    #Sets each variable dependent on selected mode, and the raw output window
    if mode=="BAT":
        var1=current
        var2=voltage
        var3=current_set
        var4=voltage_set
        var5=eoc_set
    elif mode=="TEST":
        var1=plh1
        var2=plh2
        var3=plh3
        var4=plh4
        var5=plh5
    else:
        var1=0
        var2=0
        var3=0
        var4=0
        var5=0
    global name1,name2,name3,name4,name5
    #Updates labels with new data
    a=(name1,str(var1))
    text_var1.set(a)
    b=(name2,str(var2))
    text_var2.set(b)
    c=(name3,str(var3))
    text_var3.set(c)
    d=(name4,str(var4))
    text_var4.set(d)
    e=(name5,str(var5))
    text_var5.set(e)

    #Updates dial to new data
    try:
        current_set=float(current_set)
    except:
        current_set=0
    dial.set(current_set)

    #Checks for lines containing certain filter and inserts to window

    if state_bat and "BAT" not in checks:
        checks.append("BAT")
        checks.append("CHG")
    elif not state_bat and "BAT" in checks:
        checks.remove("BAT")
        checks.remove("CHG")

    #Detects if any data is present
    if current_line[0]!="":
        if write>=length:
            write=0
        to_write=current_line[0]
        if current_line[2]!="":
            to_write=(to_write+" #"+current_line[2])
        buffer[write]=to_write
        mylist.insert(write,to_write)
        mylist.itemconfigure(write,foreground=current_line[1])
        write+=1
        mylist.delete(write)


    #Checks for cursor select and comment added
    
    


    #Packs each label and updates whole window
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    BAT_button.pack()
    PLH_button.pack()
    bat_toggle.pack()
    colour_toggle.pack()
    hide_toggle.pack()
    halt_toggle.pack()
    open_button.pack()
    load_button.pack()
    root.update()
    root2.update()
    root_comment.update()
    root_file.update()
    return state_bat,colour_code,state_hide,state_halt,loaded_data
