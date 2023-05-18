import csvParser
import categoryTagHandler
import gui
from PyQt6.QtWidgets import QApplication
from numpy import array as npArr
from numpy import linspace, amax
from matplotlib.cm import inferno

categoryDict=categoryTagHandler.readCategoryDict('test')
categoryTagHandler.appendTag(categoryDict,[('ICA','Food'),('COOP','Food'),('WILLYS','Food'),('SATS','Bills'),('Swish','Fun')])
categoryTagHandler.saveCategoryDict(categoryDict,'test')

csvP=csvParser.csvParser(categoryDict)
expenses=csvP.getExpenses('testfile.csv')
yC=csvP.tidyExpenses(expenses)
# print(yC)

months=[]
for iter in range(12):
    if iter<9:
        iterStr='0'+str(iter+1)
    else:
        iterStr=str(iter+1)
    months.append(iterStr)

cats=set(csvP.categoryDict.values())

plotColors=[]
refPoints=linspace(0,255,len(cats))

yC_yrs=list(yC.keys())
x_entries=[]
y_entriesTot=[]
y_entriesCat=[]
for i,_ in enumerate(cats):
    y_entriesCat.append([])
    r,g,b,_=inferno(int(refPoints[i]))
    plotColors.append((int(r*255),int(g*255),int(b*255)))
for yr in yC_yrs:
    for m in months:
        x_entries.append(float(yr+m))
        m_sum=0
        for i,cat in enumerate(cats):
            catSum=0
            for entry in yC[yr][m][cat]:
                catSum+=float(entry[1].replace(',','.'))
            y_entriesCat[i].append(catSum)
            m_sum+=catSum
        y_entriesTot.append(m_sum)

print(y_entriesCat)
print(y_entriesTot)
x_entries=npArr(x_entries)
app=QApplication([])
GUI=gui.trackerGUI()
for i,_ in enumerate(cats):
    yIter=y_entriesCat[i]
    if amax(yIter)>0:
        GUI.plotCat(x_entries,npArr(yIter),plotColors[i])
GUI.plotTot(x_entries,npArr(y_entriesTot),(0,255,0))


GUI.mainWindow.show()
app.exec()