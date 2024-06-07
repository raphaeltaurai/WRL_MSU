from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import json

import campus_dao
import city_dao
import company_dao
import department_dao
import level_dao
import program_dao
import students_dao
import supervisor_dao

app = Flask(__name__)

connection = get_sql_connection()


@app.route('/getCampuses', methods=['GET'])
def get_campuses():
    response = campus_dao.get_all_campuses(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getCities', methods=['GET'])
def get_cities():
    response = city_dao.get_all_cities(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getCompanies', methods=['GET'])
def get_companies():
    response = company_dao.get_all_companies(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getDepartments', methods=['GET'])
def get_departments():
    response = department_dao.get_all_departments(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getLevels', methods=['GET'])
def get_levels():
    response = level_dao.get_all_levels(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getPrograms', methods=['GET'])
def get_programs():
    response = program_dao.get_all_programs(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getStudents', methods=['GET'])
def get_students():
    response = students_dao.get_all_students(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getSupervisors', methods=['GET'])
def get_supervisors():
    response = supervisor_dao.get_all_supervisors(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getSupervisorDepartments', methods=['GET'])
def get_supervisor_departments():
    supervisor_id = request.args.get('supervisor_id')
    response = supervisor_dao.get_supervisor_departments(connection, supervisor_id)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/assignDepartmentToSupervisor', methods=['POST'])
def assign_department_to_supervisor():
    request_payload = json.loads(request.form['data'])
    supervisor_id = request_payload['supervisor_id']
    department_id = request_payload['department_id']
    supervisor_dao.assign_department_to_supervisor(connection, supervisor_id, department_id)
    response = jsonify({
        'message': 'Department assigned to supervisor successfully.'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertSupervisor', methods=['POST'])
def insert_supervisor():
    request_payload = json.loads(request.form['data'])
    supervisor_id = supervisor_dao.insert_new_supervisor(connection, request_payload)
    response = jsonify({
        'supervisor_id': supervisor_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertStudent', methods=['POST'])
def insert_student():
    request_payload = json.loads(request.form['data'])
    student_id = students_dao.insert_new_student(connection, request_payload)
    response = jsonify({
        'student_id': student_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProgram', methods=['POST'])
def insert_program():
    request_payload = json.loads(request.form['data'])
    program_id = program_dao.insert_new_program(connection, request_payload)
    response = jsonify({
        'program_id': program_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertLevel', methods=['POST'])
def insert_level():
    request_payload = json.loads(request.form['data'])
    level_id = level_dao.insert_new_level(connection, request_payload)
    response = jsonify({
        'level_id': level_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertCampus', methods=['POST'])
def insert_campus():
    request_payload = json.loads(request.form['data'])
    campus_id = campus_dao.insert_new_campus(connection, request_payload)
    response = jsonify({
        'campus_id': campus_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertCity', methods=['POST'])
def insert_city():
    request_payload = json.loads(request.form['data'])
    city_id = city_dao.insert_new_city(connection, request_payload)
    response = jsonify({
        'city_id': city_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertCompany', methods=['POST'])
def insert_company():
    request_payload = json.loads(request.form['data'])
    company_id = company_dao.insert_new_company(connection, request_payload)
    response = jsonify({
        'company_id': company_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertDepartment', methods=['POST'])
def insert_department():
    request_payload = json.loads(request.form['data'])
    department_id = department_dao.insert_new_department(connection, request_payload)
    response = jsonify({
        'department_id': department_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProgram', methods=['POST'])
def delete_program():
    program_id = request.form['program_id']
    return_id = program_dao.delete_program(connection, program_id)
    response = jsonify({
        'program_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteDepartment', methods=['POST'])
def delete_department():
    department_id = request.form['department_id']
    return_id = department_dao.delete_department(connection, department_id)
    response = jsonify({
        'department_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteLevel', methods=['POST'])
def delete_level():
    level_id = request.form['level_id']
    return_id = level_dao.delete_level(connection, level_id)
    response = jsonify({
        'level_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/removeDepartmentFromSupervisor', methods=['POST'])
def remove_department_from_supervisor():
    request_payload = json.loads(request.form['data'])
    supervisor_id = request_payload['supervisor_id']
    department_id = request_payload['department_id']
    supervisor_dao.remove_department_from_supervisor(connection, supervisor_id, department_id)
    response = jsonify({
        'message': 'Department removed from supervisor successfully.'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getLecturersInDepartment', methods=['GET'])
def get_lecturers_in_department():
    department_id = request.args.get('department_id')
    response = supervisor_dao.get_lecturers_in_department(connection, department_id)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Work Related Learning System")
    app.run(port=5000)
