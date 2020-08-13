import mysql.connector
con = mysql.connector.connect(host = '18.219.99.141', database = 'db1', user = 'root', password = 'India12345')
c = con.cursor()
def create_table():
    c.execute("create table product_soujanya (prod_id int,prod_name varchar(10),prod_des varchar(20),prod_price int)")

def insert_table():
    c.execute("insert into product_soujanya values(212,'lakme','cream',100)")
    c.execute("insert into product_soujanya values(213,'nyka','matte cream',200)")
    c.execute("insert into product_soujanya values(214,'loreal','shampoo',300)")
    c.execute("insert into product_soujanya values(215,'purple','face cream',400)")
    c.execute("insert into product_soujanya values(216,'mac','foundation',500)")

    con.commit()
def delete_table():
    c.execute("delete from product_soujanya where prod_name='purple'")
    con.commit()

def update_table():
    c.execute("update product_soujanya set prod_price=1000 where prod_name='mac'")
def select_table():
    c.execute("select * from product_soujanya")
    data = c.fetchall()
    for row in data:
        print(row)

create_table()
insert_table()
#delete_table()
#update_table()
select_table()
c.close()
con.close()