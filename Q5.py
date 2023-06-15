import pymysql

conn = pymysql.connect(
    host='140.127.74.226',
    user='411031106',
    password='411031106',
    db='411031106',
    port=3306
)

try:
    cursor = conn.cursor()
    sql_select = """
    SELECT *
    FROM transport_table
    WHERE ID = '123456' AND status = 'destroyed'
    """
    cursor.execute(sql_select)
    old_data = cursor.fetchone()
    print(old_data)
    if old_data:
        new_id = 105
        new_status = "access"
        new_data = {
            'id': new_id,
            'arrive_time': old_data[1],
            'promise_time': old_data[2],
            'status': new_status,
            'user_name': old_data[4],
            
        }

        sql_insert = """
        INSERT INTO transport_table (id,arrive_time,promise_time,status,user_name)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insert, (new_data['id'], new_data['arrive_time'],new_data['promise_time'],new_data['status'],new_data['user_name']))
        conn.commit()
        print("已創建新的資料，ID: ", new_id)
    else:
        print("未找到符合條件的包裹內容")

finally:
    cursor.close()
    conn.close()
