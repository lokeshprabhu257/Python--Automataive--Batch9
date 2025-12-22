class Robot:
    def __init__(self, id_no, task):
        self.id_no = id_no
        self.task = task

    def show_details(self):
        print("Robot ID :", self.id_no)
        print("Assigned Task :", self.task)


# creating two robot objects
r1 = Robot("RX-101", "Cleaning solar panels")
r2 = Robot("ZX-555", "Exploring Mars surface")

# displaying details
r1.show_details()
print()
r2.show_details()
