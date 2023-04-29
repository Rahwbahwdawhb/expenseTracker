import csvParser
import categoryTagHandler

categoryDict=categoryTagHandler.readCategoryDict('test')
categoryTagHandler.appendTag(categoryDict,[('ICA','Food'),('COOP','Food'),('WILLYS','Food'),('SATS','Bills'),('Swish','Fun')])
categoryTagHandler.saveCategoryDict(categoryDict,'test')

csvP=csvParser.csvParser(categoryDict)
expenses=csvP.getExpenses('testfile.csv')
yC=csvP.tidyExpenses(expenses)
print(yC)