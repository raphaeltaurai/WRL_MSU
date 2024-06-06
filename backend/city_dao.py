from sql_connection import get_sql_connection

def get_all_cities(connection):
    cursor = connection.cursor()
    query = ("SELECT city.city_id, city.city_name FROM city")
    cursor.execute(query)
    response = []
    for (city_id, city_name) in cursor:
        response.append({
            'city_id': city_id,
            'city_name': city_name
        })
    return response

def insert_new_city(connection, city):
    cursor = connection.cursor()
    query = ("INSERT INTO city "
             "(city_name) "
             "VALUES (%s)")
    data = (city['city_name'],)

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_city(connection, city_id):
    cursor = connection.cursor()
    query = ("DELETE FROM city WHERE city_id=%s")
    cursor.execute(query, (city_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    #print(get_all_cities(connection))
    # print(insert_new_city(connection, {'city_name': 'New York'}))
    #print(delete_city(connection, 4))
