import pymongo
from Student import Student
from bson.objectid import ObjectId


class MongoDataLayer:
    def __init__(self):
        self.__connect()

    def __connect(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts_db"]

    def shutdown(self):
        self.__client.close()

    def add_student(self, student_obj):
        student_json = student_obj.__dict__
        self.__db.students.insert_one(student_json)

    # def edit_student(self, edited_student):
    #     self.__db.students.update({"_id": edited_student}, {$set: edited_student})

    def delete_student(self, student):
        self.__db.students.remove({"_id": ObjectId(student["_id"])})

    def get_student_by_email(self, email):
        student = self.__db.students.find_one({"email": email})
        student_obj = Student.from_json(student)
        return student_obj

    def get_students_by_date(self, date):
        student_dict = {}
        students = self.__db.students.find({"creation_time": date})
        for student in students:
            student_dict[str(student["_id"])] = Student.from_json(student)
        return student_dict

    def get_all_students(self):
        student_dict = {}
        students = self.__db.students.find()
        for student in students:
            student_dict[str(student["_id"])] = Student.from_json(student)
        return student_dict




# newMongo = MongoDataLayer()
# newMongo.load_students_from_json()



# client = pymongo.MongoClient("localhost", 27017)
# db = client["hogwarts_db"]
