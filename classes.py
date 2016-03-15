class Room:
    def __init__(self, position, name, description):
        self.position = position
        self.name = name
        self.description = description


class Conversation_room(Room):
    def __init__(self, position, name, description, who):
        super().__init__(position, name, description)

class Item:
    def __init__(self):
        self.status = "dropped"
        self.found = False

    def pickup(self):
        self.status = "picked up"

    def drop(self):
        self.status = "dropped"

class Note(Item):
    def __init__(self):
        super().__init__()
        self.position = 1
        self.name = "Note"
        self.description = ("I'm going to visit my brother, be back"
                            " in a couple of days.\n"
                            "-Ribulnor")
    def get_position(self):
        if self.status == "picked up":
            return("It's in your inventory")
        else:
            if self.position == 1:
                return ("It's in front of the wooden house.")
            else:
                return ("It's nowhere to be found.")
