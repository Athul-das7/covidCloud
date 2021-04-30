import mysql.connector as sql  # sql its like a language... mysql ki sever creation...
# mysql-connector-python

# mysql ... php mysql queries => py through use chestham.

db = sql.connect(
    host="localhost", # 127.0.0.0
    user="root",        # connecting to your user
    passwd="athul",     # entering the password
    database="vce_studentDB" # connecting to the database
)
rn = "1602-19-735-064"
cur = db.cursor()

cur.execute('''SELECT *  FROM student_list
WHERE roll_no = %s ''',(rn,))
rows = cur.fetchall()
print(type(list(rows[0])))
for r in rows:
    for ele in list(r):
        print(ele)

db.close()