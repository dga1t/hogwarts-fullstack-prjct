import pymongo
from Student import Student
from bson.objectid import ObjectId
import json


class MongoDataLayer:

    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts_db"]

    def __init__(self):
        self.__create()

    def add_student(self, student_obj):
        student_json = student_obj.__dict__
        self.__db.students.insert_one(student_json)

    def delete_student(self, student):
        self.__db.students.remove({"_id": ObjectId(student["_id"])})

    def get_all_students(self):
        student_dict = {}
        students = self.__db["students"].find()
        print("this is from mongoDatalayer:", students)
        for student in students:
            student_dict[str(student["_id"])] = Student.from_json(student)
        return student_dict

#     def load_students_from_json(self):
#         with open("../students.json", "r") as f:
#             students = json.load(f)
#             print(students)
#             self.__db.insert(students)
#
#
# newMongo = MongoDataLayer()
# newMongo.load_students_from_json()



# client = pymongo.MongoClient("localhost", 27017)
# db = client["hogwarts_db"]
