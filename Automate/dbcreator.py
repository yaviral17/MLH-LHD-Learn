import mysql.connector as mysql
def dbcr(pswd):
    mycon=mysql.connect(host="localhost",user="root",passwd=pswd)
    crsr=mycon.cursor()
    crsr.execute("DROP DATABASE IF EXISTS STUDENTS;")
    crsr.execute("CREATE DATABASE STUDENTS;")
    mycon.commit()
    crsr.execute("USE STUDENTS;")
    crsr.execute("CREATE TABLE STUDENTS(ADMISSION_NUMBER INT(6) NOT NULL UNIQUE,NAME VARCHAR(30) NOT NULL,CLASS VARCHAR(4) NOT NULL,FATHER_NAME VARCHAR(30) NOT NULL,MOTHER_NAME VARCHAR(30) NOT NULL,PhoneNo VARCHAR(10),Email VARCHAR(40));")
    # for i in range(1,10):
    #     name="N"*i
    #     fname="F"*i
    #     mname="M"*i
    #     no=str(i)*10
    #     email="E"*i+"@gamil.com"
    #     crsr.execute(f"INSERT INTO STUDENTS VALUES({i},'{name}','{12}','{fname}','{mname}','{no}','{email}');")
    #     mycon.commit()
if __name__=="__main__":
    dbcr("toor")