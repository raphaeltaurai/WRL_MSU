from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select campus.campus_id, campus.campus_name")
    cursor.execute(query)
    response = []
    for (campus_id, campus_name) in cursor:
        response.append({
            'campus_id': campus_id,
            'campus_name': campus_name
        })
    return response

def insert_new_product(connection, campus):
    cursor = connection.cursor()
    query = ("INSERT INTO campus "
             "(name)"
             "VALUES (%s")
    data = (campus['campus_name'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_campus(connection, campus_id):
    cursor = connection.cursor()
    query = ("DELETE FROM campus where campus_id=" + str(campus_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    #print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoes',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    #     }))
    print(delete_campus(connection, 4))