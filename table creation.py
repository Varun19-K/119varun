import pymysql
con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
cur = con.cursor()

try:
    cur.execute("create table employees(employee_id int(10) not null AUTO_INCREMENT primary key,Ename char(60) DEFAULT NULL,Epassword char(60) DEFAULT NULL)")
    cur.execute("insert into employees(employee_id,Ename,Epassword) VALUES(101,'surash','PASS1231@'),(102,'SUMA','SUS435@'),(103,'remash','rema54562*')")
        ################
    cur.execute("create table emplogs(trnid int(10) not null AUTO_INCREMENT primary key,employee_id int(10),Ename char(60) DEFAULT NULL,Epassword char(60) DEFAULT NULL,dtin DATETIME DEFAULT NULL,dtot DATETIME DEFAULT NULL)")
    cur.execute("insert into emplogs(trnid,employee_id,Ename,Epassword,dtin,dtot) VALUES(1,101,'surash','PASS1231@','2021-2-1 10:00:30','2021-2-1 05:09:36'),(2,103,'remash','rema54562*','2021-2-5 10:00:30','2021-2-5 05:09:36')")
    #################
        #book table creation
    cur.execute("create table book(id int(10) not null AUTO_INCREMENT primary key,title char(60) DEFAULT NULL,author char(50) DEFAULT NULL,pages int(4) DEFAULT NULL,price float(10,4) DEFAULT NULL,status char(10) DEFAULT NULL,publisher char(60) DEFAULT NULL,edition char(15) DEFAULT NULL)")
    cur.execute("insert into book (id, title, author, pages, price, status, publisher, edition) VALUES(1001, 'Python', 'Varun', 120, 300.00, 'isshued', 'Varun House', 'First Edition'),(1002, 'Python', 'Varun', 120, 300.00, 'available', 'Varun House', 'First Edition')")
        ######################################################################################
        #member table creation
    cur.execute("create table member(id int(11) not null AUTO_INCREMENT primary key,name char(30) DEFAULT NULL,standard char(50) DEFAULT NULL, address char(100) DEFAULT NULL,phone char(15) DEFAULT NULL,email char(60) DEFAULT NULL,Book_isshued int(15) DEFAULT Null)")
    cur.execute("insert into member(id, name, standard, address, phone, email) VALUES (1, 'Rabikiran', '9th standard', 'kingkoti', '9879879879', 'koti@gmail.com',0),(2, 'Rohit', '9th standard', 'bellary', '9879877779', 'rohil@gmail.com',1)")
        ########################################################################################
        #record table creation
    cur.execute("create table transactions(tid int(11) not null AUTO_INCREMENT primary key,b_id int(11) DEFAULT NULL,m_id int(11) DEFAULT NULL,doi DATETIME DEFAULT NULL,dor DATETIME DEFAULT NULL,fine float(10,2) DEFAULT NULL)")
    cur.execute("insert into transactions(tid,b_id,m_id,doi,dor,fine) VALUES (1,1001,2,'2021-2-1 12:06:30','2021-2-5 04:09:36',0)")
    con.commit()    
except:
    print("Table already exist")
finally:
    print("table created successfully")

