pswd=input("Enter the password of mysql server : ")
import time
import mysql.connector as mysql
import dbcreator
dbcreator.dbcr(pswd)
mycon=mysql.connect(host="localhost",user="root",passwd=pswd,database="STUDENTS")
crsr=mycon.cursor()
#-------------------------FUNCTIONS---------------------------
def clear_screen():
    print("\n"*50)

def loading_screen(stringg,timee):
    for i in range(100):
            print("\n"*50+stringg)
            print("-"*i+str(i+1)+"%")
            time.sleep(timee)
        
def count_record():
    crsr.execute("SELECT * FROM STUDENTS ;")
    data=crsr.fetchall()
    return len(data)

def insert_data():
    clear_screen()
    Adm_no=count_record()+1
    Student_name=input("Enter name of the student : ")
    Student_class=input("Enter class of student in numbers : ")
    Father_name=input("Enter the name of student's father : ")
    Mother_name=input("Enter the name of student's mother : ")
    Phone_number=input("Enter phone number : ")
    Email=input("Enter Email (Optional) : ")
    sql_qry="INSERT INTO STUDENTS VALUES("+str(Adm_no)+",'"+Student_name+"','"+Student_class+"','"+Father_name+"','"+Mother_name+"','"+Phone_number+"','"+Email+"');"
    # print(sql_qry)
    crsr.execute(sql_qry)
    mycon.commit()
    ch=input("Enter y to add more else any to exit to main menu : ")
    if ch=="y" or ch=="Y":
        insert_data( )

def edit_data():
    Adm_no=int(input("Enter the admission number whose record is to be changed : "))
    if Adm_no in range(1,count_record()):
        loading_screen("Clearing Existing data ...",0.03)
        print("Old data cleared ")        
        print("Now Enter new data : ")
        Student_name=input("Enter name of the student : ")
        Student_class=input("Enter class of student in numbers : ")
        Father_name=input("Enter the name of student's father : ")
        Mother_name=input("Enter the name of student's mother : ")
        Phone_number=input("Enter phone number : ")
        Email=input("Enter Email (Optional) : ")
        sql_qry=f'UPDATE STUDENTS SET NAME="{Student_name}",CLASS="{Student_class}",FATHER_NAME="{Father_name}",MOTHER_NAME="{Mother_name}",PhoneNo="{Phone_number}",Email="{Email}" WHERE ADMISSION_NUMBER={Adm_no};'
        # print(sql_qry)
        crsr.execute(sql_qry)
        mycon.commit()
        ch=input("Enter y to edit more else any to exit to main menu : ")
        if ch=="y" or ch=="Y":
            edit_data()

        print("\n"*50+"Data edited !!")
        input("Press Enter to continue...")
    else:
        loading_screen("Searching in database...", 0.01)
        print("\n"*60+"The Admission number you entered is incorrect !!")
        edit_data()
        

def remove_data():
    Adm_no=int(input("Enter the admission number of the student : "))
    if Adm_no in range(1,count_record()+1):
        loading_screen("Deleting Data...", 0.01)
        qry="DELETE FROM STUDENTS WHERE ADMISSION_NUMBER="+str(Adm_no)+" ;"
        print(qry)
        crsr.execute(qry)
        mycon.commit()
        
    else:
        loading_screen("searching record in database...", 0.001)
        print("Record not found !!\nTry again...")
        input("Press enter to continue...")
        clear_screen()
        remove_data( )

def view_data():
    clear_screen()
    Adm_no=int(input("Enter the admission number of the students : "))
    if Adm_no in range(1,count_record()):
        loading_screen("Fetching data...", 0.02)
        crsr.execute("SELECT * FROM STUDENTS WHERE ADMISSION_NUMBER="+str(Adm_no)+" ;")
        data=crsr.fetchall()
        for i in data:
            print(i)
        input("\n"*3+"Press Enter to continue...")
    else:
        loading_screen("Searching record in database...", 0.02)
        clear_screen()
        print("Data not found !!\ntry again...")
        input("Press Enter to continue...")
        view_data( )

def all_data( ):
    clear_screen()
    loading_screen("Fetching all existing recoards...", 0.03)
    crsr.execute("SELECT * FROM STUDENTS ;")
    data=crsr.fetchall()
    for i in data:
        print(i)
    input("Press Enter to go back to main menu...")

def main_menu():
    clear_screen()
    no_of_students=count_record()
    print(f"Total no. of records : {no_of_students }")
    print("\n"*4)
    print("Enter 1 to add new record ")
    print("Enter 2 edit any record ")
    print("Enter 3 delete any record ")
    print("Enter 4 view any record  ")
    print("Enter 5 to view all records present in the database ")
    print("Enter EXIT to exit the program ")
    ch=input("\n>>> ")
    if ch=='1':
        insert_data()
    elif ch=='3':
        remove_data()
    elif ch=='2':
        edit_data()
    elif ch=='4':
        view_data()
    elif ch=='5':
        all_data()
    elif ch=='EXIT' or ch=='exit':
        time.sleep(0.5)
        print("See you later ")
        time.sleep(0.45)
        print("Bye :)")
        exit()
    main_menu( )
    


#-------------------------CONTROL_FLOW--------------------------
if __name__=="__main__":
    clear_screen()
    main_menu()
