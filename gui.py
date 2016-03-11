import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import content



app = QApplication(sys.argv)

class Reeve(QMainWindow):

    def __init__(self, parent=None):
        super(Reeve, self).__init__()
        self.setWindowTitle("Test")
        self.preset = 0
        self.initUI()
        self.setGeometry(735,30,450,500)
        self.room.setText("Main Menu")
        self.content = content.Content(0)
        self.output.append(self.content.get_description())


    def initUI(self):

        self.frame = QWidget(self)
        self.setCentralWidget(self.frame)

        self.layout = QVBoxLayout()
        self.invlayout = QGridLayout()

        self.room = QLabel()
        self.layout.addWidget(self.room)

        self.output = QTextEdit()

        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.input = QLineEdit()
        self.layout.addWidget(self.input)
        self.frame.setLayout(self.layout)
        self.input.setMinimumHeight(30)
        self.input.returnPressed.connect(self.add_input)

        self.inventorylabel = QLabel("Inventory")
        self.layout.addWidget(self.inventorylabel)
        self.layout.addLayout(self.invlayout)

        self.inv={}
        for n in range(0, 13):
            if n > 5:
                g = 2
                h = n-7
            else:
                g = 1
                h = n
            if h == -1:
                h = 0
            self.inv["inventory{0}".format(n)] = QTextEdit()
            self.inv["inventory"+str(n)].setReadOnly(True)
            self.invlayout.addWidget( self.inv["inventory"+str(n)], g, h)
            self.inv["inventory"+str(n)].setMaximumHeight(30)

    def add_input(self):
        self.string = self.input.text()
        self.input.clear()
        self.command = str(self.string)
        temp = self.content.handle_command(self.command)
        answer = temp[0]
        clear_check = temp[1]
        if clear_check == "clear":
            self.output.clear()

        self.output.append(self.string)
        self.output_window(answer)

    def output_window(self, answer):
        self.output.append(answer)

    def run(self):
        self.show()
        sys.exit(app.exec_())



Reeve().run()
