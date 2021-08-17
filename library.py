
import pymysql
import datetime
import pymysql
import datetime
class inportlog:  
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password    
    def inport(self):

        try:
            con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
            cur = con.cursor()
            today=datetime.datetime.today()
            
            sql1 = 'SELECT * from employees where employee_id={}'.format(id)
            #sql = 'SELECT status from book where id ={} '.format(book_id)
            cur.execute(sql1)
            res=cur.fetchall()
            for i in res:
                for j in res:
                    if j[1]==name and j[2]==password:
                        a=j
                        print("Credisencials passed successfully")
                        print("WELLCOM TO THE LIBRAY")

                        #sql=("iNSERT into transaction(b_id, m_id, doi) values({},{},'{}')".format(book_id,mem_id,today))
                        sql=("Insert into emplogs(employee_id,Ename,Epassword,dtin) values ({},'{}','{}','{}')".format(id,name,password,today))
                        cur.execute(sql)
                        sql1='select max(trnid) from emplogs'
                        cur.execute(sql1)
                        records = cur.fetchone()
                        for record in records:
                            print("your  resent login  tansaction id is:",record)
                        return "good"
           
                    else:
                        print("Credisencials failled to match")
            
        except:
            print("please provide valid info")

        finally:
            con.commit()
            con.close()
        
id=int(input("Enter your employee id:"))
name=input("Enter your name as same as mentioned in joining form:")
password=input("Enter your login password for login:")
#a=inportlog(id,name,password)
#a.inport()
#################################################################################
a=inportlog(id,name,password)
res=a.inport()
if res=="good":
 def add_book():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
  
    id_title = input('Enter Book Title :')
    id_author = input('Enter Book Author : ')
    id_publisher =input('Enter Book Publisher : ')
    id_pages = int(input('Enter Book Pages : '))
    id_price = float(input('Enter Book Price : '))
    id_edition = input('Enter Book Edition : ')
    c=int(input("Enter no of copyes: "))
    #sql = ("insert into book(ititle,author,price,pages,publisher,edition,status) values ({},'{}','{}','{}',{},{},'{}','available')".format(id_id,id_title,id_author,id_price,id_pages,id_publisher,id_edition))
    sql=("Insert into book(title,author,publisher,price,pages,edition,status) values ('{}','{}','{}',{},{},'{}','available')".format(id_title,id_author,id_publisher,id_price,id_pages,id_edition))

    for i in range(1,c+1):
        cur.execute(sql)
        print('New Book added successfully:',i)
        con.commit()
    con.close()
    wait =input('\n\n\n Press any key to continue....')
    print('All Books added successfully')
     #add=add_book(
###########################################################################################
 
 def add_member():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()

    id_name = input('Enter Member Name :')
    id_standard = input('Enter Member Class & Section : ') 
    id_address =input('Enter Member Address : ')
    id_phone = input('Enter Member Phone  : ')
    id_email = input('Enter Member Email  : ')
  #cur.execute("create table member(id int(11) primary key,name char(30) DEFAULT NULL,standard char(15) DEFAULT NULL, address char(100) DEFAULT NULL,phone char(15) DEFAULT NULL,email char(60) DEFAULT NULL)")
    sql = ("insert into member(name,standard,address,phone,email,Book_issued) values ('{}','{}','{}','{}','{}',0)".format(id_name,id_standard,id_address,id_phone,id_email))
    cur.execute(sql)
    #print('New Book added successfully')
    con.commit()
    con.close()

 #add=add_member()
    print('New Member added successfully')
    wait = input('\n\n\n Press any key to continue....')
#############################################################################################
 def modify_book():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
   
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n6. Book Edition')
    print('\n')
    choice = int(input('Enter your choice :'))
    field =" "
    if choice == 1:
        field = 'title'
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    if choice==6:
        field='edition'

    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    if field =='pages' or field == 'price':
        sql ="UPDATE book set {} = {} where id ={}".format(field,value,book_id)

    else:
        sql ="UPDATE book set  {}  = '{}' where id ={}".format(field,value,book_id)
    #print(sql)
    cur.execute(sql)
    con.commit()
    print('Book details Updated.....')
    con.close()
 #memb=modify_book()
###############################################################################################
 def modify_member():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n')
    choice = int(input('Enter your choice :'))

    field =" "
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    #print("The option you selected is:",field)
    mem_id =input('Enter member ID :')
    value = input('Enter new value :')
    sql = "UPDATE member set  {}='{}' where id ={}".format(field,value,mem_id)
    #print(sql)
    cur.execute(sql)
    con.commit()
    print('Member details Updated.....')
    con.close()
    wait = input('\n\n\n Press any key to continue....')
 #mem=modify_member()
