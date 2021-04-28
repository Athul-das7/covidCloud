import mysql.connector as sql  # sql its like a language... mysql ki sever creation...
# mysql-connector-python

# mysql ... php mysql queries => py through use chestham.

db = sql.connect(
    host="localhost", # 127.0.0.0 #
    user="root",
    passwd="athul",
    database="student_list"
)
rn = "1602-19-735-064"
cur = db.cursor()

cur.execute('''SELECT *  FROM student_list
WHERE roll_no = "1602-19-735-064" ''' #.format(rn))
rows = cur.fetchall()
for r in rows:
    print(r)

db.close()