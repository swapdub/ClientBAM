# OMG WE CAN UNIRONICALLY NAME THE BOT OPTIMUS HOLY SHIT, IT'S LATIN FOR "BEST" FUCK YEAH BITCHES
from AutoBot import AutoBot, suffix_file, append_suffix, drop_suffix
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
from tkinter import messagebox as mb
# from tkinter import Listbox

# suffix_file = "companysuffixfile.txt" # i still do not know why we need to complicate it with json

# Make/open a TKinter Window
window = tk.Tk()
window.title("SavAi Cleaner Bot")
window.resizable(0, 0)          # Doesnt allow window resize

# photo = PhotoImage(file = "myfiles\symbol1.png")
# window.iconphoto(False, photo)


# list of used variables
name_col = None
Comp_col = None
user_sel_input_file_path = None
user_sel_output_file_path = None
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
# tk.Label(window, image=photo).grid(row=0, column=1, sticky=W)



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
        name_col = None
        name_col = Name_combo.get()

    Name_combo = ttk.Combobox(window, value = col_options)
    Name_combo.grid(row=name_col_dropdown_row, column = 1)
    Name_combo.bind("<<ComboboxSelected>>", Name_click)


    def Company_click(event):
        global Comp_col
        Comp_col = None
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
        if user_sel_input_file_path:
            run = AutoBot(user_sel_input_file_path)
        
            
            if name_col == None and Comp_col == None and user_sel_input_file_path != None:
                tk.messagebox.showerror(title="Error", message="Neither Name nor Company column is selected.")
            elif name_col == None:
                tk.messagebox.showwarning(title="Error", message="No Name Column selected, Names will not be split")
            elif Comp_col == None:
                tk.messagebox.showwarning(title="Error", message="No Company Column selected, company extensions will not be dropped")
            else:
                pass
                # tk.messagebox.showerror(title="Error", message="Unexpected Error")


            if name_col:
                run.emptycheck()
                run.makenamecols(name_col)
                run.splitnames(name_col)
            else:
                pass

            if Comp_col:
                run.FindReplace(Comp_col)
            else:
                pass

            if user_sel_output_file_path:
                if name_col == None and Comp_col == None:
                    pass
                else:
                    run.to_csv(user_sel_output_file_path, user_sel_input_file_path)
            else:
                tk.messagebox.showerror(title="Error", message="Please select save file location")


        else:
            tk.messagebox.showerror(title="Error", message="No file selected. Please select a file to be cleaned")
        #     #No file selected dialogue box
    except:
        tk.messagebox.showerror(title="Error", message="Unknown Error: Please contact the developers at SavAI")

# Clean Button
tk.Button(text='Clean', command=cleanf).grid(row=select_file_row,column=3)
# Checkbox for new file or same file

tk.mainloop() #Needs this