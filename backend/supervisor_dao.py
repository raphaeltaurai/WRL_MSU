from sql_connection import get_sql_connection

def get_all_supervisors(connection):
    cursor = connection.cursor()
    query = ("SELECT supervisor.supervisor_id, supervisor.sup_fname, supervisor.sup_lname, supervisor.staff_id, "
             "supervisor.sup_phone, supervisor.sup_email, supervisor.campus_id, campus.campus_name, "
             "department.department_id, department.dep_name "
             "FROM supervisor "
             "INNER JOIN campus ON supervisor.campus_id = campus.campus_id "
             "LEFT JOIN supervisor_has_department ON supervisor.supervisor_id = supervisor_has_department.supervisor_id "
             "LEFT JOIN department ON supervisor_has_department.department_id = department.department_id")
    cursor.execute(query)
    response = []
    for (supervisor_id, sup_fname, sup_lname, staff_id, sup_phone, sup_email, campus_id, campus_name,
         department_id, dep_name) in cursor:
        response.append({
            'supervisor_id': supervisor_id,
            'sup_fname': sup_fname,
            'sup_lname': sup_lname,
            'staff_id': staff_id,
            'sup_phone': sup_phone,
            'sup_email': sup_email,
            'campus_id': campus_id,
            'campus_name': campus_name,
            'department_id': department_id,
            'dep_name': dep_name
        })
    return response

def insert_new_supervisor(connection, supervisor):
    cursor = connection.cursor()
    query = ("INSERT INTO supervisor "
             "(sup_fname, sup_lname, staff_id, sup_phone, sup_email, campus_id) "
             "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (supervisor['sup_fname'], supervisor['sup_lname'], supervisor['staff_id'],
            supervisor['sup_phone'], supervisor['sup_email'], supervisor['campus_id'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_supervisor(connection, supervisor_id):
    cursor = connection.cursor()
    query = ("DELETE FROM supervisor WHERE supervisor_id=%s")
    cursor.execute(query, (supervisor_id,))
    connection.commit()

    return cursor.lastrowid

def get_supervisor_departments(connection, supervisor_id):
    cursor = connection.cursor()
    query = ("SELECT department.department_id, department.dep_name "
             "FROM supervisor_has_department "
             "INNER JOIN department ON supervisor_has_department.department_id = department.department_id "
             "WHERE supervisor_has_department.supervisor_id = %s")
    cursor.execute(query, (supervisor_id,))
    response = []
    for (department_id, dep_name) in cursor:
        response.append({
            'department_id': department_id,
            'dep_name': dep_name
        })
    return response

def assign_department_to_supervisor(connection, supervisor_id, department_id):
    cursor = connection.cursor()
    query = ("INSERT INTO supervisor_has_department (supervisor_id, department_id) VALUES (%s, %s)")
    cursor.execute(query, (supervisor_id, department_id))
    connection.commit()

def remove_department_from_supervisor(connection, supervisor_id, department_id):
    cursor = connection.cursor()
    query = ("DELETE FROM supervisor_has_department WHERE supervisor_id = %s AND department_id = %s")
    cursor.execute(query, (supervisor_id, department_id))
    connection.commit()

def get_lecturers_in_department(connection, department_id):
    cursor = connection.cursor()
    query = ("SELECT supervisor.supervisor_id, supervisor.sup_fname, supervisor.sup_lname, supervisor.staff_id, "
             "supervisor.sup_phone, supervisor.sup_email, supervisor.campus_id, campus.campus_name "
             "FROM supervisor_has_department "
             "INNER JOIN supervisor ON supervisor_has_department.supervisor_id = supervisor.supervisor_id "
             "INNER JOIN campus ON supervisor.campus_id = campus.campus_id "
             "WHERE supervisor_has_department.department_id = %s")
    cursor.execute(query, (department_id,))
    response = []
    for (supervisor_id, sup_fname, sup_lname, staff_id, sup_phone, sup_email, campus_id, campus_name) in cursor:
        response.append({
            'supervisor_id': supervisor_id,
            'sup_fname': sup_fname,
            'sup_lname': sup_lname,
            'staff_id': staff_id,
            'sup_phone': sup_phone,
            'sup_email': sup_email,
            'campus_id': campus_id,
            'campus_name': campus_name
        })
    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_supervisors(connection))
    # print(insert_new_supervisor(connection, {
    #     'sup_fname': 'Jane',
    #     'sup_lname': 'Doe',
    #     'staff_id': 'ST12345',
    #     'sup_phone': '123456789',
    #     'sup_email': 'jane.doe@example.com',
    #     'campus_id': 1
    # }))
    # print(delete_supervisor(connection, 1))
    # print(get_supervisor_departments(connection, 1))
    # assign_department_to_supervisor(connection, 1, 1)
    # remove_department_from_supervisor(connection, 1, 1)
    # print(get_lecturers_in_department(connection, 1))
