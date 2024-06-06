from sql_connection import get_sql_connection

def get_all_departments(connection):
    cursor = connection.cursor()
    query = ("SELECT department.department_id, department.dep_code, department.dep_name FROM department")
    cursor.execute(query)
    response = []
    for (department_id, dep_code, dep_name) in cursor:
        response.append({
            'department_id': department_id,
            'dep_code': dep_code,
            'dep_name': dep_name
        })
    return response

def insert_new_department(connection, department):
    cursor = connection.cursor()
    query = ("INSERT INTO department "
             "(dep_code, dep_name) "
             "VALUES (%s, %s)")
    data = (department['dep_code'], department['dep_name'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_department(connection, department_id):
    cursor = connection.cursor()
    query = ("DELETE FROM department WHERE department_id=%s")
    cursor.execute(query, (department_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_departments(connection))
    # print(insert_new_department(connection, {
    #     'dep_code': 'CS101',
    #     'dep_name': 'Computer Science'
    # }))
    # print(delete_department(connection, 1))
