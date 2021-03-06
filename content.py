#!/home/macke/anaconda3/bin/python3.5
from classes import *
import database

class Content:
    def __init__(self, position):
        """This class controlls the game"""
        self.rooms = []
        self.create_variables()
        self.create_items()
        self.create_rooms()
        self.list_of_commands()
        self.long_sentences()
        self.pos = position
        database.create_table()

    def create_rooms(self):
        """Creates all the rooms at the start of the program"""
        self.zero()
        self.one()
        self.two()
        self.three()
        self.four()
        self.five()
        self.six()

    def create_items(self):
        """Creates all the items at the start of the program"""
        self.note = Note()
        self.ruby = Ruby()

    def create_variables(self):
        """Creates all the variables at the start of the program"""
        self.chances = 0
        self.readNote = False
        self.bandit_conv_over = False
        self.stone_conv_over = False
        self.stone_correct = False
        self.window = ("whole")
        self.quest = "not started"
        self.save = False
        self.load = False
        self.delete = False
        self.overwrite = False

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
        self.noteInfo = ["where is the note", "where is note",
        "where is the note?", "where is note?"]

        self.takeRuby = ["take ruby", "pick up ruby"]
        self.rubyInfo = ["where is the ruby", "where is ruby",
        "where is the ruby?", "where is ruby?"]


        self.lockpick = ["pick lock", "lockpick", "lockpick door",
        "lockpick the door"]
        self.break_door = ["break door", "slam door", "break the door",
        "slam the door"]
        self.info = ["info","examine","information","look around"]
        self.swim_west = ["swim", "swim west", "swim w"]

        self.bandit_conv_start = ["talk", "talk to the bandits", "speak"
        "speak to the bandits", "talk bandits", "speak bandits"]

        self.stone_conv_start = ["talk", "talk to the stone guardian", "speak"
        "speak to the stone guardian", "talk stone guardian",
        "speak stone guardian"]


    def handle_command(self, command):
        """Here the command given from the gui is handled"""

        #Main Menu

        if self.pos == 0:
            if command == "begin":
                self.pos = 1
                return (self.get_description(),"clear Wooden House first check")

            else:
                return("Please type in one of the above.","")

        if self.pos == 666:
            return("RESTART THE GAME TO TRY AGAIN.","")

        if self.pos == 7777:
            return("RESTART THE GAME IF YOU WANT TO PLAY AGAIN!","")


        #General
         #~Note
        elif self.pos == self.note.position and command in self.takeNote \
        and self.note.status == "dropped":
            self.note.status = "picked up"
            return ("You picked up a note.", "note")

        elif self.note.status == "picked up" and command == "read note":
            self.readNote = True
            return (self.note.description, "")

        elif command == "drop note" and self.note.status == "picked up":
            self.note.position = self.pos
            self.note.status = "dropped"
            return("You dropped the note.", "dropNote")

        elif command in self.noteInfo:
            return(self.note.get_position(),"")

        #~Ruby
        elif self.pos == self.ruby.position and command in self.takeRuby \
        and self.ruby.status == "dropped" and self.stone_correct == True:
            self.ruby.status = "picked up"
            return ("You picked up a ruby.", "ruby")

        elif command == "drop ruby" and self.ruby.status == "picked up":
            self.ruby.position = self.pos
            self.ruby.status = "dropped"
            return("You dropped the ruby.", "dropRuby")

        elif command in self.rubyInfo:
            found = 0
            if self.bandit_conv_over == True:
                found = 1
            if self.stone_conv_over == True:
                found = 2
            return(self.ruby.get_position(found),"")

        elif command in self.info:
            return (self.get_description(),"check")

        #~Save and Load

        elif command == "save":
            self.save = True
            return('Enter your name to create a new save, "overwrite" to overwrite or "delete" to delete',"")

        elif self.save == True:
            self.save = False
            if command == "overwrite":
                self.overwrite = True
                saves = self.get_saves()
                saves += "Enter the ID of the save you wish to overwrite."
                return(saves,"")
            else:
                save_name = command
                database.save_data((save_name, self.pos, self.readNote, \
                self.note.status,self.note.position, self.bandit_conv_over))
                return("Your name is "+save_name+" and you have saved succesfully.","")

        elif self.overwrite == True:
            saveID = int(command)
            database.update_data((self.pos, self.readNote, \
            self.note.status,self.note.position, self.bandit_conv_over,saveID))
            return("You have overwritten save number: "+str(saveID)+" succesfully.","")

        elif command == "load":
            self.load = True
            saves = self.get_saves()
            saves += "Enter the ID of the save you wish to load."
            return(saves,"")

        elif self.load == True:
            self.load = False
            id = command
            selected_data = database.select_data(id)
            self.pos = [x[1] for x in selected_data][0]
            self.readNote = [x[2] for x in selected_data][0]
            self.note.status = [x[3] for x in selected_data][0]
            self.note.position = [x[4] for x in selected_data][0]
            self.bandit_conv_over = [x[5] for x in selected_data][0]
            print(self.pos, self.readNote, self.note.status, self.bandit_conv_over)

            return(self.get_description(),"")

        elif command == "delete":
            self.delete = True
            saves = self.get_saves()
            saves += "Enter the ID of the save you wish to delete"
            return(saves,"")

        elif self.delete == True:
            self.delete = False
            id = command
            database.delete_data(id)
            return("You have deleted save number: "+str(command)+" succesfully.","")

        #Room 1 Wooden House
        elif self.pos == 1:
            if command in self.compass[1]:
                self.pos = 2
                return(self.get_description(),"clear Forest check")

            elif command in self.compass[0] or command == "enter house":
                return("The door is locked.","")

            elif command == "describe house" or command == "examine house":
                return(self.one.house_description,"")

            elif command in self.lockpick:
                return("You don't have a lockpick.","")

            elif command == self.break_door:
                return("Don't overestimate your strength.","")

            elif command == "break window":
                if self.window == "whole":
                    self.window = "broken"
                    return(self.break_window,"")
                elif self.window == "broken":
                    return("The window is already broken.","")

            elif command in self.compass[2] or command in self.compass[3] or \
            command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7]:
                return("The forest is to dense, you can't go there.","")

            else:
                return ("I beg your pardon?", "")

        #Room 2 Forest
        elif self.pos == 2:
            if command in self.compass[3]:
                self.pos = 1
                if self.quest == "complete":
                    self.pos = 7777
                    return("YOU WON THE GAME!","clear Wooden House")
                return (self.get_description(),"clear Wooden House check")

            elif command in self.compass[1]:
                self.pos = 3
                return (self.get_description(),"clear Clearing check")

            elif command in self.compass[0] or command in self.compass[2] or \
            command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7]:
                return("The forest is to dense, you can't go there.","")

            else:
                return ("I beg your pardon?", "")

        #Room 3 Clearing
        elif self.pos == 3:
            if command in self.compass[1]:
                return("You're not Jesus, you can't walk on water.","")

            elif command in self.swim_west:
                return("You never learned how to swim.","")

            elif command in self.compass[0]:
                self.pos = 4
                return(self.get_description(),"clear Cave check")

            elif command in self.compass[2]:
                self.pos = 5
                if self.quest == "declined":
                    self.pos = 666
                    return(self.bandit_lose,"clear")
                elif self.quest == "incomplete":
                    if self.ruby.status == "picked up" and self.bandit_conv_over == True:
                        self.ruby.position = 123123
                        self.quest = "complete"
                        self.pos = 3
                        return(self.happybandit,"Clearing dropRuby")
                    else:
                        return(("Bandit: Do you have the Ruby?\nYou: No. \n"
                        "Bandit: Then go get it if you want the dwarf!"),"")
                else:
                    return(self.get_description(),"clear BanditCamp check")

            elif command in self.compass[3]:
                self.pos = 2
                return(self.get_description(),"clear Forest check")

            elif command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7]:
                return("The forest is to dense, you can't go there.","")

            else:
                return ("I beg your pardon?", "")


        #Room 4 Cave entrance
        elif self.pos == 4:
            if command in self.compass[2]:
                self.pos = 3
                return(self.get_description(),"clear Clearing check")

            elif command in self.compass[4]:
                self.pos = 6
                return(self.get_description(),"clear Cave check")

            elif command in self.compass[0] or command in self.compass[1] or \
            command in self.compass[3] or command in self.compass[5] or \
            command in self.compass[6] or command in self.compass[7]:
                return("It's to dark for you to go there.","")



        #Room 6 Stone Guardian
        elif self.pos == 6:
            if command in self.stone_conv_start and self.stone_conv_over == False:
                self.pos = 6.1
                return(self.stone_opener,"")
            elif command in self.compass[7]:
                self.pos = 4
                return(self.get_description(),"clear Cave check")

            elif command in self.compass[0] or command in self.compass[1] or \
            command in self.compass[2] or command in self.compass[3] or \
            command in self.compass[4] or command in self.compass[5] or \
            command in self.compass[6]:
                return("It's not recommended to talk into a wall.","")

            else:
                return("I beg your pardon?","")
        elif self.pos == 6.1:
            if command == "yes":
                self.pos = 6.2
                return(self.stone_conversation(),"")
            elif command == "no":
                self.pos = 6
                return("You may leave or speak to the guardian again. ","clear")
            else:
                return("I require a yes or no answer.","")

        elif self.pos == 6.2:
            if command == "david":
                self.pos = 6
                self.stone_conv_over = True
                self.stone_correct = True
                string_for_print = ("Correct. \n"
                "The treasure is up for grabs; a shining red ruby \
                lays in the rooms before you.")
                return(string_for_print,"")
            elif command != "david":
                print(self.chances)
                self.chances += 1
                if self.chances == 1:
                    chance_for_print = "Wrong. Two chances remaining."
                elif self.chances == 2:
                    chance_for_print = "Wrong. One chance remaining"
                elif self.chances == 3:
                    self.stone_conv_over = True
                    self.stone_correct = False
                    self.pos = 6
                    string_for_print = ("All wrong. Leave. \n"
                    "The door is closed and your chances of saving the \
                    dwarf with the ruby looks slim.")
                    return(string_for_print,"")

                return(chance_for_print,"")



        #Room 5 Bandit Camp
        elif self.pos == 5:
            if self.quest == "incomplete":
                if self.bandit_conv_over == True:
                    if command in self.compass[0]:
                        self.pos = 3
                        return(self.get_description(),"clear Clearing check")
                    else:
                        return("Leave the place by taking the northern path seems"
                        "like your only option.","")
            if self.quest == "not started":
                if self.bandit_conv_over == False:
                    if command in self.bandit_conv_start:
                        self.pos = 5.1
                        return(self.bandit_conversation(),"cursorTop")
                    else:
                        return("Talk to the bandits before doing anything else.","")


        elif self.pos == 5.1:
            if command == "yes":
                self.pos = 5
                self.quest = "incomplete"
                return(self.bandit_accept,"")
            elif command == "no":
                self.pos = 3
                self.quest = "declined"
                return(self.bandit_decline,"Clearing")
            else:
                return("Bandit: Answer me yes or no.","")

        else:
            return ("I beg your pardon?", "")



    def long_sentences(self):
        "creates lines that would look to cluncy in the middle of the code"
        self.break_window = ("You break the window and try to crawl inside "
        "but cut yourself on one of the peices and swear to yourself not to "
        "try that again.")

        self.bandit_accept = ("Bandit: Excellent! Bring back the stone to me "
        "and you can take the dwarf.")

        self.bandit_decline = ("Bandit: Then get the fuck out of here before I "
        "cut you open!")

        self.stone_opener =("Stone Guardian: Greetings, I am a ownerless stone "
        "guardian. Do you wish to obtain the treasure I'm watching over?")

        self.happybandit = ("Bandit: You got the ruby? \n You: Yes. \n"
        "Bandit: Great! Now take the dwarf and leave.\n\n"
        "Rubilnor: Thanks for saving me...?\n"
        "You: Reeve.\n"
        "Rubilnor: Reeve! Thank you sir. Let's go back to my house and I can \n"
        "make us dinner\n"
        "You: Great idea!")

        self.bandit_lose = ("Are you coming back here without the ruby?\n"
        "You: Yes\n"
        "Bandit: You are fucking done!\n\n"
        "The bandits stab you multiple times and you die in a pool of blood.\n\n"
        "YOU LOST THE GAME PLEASE RESTART TO TRY AGAIN")

    def zero(self):
        """Creates room 0, The Main Menu"""
        position = 0
        name = "Main Menu"
        description = ('Welcome!\n'
        'Type:\n'
        '"begin" to start the game \n'
        '"credits" for credits ')
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
        "there is a path to the west.")
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
        description = ("You entered a cave. "
        "It's really dark here except for what looks to be"
        "a light from a torch northwest of you.")
        room_4 = Room(position,name,description)
        self.rooms.append(room_4)

    def five(self):
        position = 5
        name = "BanditCamp"
        description = ("You have entered a camp full of, from the looks of "
        "them, \nbandits. "
        "They look like they want to talk and leaving before does not like like "
        "an option.")
        room_5 = Room(position,name,description)
        self.rooms.append(room_5)

    def six(self):
        position = 6
        name = "StoneGuardian"
        description = ("You get to a oddly looking door lit by a lonely torch.\n"
        "When you think about it, you've read about such odd looking doors, "
        "it's not a door, it's a stone guardian.\n"
        "A stone guardian is guarding something valueble and there are "
        "only 2 ways to get it: \n"
        "1. You are it's owner. \n"
        "2. It does not have an owner and you've to answer a riddle correcty. \n"
        "You can talk to it and hope it's the second alternative. ")
        room_6 = Room(position,name,description)
        self.rooms.append(room_6)

    def get_description(self):
        """Returns the description of the current room"""
        return self.rooms[self.pos].description

    def bandit_conversation(self):
        self.bandit_conv = (
        "Bandit: Tell me; what is your name and why are you here.\n\n"
        "You: I believe... my name is Reeve...\n\n"
        'Bandit: ...What do you mean "believe"? You do not know your own name?\n\n'
        "You: I don't remember anything... except a burning house and"
        "a womans scream.\n"
        'There is a label on my backpack that says "Belongs to Reeve"'
        " so I guess that is my name.\n\n"
        "...\n\n"
        "Bandit: Are you looking for someone?\n\n")
        if self.readNote == True:
            self.bandit_conv += (
            "You: More or less... I woke up next to a house and found a note."
            "Any chance you've seen someone named Ribulnor?\n\n"
            "Bandit: I do... We have him imprisoned in one of the tents.\n\n")
        else:
            self.bandit_conv += ("You: No, why? \n\n"
            "Bandit: We got a prisoner in one of our tents. \n\n")

        self.bandit_conv +=(
        "You: Why is that?\n\n"
        "Bandit: Because he failed the quest we gave him.\n\n"
        "You: What quest?\n\n"
        "Bandit: The same quest we are going to give you;\n"
        "We want a red ruby guarded by a ownerless stone guardian "
        "in a cave nearby. A stone guardian is a type of living door guarding "
        "a treasure for its owner, but if it's ownerless you can optain the "
        "treasure by giving the right answer to his riddle. You only get 3 "
        "chances thought and everyone of us including Ribulnor has failed.\n\n"
        "Bandit: Will you accept this quest?\n")
        self.bandit_conv_over = True
        return (self.bandit_conv)

    def stone_conversation(self):
        "creates the conversation with the stone guardian"
        self.stone_conv = (
        "500 at the beginning, 500 at the end, \n"
        "5 in the middle is seen, \n "
        "The first of all letters, the first of all figures \n"
        "Take up their stations between, \n"
        "String them all together, and you will see \n"
        "The name of an ancient king.\n\n"
        "You get three chances to answer right.")
        return(self.stone_conv)

    def get_saves(self):
        "a function to fetch the saves and output them to the window"
        name_id = database.select_name_and_id()
        name_list = [x[0] for x in name_id]
        id_list = [x[1] for x in name_id]
        saves = ""
        for n in range(len(name_list)):
            saves += ("\nName: "+name_list[n]+"\nID:"+str(id_list[n])+"\n")
        return(saves)