##########################################################################################

 def mem_issue_status(mem_id):
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    sql ='SELECT Book_issued from member where id="{}" '.format(mem_id)
    #print(sql)
    cur.execute(sql)
    con.commit()
    results = cur.fetchall()
    for i in results:
     for j in i:
      return int(j)
      #print(j)

 #mem=int(input("enter member id:"))  
 #m=mem_issue_status(mem)

 def book_status(book_id):
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    sql = 'SELECT status from book where id ={} '.format(book_id)
    cur.execute(sql)
    con.commit()
    result = cur.fetchone()
    return result
    print(result)
#m=book_status(1005)
#print(m)

 def book_issue_status(book_id,mem_id):
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    sql = 'SELECT * from transactions where b_id ={} AND m_id ={}'.format(book_id,mem_id)
    cur.execute(sql)
    con.commit()
    result = cur.fetchone()
    return result
    #print(result)
    con.close()
 #m=book_issue_status(1005,5)

#print(book_issue_status(1002,2))
###############################################################################
 def issue_book():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    
    print('\n BOOK ISSUE SCREEN ')
    print('-'*80)
    book_id = input('Enter Book  ID : ')
    mem_id  = input('Enter Member ID :')
    
    today=datetime.datetime.today()
    #print(today)
    result =list(book_status(book_id))
    result1 = mem_issue_status(mem_id)
    
    #print(result)
    print(result1)
    if result1 <=5:
     if result ==['available']:
        #sql=("insert into book(title,author,publisher,price,pages,edition,status) values ('{}','{}','{}',{},{},'{}','available')".format(id_title,id_author,id_publisher,id_price,id_pages,id_edition))
        sql=("iNSERT into transactions(b_id, m_id, doi) values({},{},'{}')".format(book_id,mem_id,today))
        cur.execute(sql)
        con.commit()
       # sql = "UPDATE member set  {}='{}' where id ={}".format(field,value,mem_id)
        sql = "UPDATE book set status='issued' where id ={}".format(book_id)
        sql1 = "UPDATE member set Book_issued=Book_issued+1 where id ={}".format(mem_id)
        cur.execute(sql)
        cur.execute(sql1)
        con.commit()
        print('Book issued successfully')
     else:
          print('Book is not available for ISSUE...' )
    else:
      print(" you already collected max no of boom please return a collected book")
    wait =input('\n\n\n Press any key to continue....')
 #issu=issue_book()
 def return_book():
    fine_per_day =5.0
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
  
    print('\n BOOK RETURN SCREEN ')
    print('-'*80)
    book_id = input('Enter Book  ID : ')
    mem_id = input('Enter Member ID :')
    today =datetime.datetime.today()
    result = book_issue_status(book_id,mem_id)
    if result==None:
       print('Book was not issued...Check Book Id and Member ID again..')
    else:
       sql='update book set status ="available" where id ='+book_id +';'
       din = (today - result[3]).days
       fine = din * fine_per_day    #  fine per data
       sql1 = 'update transactions set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+mem_id+' and dor is NULL;' 
       sql2 = "UPDATE member set Book_issued=Book_issued-1 where id ={}".format(mem_id)
       cur.execute(sql)
       cur.execute(sql1)
       cur.execute(sql2)
       con.commit()
       print('\n\nBook returned successfully')
    con.close()
    wait = input('\n\n\n Press any key to continue....')
 #a=return_book()
