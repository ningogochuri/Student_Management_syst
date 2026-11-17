
from student import Student
from student_manager import StudentManager


class Menu:
    # კლასი, რომელიც მართავს მომხმარებლის მენიუს

    def __init__(self):
        # ვქმნით StudentManager-ის ობიექტს
        self.manager = StudentManager()

    def show_menu(self):
        # გამოვიტანოთ მთავარი მენიუ
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Grade")
        print("5. Exit")

    def run_menu(self):
        # პროგრამის მთავარი ციკლი
        while True:
            self.show_menu()

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                # ვიღებთ სტუდენტის მონაცემებს
                name = input("Enter student name: ").strip()

                try:
                    roll_number = int(input("Enter roll number: "))
                    grade = input("Enter grade: ").strip()

                    student = Student(name, roll_number, grade)

                    if self.manager.add_student(student):
                        print("Student added successfully!")
                    else:
                        print("This roll number already exists!")

                except ValueError as error:
                    print(f"Error: {error}")

            elif choice == "2":
                # გამოგვაქვს ყველა სტუდენტი
                students = self.manager.get_all_students()

                if not students:
                    print("No students found!")
                else:
                    for student in students:
                        print("--------------------")
                        student.display_info()

            elif choice == "3":
                # ვეძებთ სტუდენტს სიის ნომრით
                try:
                    roll_number = int(input("Enter roll number: "))
                    student = self.manager.find_student(roll_number)

                    if student is None:
                        print("Student not found!")
                    else:
                        student.display_info()

                except ValueError:
                    print("Please enter a valid number!")

            elif choice == "4":
                # ვაახლებთ სტუდენტის შეფასებას
                try:
                    roll_number = int(input("Enter roll number: "))
                    new_grade = input("Enter new grade: ").strip()

                    if self.manager.update_student_grade(roll_number, new_grade):
                        print("Grade updated successfully!")
                    else:
                        print("Student not found!")

                except ValueError as error:
                    print(f"Error: {error}")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please select 1-5.")
