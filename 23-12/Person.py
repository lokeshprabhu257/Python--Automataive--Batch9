#----1------
# Parent Class (Inheritance starts here)

class Person:
    def __init__(self, name):
        # Encapsulation: data inside class
        self.name = name

    # This method will be overridden (Polymorphism)
    def get_role(self):
        return "I am a Person"
    