##################################################################################
 def search_book(field):
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()


    print('\n BOOK SEARCH SCREEN ')
    print('-'*30)
    msg ="Enter '{}' Value :".format(field)
    title = input(msg)
    sql ='select * from book where '+ field + ' like "%'+ title+'%"'
    cur.execute(sql)
    records = cur.fetchall()
    print('Search Result for :',field,' :' ,title)
    print('-'*30)
    for record in records:
      print(record)
    con.close()
    wait = input('\n\n\n Press any key to continue....')

 def search_menu():
    while True:
      print("-"*30)
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_book(field)
 #m=search_menu()
 def reprot_book_list():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()

    
    print('\n REPORT - BOOK TITLES ')
    print('-'*80)
    sql ='select * from book'
    cur.execute(sql)
    con.commit()
    records = cur.fetchall()
    for record in records:
       print(record)
    con.close()
    wait = input('\n\n\nPress any key to continue.....')
 #r=reprot_book_list()

 def report_issued_books():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - BOOK TITLES - Issued')
    print('-'*80)
    sql = 'select * from book where status = "issued";'
    cur.execute(sql)
    con.commit()
    records = cur.fetchall()
    for record in records:
       print(record)
    con.close()
    wait = input('\n\n\nPress any key to continue.....')
 #ra=report_issued_books()
 def report_available_books():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - BOOK TITLES - Available')
    print('-'*80)
    sql = 'select * from book where status = "available";'
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
       print(record)
    con.commit()
    con.close()
    wait = input('\n\n\nPress any key to continue.....')


 def report_weed_out_books():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - BOOK TITLES - Weed Out')
    print('-'*80)
    sql = 'select * from book where status = "weedout";'
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
       print(record)
    con.commit()
    con.close()
    wait = input('\n\n\nPress any key to continue.....')


 def report_stolen_books():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - BOOK TITLES - Stolen')
    
    print('-'*80)
    sql = 'select * from book where status = "stolen";'
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
       print(record)
    con.commit()
    con.close()
    wait = input('\n\n\nPress any key to continue.....')


 def report_lost_books():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - BOOK TITLES - lost')
    print('-'*80)
    sql = 'select * from book where status = "lost";'
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
       print(record)
    con.commit()
    con.close()
    wait = input('\n\n\nPress any key to continue.....')

 ############################################################################
 def report_member_list():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    print('\n REPORT - Members List ')
    print('-'*80)
    sql = 'select * from member'
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
       print(record)
    con.commit()
    con.close()
    wait = input('\n\n\nPress any key to continue.....')


 def report_fine_collection():
    con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
    cur = con.cursor()
    today=datetime.datetime.today()
    sql ='select sum(fine) from transactions where dor ="'+str(today)+'";'
    cur.execute(sql)
    result = cur.fetchone() #always return values in the form of tuple
   
    print('Fine collection')
    print('-'*80)
    print('Total fine collected Today :',result[0])
    print('\n\n\n')
    con.close()
    wait = input('\n\n\nPress any key to continue.....')


 def report_menu():
    while True:
   
      print(' R E P O R T    M E N U ')
      print("\n1.  Book List")
      print('\n2.  Member List')
      print('\n3.  Issued Books')
      print('\n4.  Available Books')
      print('\n5.  Weed out Book')
      print('\n6.  Stolen Book')
      print('\n7.  Lost Book')
      print('\n8.  Fine Collection')
      print('\n9.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      print("#"*80)

      if choice == 1:
        reprot_book_list()
      if choice == 2:
        report_member_list()
      if choice == 3:
        report_issued_books()
      if choice == 4:
        report_available_books()
      if choice == 5:
        report_weed_out_books()
      if choice == 6:
        report_stolen_books()
      if choice == 7:
        report_lost_books()
      if choice == 8:
        report_fine_collection()
      if choice == 9:
        break

 #report=report_menu()
 def change_book_status():
      
      con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
      cur = con.cursor()   
    
      print(' S P E C I A L     M E N U')
      print("\n1.  Book Stolen")
      print('\n2.  Book Lost')
      print('\n3.  Book Weed out')
      
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      status=''
      if choice == 1:
         status ='stolen'
         fin=1
         mem_id=int(input("Enter employee id:"))
      if choice == 2:
         status = 'lost'
         fin=2
         mem_id=int(input("Enter member id:"))
      if choice == 3:
         status = 'weedout'
         fin=1.5
         mem_id=int(input("Enter member id:"))
      today=datetime.datetime.today()
      book_id = input('Enter book id :')   
      sql ="select price from book where id ={}".format(book_id)
      cur.execute(sql)
      din = cur.fetchone()
      for i in din:
         bin=i
      fine=bin*fin
      print(fine)
      sql1 = "update book set status = '{}' where id ='{}'".format(status,book_id)
      cur.execute(sql1)
      
      #print(fine)  #  fine per data
      #sql = "UPDATE book set status='issued' where id ={}".format(book_id)
      sql1 = "UPDATE transactions set dor ='{}',fine={} where b_id='{}' and m_id='{}'".format(today,fine,book_id,mem_id) 
      sql2 = "UPDATE member set Book_issued=Book_issued-1 where id ={}".format(mem_id)
      
      cur.execute(sql1)
      cur.execute(sql2)
      con.commit()
      print('Book status changed to ',status)
      con.close()
      wait = input('\n\n\nPress any key to continue.....')

 #a=change_book_status()
 def log_out():
      con = pymysql.connect(host='localhost',database='liberary',user='root',password='root')
      cur = con.cursor() 
      today=datetime.datetime.today()
      emp_id = int(input('Enter your employee id to conform:'))
      trn=int(input("Enter your recent login  transaction id:"))
      #sql1 = "UPDATE transactions set dor ='{}',fine={} where b_id='{}' and m_id='{}'".format(today,fine,book_id,mem_id) 
      sql2 = "UPDATE emplogs set dtot='{}' where employee_id ={} and trnid={}".format(today,emp_id,trn)
      cur.execute(sql2)
      con.commit()
      print('logged out Successfully ')
      con.close()
 #l=log_out()
        
 def main_menu():
    while True:
   
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Book Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue Book')
      print('\n6.  Return Book')
      print('\n7.  Search Menu')
      print('\n8.  Report Menu')
      print('\n9.  Special Menu')
      print('\n0.  TO LOG_OUT')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()
      if choice == 9:
        change_book_status()
      if choice == 0:
        log_out()
        break
 m=main_menu()

