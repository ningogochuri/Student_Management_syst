from student import Student


class StudentManager:
# კლასი, რომელიც მართავს სტუდენტების სიას

    def __init__(self):
        # ვქმნით ცარიელ სიას სტუდენტებისთვის
        self.students = []

    def add_student(self, student):
        # ვამოწმებთ, ხომ არ არსებობს იგივე სიის ნომერი
        for current_student in self.students:
            if current_student.get_roll_number() == student.get_roll_number():
                return False

        # ვამატებთ სტუდენტს სიაში
        self.students.append(student)
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
        return True
