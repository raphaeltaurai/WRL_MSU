from sql_connection import get_sql_connection

def get_all_companies(connection):
    cursor = connection.cursor()
    query = ("SELECT company.company_id, company.comp_name, company.comp_country, company.comp_phone, "
             "company.comp_email, company.comp_startdate, company.city_id, city.city_name "
             "FROM company "
             "INNER JOIN city ON company.city_id = city.city_id")
    cursor.execute(query)
    response = []
    for (company_id, comp_name, comp_country, comp_phone, comp_email, comp_startdate, city_id, city_name) in cursor:
        response.append({
            'company_id': company_id,
            'comp_name': comp_name,
            'comp_country': comp_country,
            'comp_phone': comp_phone,
            'comp_email': comp_email,
            'comp_startdate': comp_startdate,
            'city_id': city_id,
            'city_name': city_name
        })
    return response

def insert_new_company(connection, company):
    cursor = connection.cursor()
    query = ("INSERT INTO company "
             "(comp_name, comp_country, comp_phone, comp_email, comp_startdate, city_id) "
             "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (company['comp_name'], company['comp_country'], company['comp_phone'],
            company['comp_email'], company['comp_startdate'], company['city_id'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_company(connection, company_id, city_id):
    cursor = connection.cursor()
    query = ("DELETE FROM company WHERE company_id=%s AND city_id=%s")
    cursor.execute(query, (company_id, city_id))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_companies(connection))
    # print(insert_new_company(connection, {
    #     'comp_name': 'Tech Solutions',
    #     'comp_country': 'USA',
    #     'comp_phone': 1234567890,
    #     'comp_email': 'info@techsolutions.com',
    #     'comp_startdate': '2022-01-01',
    #     'city_id': 1
    # }))
    #print(delete_company(connection, 1, 1))
