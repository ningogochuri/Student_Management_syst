class Person:
#მშობელი კლასი, რომელიც აღწერს პერსონებს

    def __init__(self, name):
        # ვამოწმებთ, რომ სახელი ტექსტური იყოს და ცარიელი არ იყოს
        if not isinstance(name, str) or not name.strip():
            raise ValueError("სახელი არ შეიძლება იყოს ცარიელი!")

        # ვინახავთ სახელს (ინკაფსულაცია)
        self.__name = name.strip()

    def get_name(self):
        # ვაბრუნებთ ადამიანის სახელს
        return self.__name

    def display_info(self):
        # გამოგვაქვს ადამიანის ინფორმაცია
        print(f"სახელი: {self.__name}")
