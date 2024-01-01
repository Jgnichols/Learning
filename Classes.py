import datetime as dt

class Member: # Defines a new class called Member
    """ Creates a new member object """

    free_days = 0
    
    # Creates a class method
    @classmethod
    def setfreedays(cls, days): # Syntax is def methodname(cls, variable, ...):
        cls.free_days = days

    def __init__(self, uname, fname):
        # Define attributes and gives them values
        self.username = uname
        self.fullname = fname
        self.date_joined = dt.date.today()
        self.free_expires = dt.date.today() + dt.timedelta(days=self.free_days) # Must have (Member. or self. in front of variable)
        self.is_active = True

    # Creates a static method
    @staticmethod
    def currenttime():
        now = dt.datetime.now() # Does not use cls, or self
        return f"{now:%I:%M %p}"

    # A method to return a formatted string showing date joined
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%Y}"
    
    # A method to change is_active to (True) or (False)
    def activate(self, yesno):
        self.is_active = yesno

# Creates a object (new_guy) in the class (Member)
new_guy = Member("Rambo", "Rocco Moe")

#Creates a object (wilbur) in the class (Member) with username (wblomgren) and full name (Wilbur Blomgren)
wilbur = Member("wblomgren", "Wilbur Blomgren")

#Edits the attribute for the object
new_guy.activate(False)

# Edits the amount of free days a member gets
Member.setfreedays(90)

print(wilbur.free_days)
print(dt.date.today() + dt.timedelta(days=wilbur.free_days))
print(Member.currenttime())
print(Member.show_datejoined(wilbur))
print(wilbur.free_expires)
