from person import Person


class Student(Person):
#სტუდენტის კლასი, რომელიც მემკვიდრეობით იღებს Person კლასს

    def __init__(self, name, roll_number, grade):
        # მშობელი კლასიდან სახელის მიღება
        super().__init__(name)

        # ვამოწმებთ სიის ნომერს
        if not isinstance(roll_number, int) or isinstance(roll_number, bool) or roll_number <= 0:
            raise ValueError("სიის ნომერი უნდა იყოს დადებითი მთელი რიცხვი!")

        # ვამოწმებთ შეფასებას
        if not isinstance(grade, str) or grade.upper() not in ["A", "B", "C", "D", "F"]:
            raise ValueError("შეფასება უნდა იყოს A, B, C, D ან F!")

        # ვინახავთ სტუდენტის მონაცემებს
        self.__roll_number = roll_number
        self.__grade = grade.upper()

    def get_roll_number(self):
        # ვაბრუნებთ სტუდენტის სიის ნომერს
        return self.__roll_number

    def get_grade(self):
        # ვაბრუნებთ სტუდენტის შეფასებას
        return self.__grade

    def update_grade(self, new_grade):
        # ვამოწმებთ ახალ შეფასებას
        if not isinstance(new_grade, str) or new_grade.upper() not in ["A", "B", "C", "D", "F"]:
            raise ValueError("არასწორი შეფასება!")

        self.__grade = new_grade.upper()

    def display_info(self):
        # პოლიმორფიზმი: მშობელი კლასის მეთოდის საკუთარი ვერსია
        print(f"სახელი: {self.get_name()}")
        print(f"სიის ნომერი: {self.__roll_number}")
        print(f"შეფასება: {self.__grade}")
