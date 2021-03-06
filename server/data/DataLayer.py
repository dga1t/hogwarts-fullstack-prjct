import json
from Student import Student
from data.mongoDatalayer import MongoDataLayer


class DataLayer:
    def __init__(self):
        self.mongo_db = MongoDataLayer()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def shutdown(self):
        self.mongo_db.shutdown()

    def add_student(self, student_obj):
        self.mongo_db.add_student(student_obj)

    # def edit_student(self, edited_student):
    #     self.mongo_db.edit_student(edited_student)

    def delete_student(self, student):
        self.mongo_db.delete_student(student)

    def get_student_by_email(self, email):
        student = self.mongo_db.get_student_by_email(email)
        return student.__dict__

        # student = self.students_dict.get(students_email)
        # return student.__dict__

    def get_students_by_date(self, date):
        students_dict = {}
        students = self.mongo_db.get_students_by_date(date)
        for key, value in students.items():
            students_dict[key] = value.__dict__
        return students_dict

    def get_all_students(self):
        students_dict = {}
        students = self.mongo_db.get_all_students()
        for key, value in students.items():
            students_dict[key] = value.__dict__
        return students_dict

        # students = {}
        # for key, value in self.students_dict.items():
        #     students[key] = value.__dict__
        # return students

    # 3.4 function for receiving all students within the dictionary as json strings
    def receive_students_as_json(self):
        pass

        # students_json_list = []
        # students_list = self.receive_all_students()
        # for instance in students_list:
        #     students_json_list.append(str(instance))
        # return students_json_list


    # 3.6
    def persist_students(self):
        """converts the dictionary to a json and stores it within the data directory as file"""
        pass

        # students = {}
        # for key, value in self.students_dict.items():
        #     students[key] = value.__dict__
        #
        # with open("../students.json", "w") as write_file:
        #     write_file.write(json.dumps(students))
        #     return "Students Persisted successfully!!1"

    @staticmethod
    def load_all_students():
        """loads all the students in the json file into a dictionary object"""
        pass

    #     try:
    #         # create path to json file
    #         folder_with_json_file = pathlib.Path(__file__).resolve().parent
    #         read_file = str(folder_with_json_file) + os.sep + "students.json"
    #
    #         if os.path.exists(read_file):
    #             with open("../students.json", "r") as f:
    #                 students = json.load(f)
    #                 students_dict = {}
    #                 for key, value in students.items():
    #                     students_dict[key] = Student.from_json(value)
    #             return students_dict
    #         else:
    #             raise Exception("File doesn't exist")
    #
    #     except Exception as e:
    #         raise Exception("something went wrong, error is: {}".format(e))


    # def add_student(self, student_obj):
        # if student_obj is None:
        #     raise ValueError("Missing required student instance!")
        # if student_obj.get_email() in self.students_dict.keys():
        #     raise ValueError("Email already exists!")
        #
        # student_dict_entry = {student_obj.get_email(): student_obj}
        # self.students_dict.update(student_dict_entry)
        #
        # print("student added to dic successfully")


