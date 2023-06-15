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
    sql = """
    SELECT *
    FROM transport_table
    WHERE arrive_time > promise_time
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("包裹編號:", result[0])
            print("實際到達時間:", result[1])
            print("承諾到達時間:", result[2])
    else:
        print("未找到未按時送達的包裹")

finally:
    cursor.close()
    conn.close()
