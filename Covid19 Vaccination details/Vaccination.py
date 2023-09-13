import main_file
import datetime
import smtplib
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_db"
)
#*********************************
mycursor=mydb.cursor()
#*********************************
#insert data into db
def insert_data():
    sql="insert into vaccination_details (Name,Age,Gender,Phone_Number,Email_id,Aadhar_Number,City,Vaccine_Dose,Vaccination_Center,Doctor_Name,Date,Time,Day,Month) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print("*********Insert Data*********")
    Name=input("Enter your Full Name:")
    Age=input("Enter your age:")
    Gender=input("Enter your gender:")
    Phone_Number=int(input("Enter your Phone Number:"))
    Email_id=input("Enter your Email Id:")
    Aadhar_Number=int(input("Enter your Aadhar Number:"))
    City=input("Enter your City Name:")
    Vaccine_Dose=input("Enter your vaccination dose (1 or 2):")
    Vaccination_Center=input("Enter the place where you vaccinated:")
    Doctor_Name=input("Enter Doctor Name:")
    x=datetime.datetime.now()
    Date=x.strftime("%d/%m/%Y")
    Time=x.strftime("%H:%M:%S")
    Day=x.strftime("%A")
    Month=x.strftime("%B")
    val=(Name,Age,Gender,Phone_Number,Email_id,Aadhar_Number,City,Vaccine_Dose,Vaccination_Center,Doctor_Name,Date,Time,Day,Month)
    mycursor.execute(sql,val)
    mydb.commit()# save data into db
    print("****Your details are added to vaccination details portal*****")
    
    try:
        # creates SMTP session
        s=smtplib.SMTP('smtp.gmail.com',587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("jenishasundari@gmail.com", "lgjknelwwwyimnoo")

        # message to be sent
        message=(f"Hi..{Name} Your details succesfully added to vaccination portal")

        # sending the mail
        s.sendmail("jenishasundari@gmail.com",Email_id,message)

        # terminating the session
        s.quit()
        print("Mail send successfully......")
    except:
        print("sorry mail not send")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_file.main_function()
    else:
        print("***THANKS FOR VISITING......***")
#view data into db
def view_data():
    mycursor.execute("select * from vaccination_details")
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_file.main_function()
    else:
        print("***THANKS FOR VISITING......***")
#update data into db
def update_data():
    change=input("What you want change type like this ie. column name='update name':")
    fullname=input("Enter your Full name in single quotes:")
    sql=(f"update vaccination_details set {change} where Name={fullname}")   
    mycursor.execute(sql)
    mydb.commit()
    print("Updated successfully....")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_file.main_function()
    else:
        print("***THANKS FOR VISITING......***")
#delete data into db
def delete_data():
    column_name=input("which column you want to delete:")
    delete_data=input(f"which data you want to delete in {column_name} column:")
    sql=(f"delete from vaccination_details where {column_name}={delete_data}")
    mycursor.execute(sql)
    mydb.commit()
    print("Deleted successfully.....")
    user=input("Did you want to continue yes or no:").upper()
    if user=="YES":
        main_file.main_function()
    else:
        print("***THANKS FOR VISITING......***")
