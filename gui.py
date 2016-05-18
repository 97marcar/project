#!/home/macke/anaconda3/bin/python3.5
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import content



app = QApplication(sys.argv)

class Reeve(QMainWindow):
    """The main class"""
    def __init__(self, parent=None):
        """Constructor, creates variables and run methods at the start"""
        super(Reeve, self).__init__()
        self.setWindowTitle("Test") #Sets the window Title
        self.preset = 0
        self.initUI()
        self.setGeometry(735,30,450,500) #Sets the size and position of the window
        self.room.setText("Main Menu") #Text that displays where you are
        self.content = content.Content(0) #Creates a class from the content file
        self.output.append(self.content.get_description()) #Outputs the mainmenu text in the beginning of the game
        self.setStyleSheet('font-size: 12pt; font-family: Times New Roman;')
        self.setStyleSheet('font-size: 12pt; font-family: American Typewriter;')

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
        if "clear" in second:
            self.output.clear()

        if "Wooden House" in second:
            self.room.setText("Wooden House")

        if "Forest" in second:
            self.room.setText("Forest")

        if "Clearing" in second:
            self.room.setText("Clearing")

        if "BanditCamp" in second:
            self.room.setText("Bandit Camp")

        if second == "note":
            self.inv["inventory0"].setText("Note")

        if second == "dropNote":
            self.inv["inventory0"].setText("")





        self.output.append(self.string+"\n")
        self.output_window(answer)
        if "check" in second:
            if self.content.pos == self.content.note.position:
                self.output.append("There is a note laying on the ground.")

        if "first" in second:
            self.output.append("You are carrying a backpack with a label "
            "that says: "
            'Belongs to Reeve".')

        if second == "cursorTop":
            self.output.moveCursor(QTextCursor.Start) #moves to cursor to the top



    def output_window(self, answer):
        """Outputs the answer from the content file"""
        self.output.append(answer+"\n")

    def run(self):
        """Runs the application"""
        self.show()
        sys.exit(app.exec_())



Reeve().run()
