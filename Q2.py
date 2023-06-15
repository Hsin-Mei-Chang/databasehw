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
    SELECT product, sales
    FROM (
        SELECT 'phone' AS product, phone_sales AS sales
        FROM commodity_table
        UNION
        SELECT 'notebook' AS product, notebook_sales AS sales
        FROM commodity_table
        UNION
        SELECT 'computer' AS product, computer_sales AS sales
        FROM commodity_table
    ) AS products
    ORDER BY sales DESC
    LIMIT 2
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("產品:", result[0])
            print("銷售額:", result[1])
    else:
        print("Not Found")

finally:
    cursor.close()
    conn.close()
