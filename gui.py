import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import content



app = QApplication(sys.argv)

class Reeve(QMainWindow):
    """The main class"""
    def __init__(self, parent=None):
        super(Reeve, self).__init__()
        self.setWindowTitle("Test") #Sets the window Title
        self.preset = 0
        self.initUI()
        self.setGeometry(735,30,450,500) #Sets the size and position of the window
        self.room.setText("Main Menu") #Text that displays where you are
        self.content = content.Content(0) #Creates a class from the content file
        self.output.append(self.content.get_description()) #Outputs the mainmenu text in the beginning of the game


    def initUI(self):
        """Draws all the windows on the main window"""
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
        """Handles the commands and input"""
        self.string = self.input.text()
        self.input.clear()
        self.command = str(self.string)
        temp = self.content.handle_command(self.command.lower()) #Gives the content file the command written in the inputbox
        answer = temp[0]
        second = temp[1]
        if second == "clear":
            self.output.clear()
        elif second == "note":
            self.inv["inventory0"].setText("Note")

        self.output.append(self.string+"\n")
        self.output_window(answer)

    def output_window(self, answer):
        """Outputs the answer from the content file"""
        self.output.append(answer+"\n")

    def run(self):
        """Runs the application"""
        self.show()
        sys.exit(app.exec_())



Reeve().run()
