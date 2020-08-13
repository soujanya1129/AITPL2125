import mysql.connector
con = mysql.connector.connect(host = '18.219.99.141', database = 'db1', user = 'root', password = 'India12345')
c = con.cursor()
def create_table():
    c.execute("create table emp_soujanya(emp_id varchar(10), emp_name varchar(20), salary int)")

def insert_table():
    c.execute("insert into emp_soujanya values('AITPL1','soujanya',25000)")
    c.execute("insert into emp_soujanya values('AITPL2','sanjana',45000)")
    c.execute("insert into emp_soujanya values('AITPL3','soumya',55000)")
    c.execute("insert into emp_soujanya values('AITPL4','sonu',85000)")
    c.execute("insert into emp_soujanya values('AITPL5','souju',95000)")

    con.commit()

def delete_table():
    c.execute("delete from emp_soujanya where emp_name='souju'")
    con.commit()

def update_table():
    c.execute("update emp_soujanya set salary=100000 where emp_name='sonu'")
def select_table():
    c.execute("select * from emp_soujanya")
    data = c.fetchall()
    for row in data:
        print(row)

#create_table()
#insert_table()
delete_table()
update_table()
select_table()
c.close()
con.close()