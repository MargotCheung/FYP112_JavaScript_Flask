import pymysql

connection = pymysql.connect(
    host='localhost',
    user='flask',
    password='password',
    db='courselist',
    charset='utf8',
)

cursor = connection.cursor()