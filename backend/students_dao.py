from sql_connection import get_sql_connection

def get_all_students(connection):
    cursor = connection.cursor()
    query = ("SELECT student.student_id, student.student_fname, student.student_lname, student.reg_number, "
             "student.student_phone, student.student_email, "
             "student.department_id, department.dep_name, "
             "student.campus_id, campus.campus_name, "
             "student.program_id, program.prog_name, "
             "student.level_id, level.level_code, "
             "student.company_id, company.comp_name, "
             "student.supervisor_id, supervisor.sup_fname, supervisor.sup_lname "
             "FROM student "
             "INNER JOIN department ON student.department_id = department.department_id "
             "INNER JOIN campus ON student.campus_id = campus.campus_id "
             "INNER JOIN program ON student.program_id = program.program_id "
             "INNER JOIN level ON student.level_id = level.level_id "
             "LEFT JOIN company ON student.company_id = company.company_id "
             "LEFT JOIN supervisor ON student.supervisor_id = supervisor.supervisor_id")
    cursor.execute(query)
    response = []
    for (student_id, student_fname, student_lname, reg_number, student_phone, student_email,
         department_id, dep_name, campus_id, campus_name, program_id, prog_name,
         level_id, level_code, company_id, comp_name, supervisor_id, sup_fname, sup_lname) in cursor:
        response.append({
            'student_id': student_id,
            'student_fname': student_fname,
            'student_lname': student_lname,
            'reg_number': reg_number,
            'student_phone': student_phone,
            'student_email': student_email,
            'department_id': department_id,
            'dep_name': dep_name,
            'campus_id': campus_id,
            'campus_name': campus_name,
            'program_id': program_id,
            'prog_name': prog_name,
            'level_id': level_id,
            'level_code': level_code,
            'company_id': company_id,
            'comp_name': comp_name,
            'supervisor_id': supervisor_id,
            'supervisor_name': f"{sup_fname} {sup_lname}" if sup_fname and sup_lname else None
        })
    return response

def insert_new_student(connection, student):
    cursor = connection.cursor()
    query = ("INSERT INTO student "
             "(student_fname, student_lname, reg_number, student_phone, student_email, "
             "department_id, campus_id, program_id, level_id, company_id, supervisor_id) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data = (student['student_fname'], student['student_lname'], student['reg_number'],
            student['student_phone'], student['student_email'], student['department_id'],
            student['campus_id'], student['program_id'], student['level_id'],
            student['company_id'], student['supervisor_id'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_student(connection, student_id):
    cursor = connection.cursor()
    query = ("DELETE FROM student WHERE student_id=%s")
    cursor.execute(query, (student_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_students(connection))
    # print(insert_new_student(connection, {
    #     'student_fname': 'John',
    #     'student_lname': 'Doe',
    #     'reg_number': '12345',
    #     'student_phone': 987654321,
    #     'student_email': 'john.doe@example.com',
    #     'department_id': 1,
    #     'campus_id': 1,
    #     'program_id': 1,
    #     'level_id': 1,
    #     'company_id': 1,
    #     'supervisor_id': 1
    # }))
    # print(delete_student(connection, 1))
