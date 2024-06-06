from sql_connection import get_sql_connection

def get_all_programs(connection):
    cursor = connection.cursor()
    query = ("SELECT program.program_id, program.prog_code, program.prog_name FROM program")
    cursor.execute(query)
    response = []
    for (program_id, prog_code, prog_name) in cursor:
        response.append({
            'program_id': program_id,
            'prog_code': prog_code,
            'prog_name': prog_name
        })
    return response

def insert_new_program(connection, program):
    cursor = connection.cursor()
    query = ("INSERT INTO program "
             "(prog_code, prog_name) "
             "VALUES (%s, %s)")
    data = (program['prog_code'], program['prog_name'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_program(connection, program_id):
    cursor = connection.cursor()
    query = ("DELETE FROM program WHERE program_id=%s")
    cursor.execute(query, (program_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_programs(connection))
    # print(insert_new_program(connection, {
    #     'prog_code': 'CS101',
    #     'prog_name': 'Computer Science'
    # }))
    # print(delete_program(connection, 1))
