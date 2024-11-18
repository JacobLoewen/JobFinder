import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'JAKE',
    password = '123',
    db = 'dreamhome',
    cursorclass = pymysql.cursors.DictCursor
)

with db.cursor() as cursor:
    cursor.execute('SELECT * FROM branch;')
    result = cursor.fetchall()
    print(result)
