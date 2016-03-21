import os
import sys
from PyQt4.QtGui import *
 
# Create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("PyQT4 Pixmap @ pythonspot.com ") 
 
# Create widget
print( os.getcwd() )
p=os.path.dirname(os.path.realpath(__file__))
print(p)
label = QLabel(w)
pixmap = QPixmap(p + '/logo.jpg')
label.setPixmap(pixmap)
w.resize(pixmap.width(),pixmap.height())
 
# Draw window
w.show()
app.exec_()
