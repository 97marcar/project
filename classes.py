#!/home/macke/anaconda3/bin/python3.5
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
            elif self.position == 2:
                return("It's in the forest next to the wooden house.")

            elif self.position == 3:
                return("It's in the clearing.")

            elif self.position == 4:
                return("It's in the entrance of the cave.")

            elif self.position == 5:
                return("It's in the Bandit Camp.")

            elif self.position == 6:
                return("It's in the room of the stone guardian.")
            elif self.position == 123123:
                return("It's in the bandits possession.")

            else:
                return ("It's nowhere to be found.")

class Ruby(Item):
    def __init__(self):
        super().__init__()
        self.position = 6
        self.name = "Ruby"

    def get_position(self,found):
        if self.status == "picked up":
            return("It's in your inventory")
        elif found == 1:
            return("The bandits says it's guarded by a stone guardian.")
        elif found == 2:
            if self.position == 1:
                return ("It's in front of the wooden house.")

            elif self.position == 2:
                return("It's in the forest next to the wooden house.")

            elif self.position == 3:
                return("It's in the clearing.")

            elif self.position == 4:
                return("It's in the entrance of the cave.")

            elif self.position == 5:
                return("It's in the Bandit Camp.")

            elif self.position == 6:
                return("It's in the room of the stone guardian.")
        else:
            return("I beg your pardon?")
