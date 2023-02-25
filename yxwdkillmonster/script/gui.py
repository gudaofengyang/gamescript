import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

def Hello(a):

    if a==0:
        b = False
    else:
        b = True
    return b

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile



app = QApplication([])
qfile = QFile('jui.ui')
qfile.open(QFile.ReadOnly)
ui = QUiLoader().load(qfile)
qfile.close()

def click():
    a = int(ui.aInput.text())
    c = Hello(a)
    ui.aOutput.append(str(c))

ui.pushButton.clicked.connect(click)
ui.show()
app.exec_()
