# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

import pandas as pd
#"Auto(responder )Bot" a.k.a. AutoBot
class AutoBot: #Optimus Prime here we come!
    "shut up swaps"


    def __init__(self,file_path):   # Asking for variable in initializing hampers none file class functionality
        self.df = pd.read_csv(file_path)
        self.nameloc = self.df.columns.get_loc("Name")  # To Do: not define in init, error if file doesnt have Name column


    # Drop if full column/row empty
    def emptycheck(self):
        self.df = self.df.dropna(axis= 'columns', how='all')
        self.df = self.df.dropna(axis= 'index', how='all')


    # Make new columns if they do not exist
    def makenamecols(self):
        try:
            self.df.insert(self.nameloc+1, "FirstName", None)
            self.df.insert(self.nameloc+2, "MiddleName", None)
            self.df.insert(self.nameloc+3, "LastName", None)
        except:
            return
    

    # Split original names into 3 columns and assign them to respective columns
    def splitnames(self):   
        for i in range(len(self.df["Name"])):
            try:
                a, *b, c = self.df.iat[i,self.nameloc].split()
                s = " "
                b = s.join(b)
            except:
                a = self.df.iat[i,self.nameloc]
                b = None
                c = None
            self.df.iat[i,self.nameloc+1] = a
            self.df.iat[i,self.nameloc+2] = b
            self.df.iat[i,self.nameloc+3] = c
    

    # Send data back to original file to make changes
    def to_csv(self):
       self.df.to_csv('file_name.csv', index=False)
    
    # Find and replace company names using a set list
    def FindReplace(self):
        with open("companysuffixfile.txt") as f:
            companysuffixlist = f.read().splitlines()
        
        # Function that returns length of input, needed for sorting
        def myFunc(e):
            return len(e)
        companysuffixlist.sort(reverse=True, key=myFunc)

        for suffix in companysuffixlist:
            self.df["Company Name"] = [re.sub("\ " + suffix + "\.?$", '', idk) for idk in self.df["Company Name"]] 
    

    # Run all functions above, edit original file()
    def fullsplit(self):
        self.makenamecols()
        self.emptycheck()
        self.splitnames()
        self.to_csv()
        
    def CompanySplit(self):
        try:
            self.append_suffix()
            self.FindReplace()
            self.to_csv()
        except:            
            self.FindReplace()
            self.to_csv()

# Create/Append to file with a list of Company Extensions
def append_suffix(suffix):   #I propose this should be a seperate function, not in this class
    # Open file in read n write mode
    with open("companysuffixfile.txt", "a+") as file_object:
        lines = file_object.read().splitlines()

        # Check if value exists, if not, then append to file
        if suffix not in lines:
            file_object.seek(0)             # Move read cursor to the start of file.
            data = file_object.read(10)     # If file is not empty then append '\n'
            if len(data) > 0:
                file_object.write("\n")     # Append text at the end of file
            file_object.write(suffix)


# Create/Append to file with a list of Company Extensions
def drop_suffix(dropsuffix):   #I propose this should be a seperate function, not in this class
    # Open file in read n write mode
    with open("companysuffixfile.txt") as file_object:
        lines = file_object.read().splitlines()
    terms = len(lines)
    lines.pop(terms - dropsuffix - 1)

    # Empty file to prevent doubling
    open("companysuffixfile.txt", "w").close()

    # Check if value exists, if not, then append to file
    with open("companysuffixfile.txt", "a+") as file_object:
        for ex in ext:
            file_object.seek(0)             # Move read cursor to the start of file.
            data = file_object.read(10)     # If file is not empty then append '\n'
            if len(data) > 0:
                file_object.write("\n")     # Append text at the end of file
            file_object.write(ex)

##OMG WE CAN UNIRONICALLY NAME THE BOT OPTIMUS HOLY SHIT, IT'S LATIN FOR "BEST" FUCK YEAH BITCHES

# import pandas as pd
# from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile 
from tkinter import messagebox as mb
# from tkinter import Listbox

# Make/open a TKinter Window
window = tk.Tk()
window.title("SavAi Cleaner Bot")


# Prettify!!
# fontStyle = tk.font(family="Lucida Grande", size=20)
tk.Label(window, text="SavAi",
		 fg = "black",
		#  bg = "yellow",
		 font = "Verdana 20 bold").grid(row=0, column=1)

## 
# def sholist():
listbox = tk.Listbox(window)#, selectmode=SINGLE)
listbox.grid(row=3, column=1)

with open("companysuffixfile.txt") as f:
    ext = f.read().splitlines()

    for l in ext:
        listbox.insert(-1, l)


# # Input button for keyword
def append():
    listbox.delete(0, -1)
    if not e1.get().rstrip(" "):
        print ("empty")
        pass
    else:
        append_suffix(e1.get().rstrip(" "))
        listbox.insert(-1, e1.get().rstrip(" "))
        print ("not empty")

e1 = tk.Entry(window)#.grid(row=0) #.place(x=50, y=15) # Text box on window
e1.grid(row=1,column=1)
# lab = tk.Label(window, width=15, text='Company Extension', anchor='w')
tk.Label(window, text="Company Extension").grid(row=1)
# tk.Label(window, text="Last Name").grid(row=1)
tk.Button(window, text="Add",command=append).grid(row=1,column=2)


# Drop from current list of keywords
def exlist():
    sel = listbox.curselection()
    print(sel)
    drop_suffix(sel[0])
    listbox.delete(tk.ACTIVE)
    
tk.Button(window, text="Delete",command=exlist).grid(row=1,column=3)
    

# Ask for file path
def filef():
    filef.path = askopenfilename()
# # Pass the ask dialogue box through a button
tk.Button(window, text="Open",command=filef).grid(row=10,column=2)

# Ask for save path
def files():
    files.path = asksaveasfile()
# # Pass the ask dialogue box through a button
tk.Button(window, text="Save Location",command=files).grid(row=11,column=1)


# Clean/Run Autobot
def cleanf():
    if var1.get()== 1:      # Ideally this will be inside try fn
        print("Hooray!!")
    else:
        try:
            run = AutoBot(filef.path)
            run.emptycheck()
            run.makenamecols()
            run.splitnames()
            run.to_csv()
        except:
            #No file selected dialogue box
            tk.messagebox.showerror(title="Error", message="Error: File not selected")
# Clean Button
tk.Button(text='Clean', command=cleanf).grid(row=10,column=3)

# Checkbox for new file or same file
var1 = tk.IntVar()
tk.Checkbutton(window, text="Update Same File", variable=var1).grid(row=10, column=1)#, sticky=W)
# var2 = tk.IntVar()
# tk.Checkbutton(window, text="female", variable=var2).grid(row=1)#, sticky=W)


tk.mainloop() #Needs this