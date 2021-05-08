import mysql.connector as sql  # sql its like a language... mysql ki sever creation...
# mysql-connector-python

# mysql ... php mysql queries => py through use chestham.

#db = sql.connect(
db=sql.connect(
    host="vce-dbms.ctk43tbzkevt.us-east-1.rds.amazonaws.com",  # 127.0.0.0/ You don't have to change this.
    user="AthulMouni",  # connecting to your user/ if you have different user mention
    passwd="AthulMouni",  # entering the password/ change it to your password
    database="vce_db"  # connecting to the database/ Don't change this
)
#
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