# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import pandas as pd
import re
import os

suffix_file = "companysuffixfile.txt" # i still do not know why we need to complicate it with json
#"Auto(responder )Bot" a.k.a. AutoBot
class AutoBot: #Optimus Prime here we come!

    def __init__(self,file_path):   # Asking for variable in initializing hampers none file class functionality
        self.df = pd.read_csv(file_path)
        
       
    # Drop if full column/row empty
    def emptycheck(self):
        self.df = self.df.dropna(axis= 'columns', how='all')
        self.df = self.df.dropna(axis= 'index', how='all')


    # Make new columns if they do not exist
    def makenamecols(self, namecol):
        self.nameloc = self.df.columns.get_loc(namecol)  # To Do: not define in init, error if file doesnt have Name column
        try:
            self.df.insert(self.nameloc+1, "FirstName", None)
            self.df.insert(self.nameloc+2, "MiddleName", None)
            self.df.insert(self.nameloc+3, "LastName", None)
        except:
            return
    

    # Split original names into 3 columns and assign them to respective columns
    def splitnames(self, namecol):
        self.nameloc = self.df.columns.get_loc(namecol)  # To Do: not define in init, error if file doesnt have Name column
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
