# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd
import re
import os

suffix_file = "companysuffixfile.txt" # i still do not know why we need to complicate it with json
#"Auto(responder )Bot" a.k.a. AutoBot
class AutoBot: #Optimus Prime here we come!

    def __init__(self,file_path, namecol):   # Asking for variable in initializing hampers none file class functionality
        self.df = pd.read_csv(file_path)
        self.nameloc = self.df.columns.get_loc(namecol)  # To Do: not define in init, error if file doesnt have Name column
       
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
            # self.main_df.append(self.df, ignore_index = True)          #only works as intended if both csv files have the same columns in the same order (I think)
    

    # Send data back to original file to make changes
    def to_csv(self, spath,user_file):#, spath = None):
        file_name = os.path.basename(user_file)
        s1 = "/cleaned - "
        self.df.to_csv(spath + s1 + file_name, index=False) # To Do: append date/time to keep unique file name

        # output_file_path = "myfiles/user_file"
        # file_path = "myfiles/cleaned_data"
        # self.main_df.to_csv(output_file_path + '.csv', index=False) #tkinter will allow to pick filepath and file name
        # self.main_df.to_csv(file_path + '.csv', index=False)
    
    # Find and replace company names using a set list
    def FindReplace(self, companycol):
        with open(suffix_file) as f:
            companysuffixlist = f.read().splitlines()
        
        # Function that returns length of input, needed for sorting
        def myFunc(e):
            return len(e)
        companysuffixlist.sort(reverse=True, key=myFunc)

        for suffix in companysuffixlist:
            self.df[companycol] = [re.sub("\ \,?\ ?"+suffix+"\.?$", '', idk) for idk in self.df[companycol]] 
            self.df[companycol] = [re.sub("\,\ ?"+suffix+"\.?$", '', idk) for idk in self.df[companycol]] 
    
    # "\ \,?\ ?"x "\.?" | "\,\ ?" x "\.?"
    # "\ " + suffix + "\.?$"

    # Run all functions above, edit original file()
    def fullsplit(self):
        self.emptycheck()
        self.makenamecols()
        self.splitnames()
        self.to_csv()
        
    def CompanySplit(self):
        self.FindReplace()
        self.to_csv()

# Create/Append to file with a list of Company Extensions
def append_suffix(suffix):   #I propose this should be a seperate function, not in this class
    # Open file in read n write mode
    with open(suffix_file, "a+") as file_object:
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
    with open(suffix_file) as file_object:
        lines = file_object.read().splitlines()
        terms = len(lines)
        lines.pop(terms - dropsuffix - 1)

    # Empty file to prevent doubling
    open(suffix_file, "w").close()

    # Check if value exists, if not, then append to file
    with open(suffix_file, "a+") as file_object:
        for ex in lines:
            file_object.seek(0)             # Move read cursor to the start of file.
            data = file_object.read(10)     # If file is not empty then append '\n'
            if len(data) > 0:
                file_object.write("\n")     # Append text at the end of file
            file_object.write(ex)


# OMG WE CAN UNIRONICALLY NAME THE BOT OPTIMUS HOLY SHIT, IT'S LATIN FOR "BEST" FUCK YEAH BITCHES
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
from tkinter import messagebox as mb
# from tkinter import Listbox

# Make/open a TKinter Window
window = tk.Tk()
window.title("SavAi Cleaner Bot")
window.resizable(0, 0)          # Doesnt allow window resize


# list of used variables
name_col_dropdown_row = 10
comp_name_dropdown_row = 11
select_file_row = 12
save_file_row = select_file_row + 1



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

try:
    with open(suffix_file, "r+") as f:
        ext = f.read().splitlines()
        for l in ext:
            listbox.insert(-1, l)
except:    
    open(suffix_file, "a+").close()



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

e1 = tk.Entry(window) # Text box on window
e1.grid(row= 1, column= 1)
tk.Label(window, text="Company Extension").grid(row=1)
tk.Button(window, text="Add",command=append).grid(row=1,column=2)

# Drop from current list of keywords
def exlist():
    sel = listbox.curselection()
    print(sel)
    drop_suffix(sel[0])
    listbox.delete(tk.ACTIVE)
    
tk.Button(window, text="Delete",command=exlist).grid(row=1,column=3)

# Let User choose which is Name Column in a dropbox from file to split
tk.Label(window, text="Name Column :").grid(row=name_col_dropdown_row, sticky=W)

tk.Label(window, text="Company Column :", anchor="w").grid(row=comp_name_dropdown_row, sticky=W)


# Ask for file path
def filef():
    global user_sel_input_file_path
    user_sel_input_file_path = askopenfilename(title = "Select A File", 
                            filetypes=(("csv","*.csv"),("all files","*.*")) )
    
    myLabel = tk.Label(window, text=user_sel_input_file_path).grid(   
                                                    row=select_file_row, 
                                                    column=1   
                                                    )
    col_options = [

    ]
    df2 = pd.read_csv(user_sel_input_file_path)

    for head in df2.columns:
        col_options.append(head)



    def Name_click(event):
        global name_col
        name_col = Name_combo.get()

    Name_combo = ttk.Combobox(window, value = col_options)
    Name_combo.grid(row=name_col_dropdown_row, column = 1)
    Name_combo.bind("<<ComboboxSelected>>", Name_click)


    def Company_click(event):
        global Comp_col
        Comp_col = Company_box.get()

    Company_box = ttk.Combobox(window, value = col_options)
    Company_box.grid(row=comp_name_dropdown_row, column = 1)
    # Company_box.current(0)
    Company_box.bind("<<ComboboxSelected>>", Company_click)


# Pass the ask dialogue box through a button
tk.Button(window, text="Open",command=filef).grid(row=select_file_row, column=2)
tk.Label(window, text="File : ").grid(row=select_file_row, sticky=W)

# Ask for save path
def files():
    global user_sel_output_file_path
    user_sel_output_file_path = askdirectory(title = "Select Save Location")
    print(user_sel_output_file_path)

    mylabel = tk.Label(window, text=user_sel_output_file_path).grid(
                                                    row=save_file_row, 
                                                    column=1
                                                    )
# Pass the ask dialogue box through a button
tk.Button(window, text="Save Location",command=files).grid( row=save_file_row,
                                                            column=2, 
                                                            columnspan =2)

tk.Label(window, text="Save Path : ").grid(row=save_file_row, sticky=W)


# Clean/Run Autobot
def cleanf():
    try:
        try:
            run = AutoBot(user_sel_input_file_path, name_col)
            try:
                run.emptycheck()
                run.makenamecols()
                run.splitnames()
                try:
                    run.FindReplace(Comp_col)
                    try:
                        run.to_csv(user_sel_output_file_path, user_sel_input_file_path)
                    except:
                        tk.messagebox.showerror(title="Error", message="Please select save file location")
                except:
                    tk.messagebox.showerror(title="Error", message="Select Company Name column from drop down")
            except:
                tk.messagebox.showerror(title="Error", message="Unexpected error")
        except:
            tk.messagebox.showerror(title="Error", message="No file selected. Please select a file to be cleaned")
    except:
        #No file selected dialogue box
        tk.messagebox.showerror(title="Error", message="Unknown Error: Please contact the developers at SavAI")
# Clean Button
tk.Button(text='Clean', command=cleanf).grid(row=select_file_row,column=3)
# Checkbox for new file or same file

tk.mainloop() #Needs this