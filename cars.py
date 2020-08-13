import mysql.connector
con = mysql.connector.connect(host = '18.219.99.141', database = 'db1', user = 'root', password = 'India12345')
c = con.cursor()
def create_table():
    c.execute("create table car_soujanya (modelnumber int, manu_date date, car_name varchar(10),price int)")

def insert_table():
    c.execute("insert into car_soujanya values(212,'2015-06-19','zudio',100000)")
    c.execute("insert into car_soujanya values(213,'2016-07-20','ludio',200000)")
    c.execute("insert into car_soujanya values(214,'2017-08-21','mudio',300000)")
    c.execute("insert into car_soujanya values(215,'2018-09-22','rudio',400000)")
    c.execute("insert into car_soujanya values(216,'2019-10-28','sudio',500000)")

    con.commit()
def delete_table():
    c.execute("delete from car_soujanya where car_name='zudio'")
    con.commit()

def update_table():
    c.execute("update car_soujanya set price=100000 where car_name='sudio'")
def select_table():
    c.execute("select * from car_soujanya")
    data = c.fetchall()
    for row in data:
        print(row)

#create_table()
insert_table()
#delete_table()
#update_table()
select_table()
c.close()
con.close()