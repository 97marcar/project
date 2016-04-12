from classes import *

class Content:
    def __init__(self, position):
        """This class controlls the game"""
        self.pos = position
        self.enter = ""
        self.command = ""
        self.rooms = []
        self.zero()
        self.one()
        self.two()
        self.three()
        self.note = Note()
        self.list_of_commands()
        self.long_sentences()

    def list_of_commands(self):
        """Creates lists of commands, for structure"""
        self.compass = [["n", "go n", "north", "go north"],
        ["w", "go w", "west", "go west"],
        ["s", "go s", "south", "go south"],
        ["e", "go e", "east", "go east"],
        ["nw", "go nw", "northwest", "go northwest"],
        ["ne", "go ne", "northeast", "go northeast"],
        ["sw", "go sw", "southwest", "go southwest"],
        ["se", "go se", "southeast", "go southeast"]]

        self.takeNote = ["take note", "pick up note"]

        self.lockpick = ["pick lock", "lockpick", "lockpick door"]
        self.info = ["info","examine","information","look around"]
        self.swim_west = ["swim", "swim west", "swim w"]

    def handle_command(self, command):
        """Here the command given from the gui is handled"""

        #Main Menu
        if self.pos == 0:
            if command == "begin":
                self.pos = 1
                return (self.get_description(),"clear Wooden House first")

        #General
         #~Note
        elif self.pos == self.note.position and command in self.takeNote \
        and self.note.status == "dropped":
            self.note.status = "picked up"
            return ("You picked up a note.", "note")

        elif self.note.status == "picked up" and command == "read note":
            return (self.note.description, "")

        elif command in self.info:
            return (self.get_description(),"")

        #Room 1 Wooden House
        elif self.pos == 1:
            if command in self.compass[1]:
                self.pos = 2
                return(self.get_description(),"clear Forest")

            elif command in self.compass[0] or command == "enter house":
                return("The door is locked.","")

            elif command == "describe house":
                return(self.one.house_description,"")

            elif command in self.lockpick:
                return("You don't have a lockpick.")

            elif command == "break door":
                return("Don't overestimate your strength.")

            elif command == "break window":
                return(self.break_window,"")

            elif command in self.compass[2] or command in self.compass[3] or \
            command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7] or \
            command in self.compass[8]:
                return("The forest is to dense, you can't go there.","")

            else:
                return ("I beg your pardon?", "")

        #Room 2 Forest
        elif self.pos == 2:
            if command in self.compass[3]:
                self.pos = 1
                return (self.get_description(),"clear Wooden House")

            elif command in self.compass[1]:
                self.pos = 3
                return (self.get_description(),"clear Clearing")

            elif command in self.compass[0] or command in self.compass[2] or \
            command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7] or \
            command in self.compass[8]:
                return("The forest is to dense, you can't go there.","")

        #Room 3 Clearing
        elif self.pos == 3:
            if command in compass[1]:
                return("You're not Jesus, you can't walk on water.")

            if command in self.swim_west:
                return("You never learned how to swim.")

            if command in compass[0]:
                self.pos = 4
                return(self.get_description(),"clear Cave")


        else:
            return ("I beg your pardon?", "")


    def long_sentences(self):
        self.break_window = ("You break the window and try to crawl inside "
        "but cut yourself on one of the peices and swear to yourself not to try that again.")

    def zero(self):
        """Creates room 0, The Main Menu"""
        position = 0
        name = "Main Menu"
        description = ('Welcome to the world of test.\n'
        'Type:\n'
        '"begin" to start the game \n'
        '"options" for options \n'
        '"credits" for credits \n')
        room_0 = Room(position,name,description)
        self.rooms.append(room_0)

    def one(self):
        """Creates room 1, right outside the wooden house"""
        position = 1
        name = "Wooden House"
        house_description = ("It's a wooden house with a wooden door and"
        " a window next to it")
        description = ("You are standing in the front of a wooden house.\n"
        "It looks like there is forest in all directions, all though it looks like "
        "there is a path to the west.\n"
        "It's a note laying on the ground.")
        room_1 = Room(position,name,description)
        self.rooms.append(room_1)

    def two(self):
        """Creates room 2, Forest"""
        position = 2
        name = "Forest"
        description = ("You are standing in "
        "the middle of a forest.\n"
        "The path continues to the west.\n"
        "There is a very large rotten three here.")
        room_2 = Room(position,name,description)
        self.rooms.append(room_2)

    def three(self):
        "Creates room 3, Clearing"
        position = 3
        name = "Clearing"
        description = ("You entered a clearing.\n"
        "It looks to be a waterhole here as well as \n"
        "a caveopening in front of you.\n"
        "Also there is a path to the south.")
        room_3 = Room(position,name,description)
        self.rooms.append(room_3)

    def four(self):
        position = 4
        name = "Cave"
        description = ("You entered a cave."
        "It's really dark here except for what looks to be"
        "a light from a torch northwest of you.")
        room_4 = Room(position,name,description)
        self.rooms.append(room_3)

    def get_description(self):
        """Returns the description of the current room"""
        return self.rooms[self.pos].description
