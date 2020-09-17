# OMG WE CAN UNIRONICALLY NAME THE BOT OPTIMUS HOLY SHIT, IT'S LATIN FOR "BEST" FUCK YEAH BITCHES
import pandas as pd
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








# Let User choose which is Name Column in a dropbox from file to split


# print(clicked.get())
# OptionMenu(window, clicked, *col_options).grid(row=col_name_dropdown_row,
#                                                 column = 1)

tk.Label(window, text="Select Name Column").grid(row=name_col_dropdown_row)


tk.Label(window, text="Select Company Column").grid(row=comp_name_dropdown_row)


# Ask for file path
def filef():
    global name_col
    filef.path = askopenfilename(title = "Select A File", 
                            filetypes=(("csv","*.csv"),("all files","*.*")) )
    
    myLabel = tk.Label(window, text=filef.path).grid(   
                                                    row=select_file_row, 
                                                    column=1   
                                                    )
    col_options = [

    ]
    df2 = pd.read_csv(filef.path)
    for head in df2.columns:
        col_options.append(head)

    clicked = StringVar()
    clicked.set(col_options[0])
    mycombo = ttk.Combobox(window, value = col_options).grid(row=name_col_dropdown_row,
                                            column = 1)

    def on_click(event):
        name_col = clicked.get()
        return name_col


# Pass the ask dialogue box through a button
tk.Button(window, text="Open",command=filef).grid(row=select_file_row,column=2)
tk.Label(window, text="File : ").grid(row=select_file_row)

# Ask for save path
def files():
    files.path = askdirectory(title = "Select Save Location")
    print(files.path)

    mylabel = tk.Label(window, text=files.path).grid(
                                                    row=save_file_row, 
                                                    column=1
                                                    )
# Pass the ask dialogue box through a button
tk.Button(window, text="Save Location",command=files).grid( row=save_file_row,
                                                            column=2, 
                                                            columnspan =2)

tk.Label(window, text="Save Path : ").grid(row=save_file_row)




# Checkbox for new file or same file

tk.mainloop() #Needs this