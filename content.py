from room import *

class Content:
    def __init__(self, position):
        self.pos = position
        self.enter = ""
        self.command = ""
        self.rooms = []
        self.zero()
        self.one()



    def handle_command(self, command):
        if self.pos == 0 and command == "begin":
            self.pos = 1
            return "beginning"


    def zero(self):
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
        position = 1
        name = "Wooden House"
        description = "You are standing in the front of a wooden house.\
        It looks like there is forest in all directions, all though it looks like there is a path \
        to the west."
        room_1 = Room(position,name,description)
        self.rooms.append(room_1)

    def get_description(self):
        return self.rooms[self.pos].description
