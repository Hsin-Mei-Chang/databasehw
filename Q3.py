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
    SELECT in_city, 
           CONCAT_WS(',', 
                      IF(phone_stock = 0, 'phone', NULL), 
                      IF(notebook_stock = 0, 'notebook', NULL), 
                      IF(computer_stock = 0, 'computer', NULL)
           ) AS out_of_stock_products
    FROM commodity_table
    WHERE in_city = 'Kaohsiung'
      AND (phone_stock = 0 OR notebook_stock = 0 OR computer_stock = 0)
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        for result in results:
            print("店家所在縣市:", result[0])
            print("缺貨產品:", result[1])
    else:
        print("Not Found")

finally:
    cursor.close()
    conn.close()
