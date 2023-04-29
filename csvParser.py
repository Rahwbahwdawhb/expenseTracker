from csv import reader
from copy import deepcopy

# categoryDict=dict()
# categoryDict['ICA']='Food'
# categoryDict['COOP']='Food'
# categoryDict['WILLYS']='Food'
# categoryDict['SATS']='Bills'
# categoryDict['Swish']='Fun'
# expCategories=['Food','Bills','Clothes','Food suppl.','Fun','Misc']

class csvParser:
    def __init__(self,categoryDict):
        self.categoryDict=categoryDict        
        expCategories=set()
        for _,category in self.categoryDict.items():
            expCategories.add(category)
        expCategories.add('Misc')
        categoryContainer=dict()
        for cat in expCategories:
            categoryContainer[cat]=[]
        self.monthContainer=dict()
        for iter in range(12):
            if iter<9:
                iterStr='0'+str(iter+1)
            else:
                iterStr=str(iter+1)
            self.monthContainer[iterStr]=deepcopy(categoryContainer)

    def getExpenses(self,fileName):
        #reads Nordea .csv-file and groups expense amounts, their descriptions and dates as tuples
        #returns all such tuples from the file in a list
        expenses=[]
        with open(fileName) as f:
            csvContents=reader(f,delimiter=';')
            for row in csvContents:
                if row[1].find('-')!=-1: #check that the transaction is negative=expense
                    expenses.append((row[0].replace('-',''),row[1][1:],row[5])) #extract amount and description of transaction
        return expenses
    def tidyExpenses(self,expIn,yearContainer=None):
        #sort expenses into years, months and categories in nested dictionaries
        expIn.sort(key=lambda x: x[0],reverse=False) #initial sorting so earliest date appears first
        if yearContainer is None: #initialize year container if none is provided as input
            noInitialContainer=True
            yearContainer=dict()
            yearContainer[expIn[0][0][0:-4]]=deepcopy(self.monthContainer)
        else:
            noInitialContainer=False
        for exp in expIn:
            loopYear=expIn[0][0][0:-4]
            if loopYear not in yearContainer.keys(): #create nested month dictionary if the year is not already in the year container
                yearContainer[loopYear]=deepcopy(self.monthContainer)
            for word in exp[2].split(' '): #split description string into separate words and check if any of them in the category dictionary
                if word in self.categoryDict.keys():
                    loopCategory=self.categoryDict[word]
                    break
                else:
                    loopCategory='Misc'
            yearContainer[loopYear][exp[0][-4:-2]][loopCategory].append(exp) #append expense to suitable category in innermost relevant nested dictionary
        if noInitialContainer: #return year container if none was provided as input
            return yearContainer
        
    
# csvP=csvParser(categoryDict)
# expenses=csvP.getExpenses('testfile.csv')
# yC=csvP.tidyExpenses(expenses)
# # print(expenses)
# for y in yC.keys():
#     print(y)
#     for m in yC[y].keys():
#         if yC[y][m]!=[]:
#             print(yC[y][m])