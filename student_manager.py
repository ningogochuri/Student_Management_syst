from student import Student
from json_manager import JSONManager


class StudentManager:
    # კლასი, რომელიც მართავს სტუდენტების ინფორმაციას

    def __init__(self):
        # ვქმნით JSONManager-ის ობიექტს
        self.json_manager = JSONManager()

        # სტუდენტების მონაცემები ჩაიტვირთოს JSON ფაილიდან
        self.students = []

        students_data = self.json_manager.read_data()

        for student_data in students_data:
            student = Student(
                student_data["name"],
                student_data["roll_number"],
                student_data["grade"]
            )

            self.students.append(student)

    def add_student(self, student):
        # ვამოწმებთ, ხომ არ არსებობს იგივე სიის ნომერი
        for current_student in self.students:
            if current_student.get_roll_number() == student.get_roll_number():
                return False

        # ვამატებთ სტუდენტს სიაში
        self.students.append(student)

        # ვინახავთ მონაცემებს JSON ფაილში
        self.save_students()

        return True

    def get_all_students(self):
        # ვაბრუნებთ ყველა სტუდენტის სიას
        return self.students

    def find_student(self, roll_number):
        # ვეძებთ სტუდენტს სიის ნომრით
        for student in self.students:
            if student.get_roll_number() == roll_number:
                return student

        # თუ სტუდენტი ვერ ვიპოვეთ
        return None

    def update_student_grade(self, roll_number, new_grade):
        # ვეძებთ სტუდენტს
        student = self.find_student(roll_number)

        if student is None:
            return False

        # ვანახლებთ სტუდენტის შეფასებას
        student.update_grade(new_grade)

        # ვინახავთ განახლებულ მონაცემებს
        self.save_students()

        return True

    def save_students(self):
        # სტუდენტების ობიექტები გადაგვყავს  სიაში
        students_data = []

        for student in self.students:
            student_data = {
                "name": student.get_name(),
                "roll_number": student.get_roll_number(),
                "grade": student.get_grade()
            }

            students_data.append(student_data)

        # ვინახავთ მონაცემებს JSON ფაილში
        self.json_manager.write_data(students_data)
