from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


class gui(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        self.setWindowTitle('Arch Linux Customizer')

        self.setMaximumWidth(500)
        self.setMinimumWidth(500)
        self.setMaximumHeight(650)
        self.setMinimumHeight(650)


        self.thrd = thread()
        self.thrd.start()

        self.body()

    def body(self):
        ## themes section

        self.themes = QLabel('Themes:', self)
        self.themes.setGeometry(10, 20, 50,50)

        self.vertixBtn = QPushButton('Vertex Themes', self)
        self.vertixBtn.setGeometry(40, 60, 140, 40)
        self.vertixBtn.setCursor(QCursor(Qt.PointingHandCursor))



        self.arcBtn = QPushButton('Arc Themes', self)
        self.arcBtn.setGeometry(300, 60, 140, 40)
        self.arcBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.arcBtn.clicked.connect(self.arcTheme)
        self.arcBtn.clicked.connect(self.threading)



        line = QFrame(self)
        line.setFrameShape(QFrame.HLine)
        line.setGeometry(10, 100, 480, 50)


        ## icons section

        icons = QLabel('Icons:', self)
        icons.setGeometry(10, 180, 50,50)

        self.arcBtnIco = QPushButton('Arc Icon', self)
        self.arcBtnIco.setGeometry(40, 220, 120, 40)
        self.arcBtnIco.setCursor(QCursor(Qt.PointingHandCursor))

        self.buufBtn = QPushButton('Buuf Icons', self)
        self.buufBtn.setGeometry(190, 220, 120, 40)
        self.buufBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.oranBtn = QPushButton('Oranchelo', self)
        self.oranBtn.setGeometry(340, 220, 120,40)
        self.oranBtn.setCursor(QCursor(Qt.PointingHandCursor))

        line2 = QFrame(self)
        line2.setFrameShape(QFrame.HLine)
        line2.setGeometry(10, 300, 480, 50)

        ## Terminal Edit

        terminal = QLabel('Change Terminal command prompt:', self)
        terminal.setGeometry(10, 320, 250, 50)

        self.terminalBtn = QPushButton('Change terminal', self)
        self.terminalBtn.setGeometry(170, 370, 150,40)
        self.terminalBtn.setCursor(QCursor(Qt.PointingHandCursor))

        ## Process show

        self.prcsShow = QTextEdit(self)
        self.prcsShow.setGeometry(10, 430, 480, 210)
        self.prcsShow.setReadOnly(True)
        self.prcsShow.setStyleSheet('QWidget {background-color:black;}')


    def arcTheme(self):
        return 'yaourt -S arc-cyberfox-theme --noconfirm'

    def threading(self):

        self.connect(self.thrd, SIGNAL('ProcessRunning'), self.textAdd)



    def textAdd(self, val):
        self.prcsShow.append(val)


##Threading class

class thread(QThread):
    def __init__(self):

        mainClass = gui
        self.cmd = str(mainClass.arcTheme(self))

        super(thread, self).__init__()

    def run(self):
        command = self.cmd
        self.pro = subprocess.Popen(command.split(),\
                                    stdout=subprocess.PIPE,\
                                    stderr=subprocess.STDOUT,\
                                    universal_newlines=True)

        while True:
            line = self.pro.stdout.readline()
            if self.pro.poll() != None:
                break
            self.emit(SIGNAL('ProcessRunning'), line)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = gui()
    window.show()
    sys.exit(app.exec_())