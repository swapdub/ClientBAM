# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd
import re

suffix_file = "potato.json"
#"Auto(responder )Bot" a.k.a. AutoBot
class AutoBot: #Optimus Prime here we come!

    def __init__(self,file_path):   # Asking for variable in initializing hampers none file class functionality
        self.df = pd.read_csv(file_path)
        self.nameloc = self.df.columns.get_loc("Name")  # To Do: not define in init, error if file doesnt have Name column
        try:
            self.base_df = pd.read_csv("cleaned_data.csv") #path of database file
            self.main_df = base_df.drop_duplicates()
        except:
            self.main_df = pd.DataFrame(columns = ['UpdatedAt', 'Name', 'FirstName', 'MiddleName', 'LastName', 'Title',
                'Company Name', 'Website', 'List', 'Intel', 'Contact Location',
                'ContactCity', 'ContactState', 'ContactStateAbbr', 'ContactCountry',
                'ContactCountryAlpha2', 'ContactCountryAlpha3', 'ContactCountryNumeric',
                'Company Location', 'CompanyCity', 'CompanyState', 'CompanyStateAbbr',
                'CompanyCountry', 'CompanyCountryAlpha2', 'CompanyCountryAlpha3',
                'CompanyCountryNumeric', 'CompanyStaffCountRange',
                'CompanyRevenueRange', 'Email1', 'EmValidation1', 'Total AI1', 'Email2',
                'EmValidation2', 'Total AI2', 'ContactPhone1', 'CompanyPhone1',
                'ContactPhone2', 'CompanyPhone2', 'ContactPhone3', 'CompanyPhone3',
                'LinkedInContactURL', 'LinkedInCompanyURL', 'AdvertisingIntelligence',
                'AlexaScore', 'CompanyNews', 'EmployeeReviews', 'GoogleFinance',
                'GoogleResearch', 'JobPostings', 'LocalSportsTeams', 'LocalWeather',
                'News', 'PaidSearchIntelligence', 'PaidSearchKeywordsIntelligence',
                'SearchMarketingIntelligence', 'SecFilings', 'SeoResearch',
                'SimilarWebsites', 'SocialMediaMentions', 'SocialMediaPosts',
                'SocialPosts', 'Tweets', 'WebTechnologies', 'WebsiteAudit',
                'WebsiteAudit2', 'WebsiteGrader', 'Whois', 'Wikipedia', 'YahooFinance'])

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
            self.main_df.append(self.df, ignore_index = True)          #only works as intended if both csv files have the same columns in the same order (I think)
    

    # Send data back to original file to make changes
    def to_csv(self, spath):#, spath = None):
        self.df.to_csv(spath + '/file_name.csv', index=False) # To Do: append date/time to keep unique file name

        output_file_path = "myfiles/user_file"
        file_path = "myfiles/cleaned_data"
        self.main_df.to_csv(output_file_path + '.csv', index=False) #tkinter will allow to pick filepath and file name
        self.main_df.to_csv(file_path + '.csv', index=False)
    
    # Find and replace company names using a set list
    def FindReplace(self):
        with open(suffix_file) as f:
            companysuffixlist = f.read().splitlines()
        
        # Function that returns length of input, needed for sorting
        def myFunc(e):
            return len(e)
        companysuffixlist.sort(reverse=True, key=myFunc)

        for suffix in companysuffixlist:
            self.df["Company Name"] = [re.sub("\ \,?\ ?"+suffix+"\.?$", '', idk) for idk in self.df["Company Name"]] 
            self.df["Company Name"] = [re.sub("\,\ ?"+suffix+"\.?$", '', idk) for idk in self.df["Company Name"]] 
    
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
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
from tkinter import messagebox as mb
# from tkinter import Listbox

# Make/open a TKinter Window
window = tk.Tk()
window.title("SavAi Cleaner Bot")
window.resizable(0, 0)          # Doesnt allow window resize

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

e1 = tk.Entry(window)#.grid(row=0) #.place(x=50, y=15) # Text box on window
e1.grid(row= 1, column= 1)
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
    filef.path = askopenfilename(title = "Select A File", filetypes=(("csv","*.csv"),("all files","*.*")) )
    # myLabel = tk.Label(window, text="").grid(row=10, column=1)
    # myLabel.pack_forget()
    myLabel = tk.Label(window, text=filef.path).grid(row=10, column=1)
    # try:
    # except:
    #     pass
    # mylabel = tk.Label(window, text=filef.path).grid(row=10, column=1)
# Pass the ask dialogue box through a button
tk.Button(window, text="Open",command=filef).grid(row=10,column=2)
tk.Label(window, text="File : ").grid(row=10)

# Ask for save path
def files():
    files.path = askdirectory(title = "Select Save Location")
    print(files.path)
    mylabel = tk.Label(window, text=files.path).grid(row=11, column=1)
# Pass the ask dialogue box through a button
tk.Button(window, text="Save Location",command=files).grid(row=11,column=2, columnspan =2)
tk.Label(window, text="Save Path : ").grid(row=11)


# Clean/Run Autobot
def cleanf():
    try:
        try:
            run = AutoBot(filef.path)
            try:
                run.emptycheck()
                run.makenamecols()
                run.splitnames()
                run.FindReplace()
                run.to_csv(files.path)
            except:
                tk.messagebox.showerror(title="Error", message="Please select save file location.")
        except:
            tk.messagebox.showerror(title="Error", message="No file selected. Please select a file to be cleaned.")
    except:
        #No file selected dialogue box
        tk.messagebox.showerror(title="Error", message="Unknown Error: Please contact the developers at SavAI")
# Clean Button
tk.Button(text='Clean', command=cleanf).grid(row=10,column=3)
# Checkbox for new file or same file

tk.mainloop() #Needs this