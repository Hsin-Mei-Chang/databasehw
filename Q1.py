import pymysql

conn = pymysql.connect(
    host='140.127.74.226',
    user='411031106',
    password='411031106',
    db='411031106',
    port = 3306
)

try:
    cursor = conn.cursor()
    sql = """
    SELECT user_name, SUM(cost) AS total_cost
    FROM user_table
    GROUP BY user_name
    ORDER BY total_cost DESC
    LIMIT 1
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        print("過去一年買最多的用戶是：",result[0])
        print("Total_cost:", result[1])
    else:
        print("Not Found")

finally:
    cursor.close()
    conn.close()
