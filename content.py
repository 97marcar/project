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
        self.note = Note()
        self.list_of_commands()

    def list_of_commands(self):
        """Creates lists of commands, for structure"""
        self.compass = [["n", "go n", "north", "go north"],
        ["s", "go s", "south", "go south"],
        ["w", "go w", "west", "go west"],
        ["e", "go e", "east", "go east"],
        ["nw", "go nw", "northwest", "go northwest"],
        ["ne", "go ne", "northeast", "go northeast"],
        ["sw", "go sw", "southwest", "go southwest"],
        ["se", "go se", "southeast", "go southeast"]]

        self.takeNote = ["take note", "pick up note"]

    def handle_command(self, command):
        """Here the command given from the gui is handled"""
        #Main Menu
        if self.pos == 0 and command == "begin":
            self.pos = 1
            return (self.get_description(),"clear")

        #General
            #Note
        elif self.pos == self.note.position and command in self.takeNote \
        and self.note.status == "dropped":
            self.note.status = "picked up"
            return ("You picked up a note.", "note")

        elif self.note.status == "picked up" and command == "read note":
            return (self.note.description, "")

        elif command in self.compass[0]:
            return("123","")
        elif command in self.compass[1]or[2]or[3]or[4]or[5]or[6]:
            return("1234","")

        else:
            return ("I beg your pardon?", "")




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
        description = ("You are standing in the front of a wooden house.\n"
        "It looks like there is forest in all directions, all though it looks like "
        "there is a path to the west.\n"
        "It's a note laying on the ground.")
        room_1 = Room(position,name,description)
        self.rooms.append(room_1)

    def get_description(self):
        """Returns the description of the current room"""
        return self.rooms[self.pos].description
