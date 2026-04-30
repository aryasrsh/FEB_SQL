import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Arya@1120', database='feb', port=3306)

cur = conn.cursor()

# sql = "create table emp(id int primary key, name varchar(20), salary int)"  

# sql = "insert into emp values(101, 'Anu', 30000)"             # close commands after each query or change the name
# sql = "insert into emp values(102, 'Sam', 22000)"
# sql = "insert into emp values(203, 'Farheen', 16500)"
# sql = "insert into emp values(538, 'Neha', 65000)"

sql = "select * from emp"

cur.execute(sql)

# row = cur.fetchall()             # to fetch all rows

# # row = cur.fetchone()            # fetch only the 1st row
# # print(row)          # gets in tuple form
 
# for i in row:
#     print(i[0],i[1],i[2])              # to get in table form - indexing


# row = cur.fetchmany(2)     # whatever value we give it displays that much
# print(row)

# for i in row:
#     print(i[0],i[1],i[2])       # just gives 2 values


conn.commit()
conn.close()

