import json


class JSONManager:


    def read_data(self):
        # ვკითხულობთ სტუდენტების მონაცემებს
        try:
            with open("data/students.json", "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

    def write_data(self, data):
        # ვინახავთ სტუდენტების მონაცემებს
        with open("data/students.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
