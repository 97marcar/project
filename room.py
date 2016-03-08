class Room:
    def __init__(self, position, name, description):
        self.position = position
        self.name = name
        self.description = description


class Conversation_room(Room):
    def __init__(self, position, name, description, who):
        super().__init__(position, name, description)
        
