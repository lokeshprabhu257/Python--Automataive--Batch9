# -------------------- Custom Exceptions --------------------
class StudentNotFoundError(Exception):
    pass

class SubjectNotFoundError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass


# -------------------- Decorators with Exceptions --------------------
def validate_student_id(func):
    def wrapper(self, student_id, *args, **kwargs):
        if student_id not in self.students:
            raise StudentNotFoundError("Student not found.")
        return func(self, student_id, *args, **kwargs)
    return wrapper


def validate_subject(func):
    def wrapper(self, student_id, subject, *args, **kwargs):
        if subject not in self.students[student_id].marks:
            raise SubjectNotFoundError("Subject not found for this student.")
        return func(self, student_id, subject, *args, **kwargs)
    return wrapper


# -------------------- Student Class --------------------
class Student:
    def __init__(self, student_id, name, class_name):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def update_marks(self, subject, mark):
        self.marks[subject] = mark

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Class: {self.class_name}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")


# -------------------- School Management System --------------------
class SchoolManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, class_name):
        if student_id in self.students:
            raise DuplicateStudentError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name, class_name)

    @validate_student_id
    def display_student_info(self, student_id):
        self.students[student_id].display_info()
        print()

    @validate_student_id
    def add_marks(self, student_id, subject, mark):
        self.students[student_id].add_marks(subject, mark)

    @validate_student_id
    @validate_subject
    def update_marks(self, student_id, subject, mark):
        self.students[student_id].update_marks(subject, mark)

    def display_students(self):
        for student in self.students.values():
            student.display_info()
            print()


# -------------------- Main Program --------------------
def main():
    sms = SchoolManagementSystem()

    while True:
        try:
            print("\n1. Add Student")
            print("2. Add Marks")
            print("3. Update Marks")
            print("4. Display Student Info")
            print("5. Display All Students")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                class_name = input("Enter student class: ")
                sms.add_student(student_id, name, class_name)

            elif choice == "2":
                student_id = input("Enter student ID: ")
                subject = input("Enter subject: ")
                mark = float(input("Enter mark: "))
                sms.add_marks(student_id, subject, mark)

            elif choice == "3":
                student_id = input("Enter student ID: ")
                subject = input("Enter subject: ")
                mark = float(input("Enter new mark: "))
                sms.update_marks(student_id, subject, mark)

            elif choice == "4":
                student_id = input("Enter student ID: ")
                sms.display_student_info(student_id)

            elif choice == "5":
                sms.display_students()

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input! Please enter numeric values for marks.")

        except (StudentNotFoundError, SubjectNotFoundError, DuplicateStudentError) as e:
            print(e)

        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()