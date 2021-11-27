import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()
try:
    print("Insert book details that you want to add in:")
    cd=int(input("Enter bookcode: "))
    nm=input("Book name: ")
    ct=input("Category: ")
    at=input("Author: ")
    pd=input("publication: ")
    ed=input("edition: ")
    pr=float(input("Price: "))

    curs.execute("insert into Books values(%d,'%s','%s','%s','%s','%s',%.2f)"%(cd,nm,ct,at,pd,ed,pr))
    con.commit()
    print("Book added successfully")
except:
    print("Error in insertion")

con.close()