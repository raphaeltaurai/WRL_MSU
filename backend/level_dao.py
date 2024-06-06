from sql_connection import get_sql_connection

def get_all_levels(connection):
    cursor = connection.cursor()
    query = ("SELECT level.level_id, level.level_code FROM level")
    cursor.execute(query)
    response = []
    for (level_id, level_code) in cursor:
        response.append({
            'level_id': level_id,
            'level_code': level_code
        })
    return response

def insert_new_level(connection, level):
    cursor = connection.cursor()
    query = ("INSERT INTO level "
             "(level_id, level_code) "
             "VALUES (%s, %s)")
    data = (level['level_id'], level['level_code'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_level(connection, level_id):
    cursor = connection.cursor()
    query = ("DELETE FROM level WHERE level_id=%s")
    cursor.execute(query, (level_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_levels(connection))
    # print(insert_new_level(connection, {
    #     'level_id': 1,
    #     'level_code': 'L1'
    # }))
    # print(delete_level(connection, 1))
