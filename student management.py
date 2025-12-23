class Student:
    def __init__(self, name, roll_no, branch, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print(f"{self.name:<15} {self.roll_no:<10} {self.branch:<10} {self.cgpa:<5}")



students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Roll Number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        branch = input("Enter branch: ")
        cgpa = float(input("Enter CGPA: "))
        students.append(Student(name, roll_no, branch, cgpa))
        print(f"\n Student '{name}' added successfully!")

    elif choice == '2':
        if students:
            print("\n----- All Students -----")
            print(f"{'Name':<15} {'Roll No':<10} {'Branch':<10} {'CGPA':<5}")
            print("-" * 45)
            for s in students:
                s.display()
        else:
            print("\n No students found. Please add some first.")

    elif choice == '3':
        if students:
            name = input("Enter the name of the student to update roll number: ")
            found = False
            for s in students:
                if s.name.lower() == name.lower():
                    new_roll = input(f"Enter new roll number for {s.name}: ")
                    s.roll_no = new_roll
                    print(f"\n Roll number updated for {s.name}!")
                    found = True
                    break
            if not found:
                print("\n Student not found.")
        else:
            print("\n No students found. Please add some first.")

    elif choice == '4':
        print("\n Exiting program... Goodbye!")
        break

    else:
        print("\n Invalid choice! Please enter a number between 1 and 4.")
