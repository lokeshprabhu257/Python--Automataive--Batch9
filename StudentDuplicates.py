# Find students who have the same first name but different surnames

students = ["Ravi Kumar", "Ravi Sharma","Anil Verma", "Anil Singh","Suresh Rao", "Manoj Patel","Rahul Das", "Rahul Ghosh","Amit Shah", "Amit Mehta",
            "Kiran Joshi", "Neha Gupta","Pooja Iyer", "Sneha Nair","Arjun Malhotra", "Vikas Jain","Priya Khanna", "Nitin Bansal",
            "Rohit Agarwal", "Sunil Mishra"]

name_map = {}

# Group surnames by first name
for student in students:
    first_name, surname = student.split()
    
    if first_name in name_map:
        name_map[first_name].add(surname)
    else:
        name_map[first_name] = {surname}

print("Students with same first name but different surnames:")

for first_name, surnames in name_map.items():
    if len(surnames) > 1:           # Check if there are multiple surnames for the same first name in set
        for surname in surnames:
            print(f"{first_name} {surname}")