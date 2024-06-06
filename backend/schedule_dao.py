from sql_connection import get_sql_connection

def get_all_schedules(connection):
    cursor = connection.cursor()
    query = ("SELECT scheduling.scheduling_id, scheduling.sched_date, "
             "scheduling.city_id, city.city_name, "
             "scheduling.company_id, company.comp_name, "
             "scheduling.supervisor_id, supervisor.sup_fname, supervisor.sup_lname, "
             "scheduling.department_id, department.dep_name "
             "FROM scheduling "
             "INNER JOIN city ON scheduling.city_id = city.city_id "
             "INNER JOIN company ON scheduling.company_id = company.company_id "
             "INNER JOIN supervisor ON scheduling.supervisor_id = supervisor.supervisor_id "
             "INNER JOIN department ON scheduling.department_id = department.department_id")
    cursor.execute(query)
    response = []
    for (scheduling_id, sched_date, city_id, city_name, company_id, comp_name, 
         supervisor_id, sup_fname, sup_lname, department_id, dep_name) in cursor:
        response.append({
            'scheduling_id': scheduling_id,
            'sched_date': sched_date,
            'city_id': city_id,
            'city_name': city_name,
            'company_id': company_id,
            'comp_name': comp_name,
            'supervisor_id': supervisor_id,
            'supervisor_name': f"{sup_fname} {sup_lname}",
            'department_id': department_id,
            'dept_name': dep_name
        })
    return response

def insert_new_schedule(connection, schedule):
    cursor = connection.cursor()
    query = ("INSERT INTO scheduling "
             "(sched_date, city_id, company_id, supervisor_id, department_id) "
             "VALUES (%s, %s, %s, %s, %s)")
    data = (schedule['sched_date'], schedule['city_id'], schedule['company_id'], 
            schedule['supervisor_id'], schedule['department_id'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_schedule(connection, scheduling_id):
    cursor = connection.cursor()
    query = ("DELETE FROM scheduling WHERE scheduling_id=%s")
    cursor.execute(query, (scheduling_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Example usage:
    print(get_all_schedules(connection))
    # print(insert_new_schedule(connection, {
    #     'sched_date': '2023-01-01', 
    #     'city_id': 1, 
    #     'company_id': 1, 
    #     'supervisor_id': 1, 
    #     'department_id': 1
    # }))
    # print(delete_schedule(connection, 1))
