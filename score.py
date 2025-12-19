# Function to check pass or fail
def check_result(score):
    if score >= 60:
        return "PASS"
    else:
        return "FAIL"

# Function to print report card
def report_card(name, marks):
    print("\n--- REPORT CARD ---")
    print("Student Name:", name)

    for subject, score in marks.items():
        result = check_result(score)
        print(subject, ":", score, "-", result)

# Student details
student_name = "Lokesh"

subjects_marks = {
    "Maths": 75,
    "Science": 58,
    "English": 65,
    "Computer": 80
}

# Call function
report_card(student_name, subjects_marks)
