import json
import datetime


class Student:
    def __init__(self, ID, f_name, l_name, email, password):
        self._ID = ID
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        self.mastered_skill = None
        self.desired_skill = None
        self.creation_time = str(datetime.date.today())
        self.updated = None

    def get_email(self):
        return self.email

    def add_skill(self):
        pass

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(student_json):
        return Student(student_json['_ID'], student_json['f_name'], student_json['l_name'], student_json['email'],
                       student_json['password'])


