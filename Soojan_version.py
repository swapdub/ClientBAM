import pandas as pd
import json

# @soojan: issue was self.main_df = self.main_df.append, sent it to inf loop

file_path1 = "D:\SavAi\ClientBAM\seamless2@clientbam.com-contacts-2020-06-30-08-03-23-cleaned - Copy.csv"
with open("potato.json") as f:  #how to fix path of main file?
    suffix_list = json.loads(f.read())
print(suffix_list)

class AutoBot: #Optimus Prime here we come!    ##class AutoBot():
    "autobot"

    def __init__(self,file_path):   # Asking for variable in initializing hampers none file class functionality
        self.df = pd.read_csv(file_path)
        self.nameloc = self.df.columns.get_loc("Name")  #Do not define in init, error if file doesnt have Name column

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


    # Find and replace company names using a set list
    def FindReplace(self):
        for suffix in suffix_list:
            c = self.df.columns.get_loc("Company Name")  #need to create dialog box to ask person what the name of the column with company names is
            for i in range(len(self.df)):
                self.df.iat[i,c] = self.df.iat[i,c].rstrip("\ \,?\ ?{}\.?|\,\ ?{}\.?".format(suffix,suffix))

    # Run all functions above, edit original file()
    # Dont link functions inside a class, do this outside and call individual functions to execute task : Shetty
    def fullsplit(self):
        # self.emptycheck()
        self.makenamecols()
        self.splitnames()
        print(self.main_df)
        self.FindReplace()
        self.df.drop_duplicates()

    def save_to_csv(self):
        output_file_path = "myfiles/user_file"
        file_path = "myfiles/cleaned_data"
        self.main_df.to_csv(output_file_path +'.csv', index=False) #tkinter will allow to pick filepath and file name
        self.main_df.to_csv(file_path +'.csv', index=False) #tkinter will allow to pick filepath and file name


def append_to_suffix(new_suffix):
    with open("potato.json") as f:  #how to fix path of main file?
        suffix_list = json.loads(f.read())
    suffix_set = set(suffix_list)
    suffix_set.add(new_suffix)
    suffix_list = list(suffix_set)
    out_file = open("potato.json", "w")      
    json.dump(suffix_list, out_file, indent = 6)      
    out_file.close()

outpath = "D:\SavAi\ClientBAM\soojan"
test = AutoBot(file_path1)
with open("companysuffixfile.txt", "r") as tfile:
    sufflist = tfile.read().splitlines()

for n in sufflist:
    append_to_suffix(n)

test.fullsplit()
test.save_to_csv()