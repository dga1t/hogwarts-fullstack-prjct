from flask import Flask, json, request
from flask_cors import CORS


from data.DataLayer import DataLayer
from Student import Student


app = Flask(__name__)
CORS(app)

data_layer = DataLayer()
# print(data_layer.students_dict)
# students_dic = {}


# @app.before_first_request
# def before_first_request():
#     students_dic.update(data_layer.load_all_students())


# ------------------------------------- GET ROUTS ---------------------------------------- #


# @app.route('/students')
# def get_all_students():
#     return data_layer.receive_all_students()


@app.route('/students')
def get_all_students():
    students = data_layer.get_all_students()
    print("this is from api:", students)
    response = app.response_class(response=json.dumps(students))
    return response


# @app.route('/students/<email>')
# def get_student_by_email(email):
#     return data_layer.get_student_by_email(email)


@app.route('/students/date')
def get_students_per_date():
    pass
    # requested_date = request.args.get('date')
    # students_added_by_date = {}
    #
    # for key, value in students_dic.items():
    #     if type(value) is dict:
    #         for k, v in value.items():
    #             if v == requested_date:
    #                 students_added_by_date.update(value)
    #
    # response = app.response_class(
    #     response=json.dumps(students_added_by_date),
    #     status=200,
    #     mimetype='application/json')
    # return response


@app.route('/skills')
# get count of desired skills (how many of the students desire a specific skill)
def get_skills_count():
    pass


@app.route('/skills/students')
# get count for how many students have each type of skill
def get_student_by_skill():
    pass


# ------------------------------------- POST/PUT/DELETE ROUTS ---------------------------------------- #


@app.route('/students', methods=['POST'])
# request which will be invoked by admin
# the route will receive a json with the student fields
def add_student():
    student_details = request.json
    # do validations - ???.do_validations(student_details)
    new_student = Student.from_json(student_details)
    data_layer.add_student(new_student)
    # data_layer.persist_students()
    return student_details


@app.route('/students/login', methods=['POST'])
# login a student(email + password) - the route will receive a json with the login and password
def login_student():
    account_data = request.json
    # do validations
    students_account = data_layer.get_student_by_email(account_data['email'])

    response = app.response_class(
        response=json.dumps(students_account),
        status=200,
        mimetype='application/json')
    return response


@app.route('/students/edit', methods=['PUT'])
# the route will receive a json with the student fields
def edit_student():
    pass
    # new_student_info = request.json
    # for student in students_dic:
    #     if student.email == new_student_info['email']:
    #         updated_profile = Student.from_json(new_student_info)
    #         student.updated = datetime.datetime.now()

    # to be continued


@app.route('/students', methods=['DELETE'])
def delete_student():
    to_delete = request.json
    print(to_delete)
    # do validations
    data_layer.remove_student(to_delete)
    return f"Student with login {to_delete} deleted successfully"


if __name__ == "__main__":
    app.run()
