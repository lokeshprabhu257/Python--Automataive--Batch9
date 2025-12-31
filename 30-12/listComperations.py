# Managers
managers = ("Ravi", "Anand", "Suresh")

# Employees
employees = (
    "Arjun", "Karthik", "Vignesh", "Praveen",
    "Deepak", "Nithin", "Rahul", "Sanjay",
    "Ajith", "Manoj", "Gokul", "Harish"
)
# Create a mapping of managers to their respective employees using map and filter
reporting_map = dict(
    map(
        lambda manager: (
            manager,
            list(
                filter(
                    lambda employee: employees.index(employee) // 4 == managers.index(manager),
                    employees
                )
            )
        ),
        managers
    )
)
# Output
for manager, emp_list in reporting_map.items():
    print(f"{manager} ----> {emp_list}")