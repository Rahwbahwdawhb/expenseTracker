from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from pyqtgraph import PlotWidget, mkPen
from numpy import array as nArray

class trackerGUI:
    def __init__(self):
        self.mainWindow=QWidget()
        mainLayout=QGridLayout()
        self.mainWindow.setLayout(mainLayout)

        self.monthPlot_category=PlotWidget()
        self.monthPlot_total=PlotWidget()
        mainLayout.addWidget(self.monthPlot_category,0,0)
        mainLayout.addWidget(self.monthPlot_total,1,0)

    def plotTot(self,xIn,yIn,RGB):
        self.monthPlot_total.plot(xIn,yIn,pen=mkPen(color=RGB))
    def plotCat(self,xIn,yIn,RGB):
        self.monthPlot_category.plot(xIn,yIn,pen=mkPen(color=RGB))

if __name__=='__main__':
    app=QApplication([])
    gui=trackerGUI()
    gui.mainWindow.show()
    app.exec()

