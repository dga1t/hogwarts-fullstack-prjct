from flask import Flask, json, request
from flask_cors import CORS
import atexit

from data.DataLayer import DataLayer
from Student import Student


app = Flask(__name__)
CORS(app)

data_layer = DataLayer()


# ------------------------------------- GET ROUTS ---------------------------------------- #


@app.route('/students')
def get_all_students():
    students = data_layer.get_all_students()
    print("this is from api:", students)
    response = app.response_class(response=json.dumps(students))
    return response


@app.route('/students/<email>')
def get_student_by_email(email):
    student = data_layer.get_student_by_email(email)
    response = app.response_class(response=json.dumps(student))
    return response


@app.route('/students/date')
def get_students_per_date():
    requested_date = request.args.get('date')
    print(requested_date)
    print(type(requested_date))
    students = data_layer.get_students_by_date(requested_date)
    return students


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
    return student_details


@app.route('/students/login', methods=['POST'])
# login a student(email + password) - the route will receive a json with the login and password
def login_admin():
    account_data = request.json
    # do validations
    students_account = data_layer.get_student_by_email(account_data['email'])

    response = app.response_class(
        response=json.dumps(students_account),
        status=200,
        mimetype='application/json')
    return response


# @app.route('/students/edit', methods=['PUT'])
# # the route will receive a json with the student fields
# def edit_student():
#     edited_student = request.json
#     data_layer.edit_student(edited_student)
#     return f"Student {...} edited successfully "


@app.route('/students', methods=['DELETE'])
def delete_student():
    to_delete = request.json
    # do validations
    data_layer.delete_student(to_delete)
    return f"Student with login {to_delete} deleted successfully"


@atexit.register
def byebye():
    data_layer.shutdown()


if __name__ == "__main__":
    app.run()
