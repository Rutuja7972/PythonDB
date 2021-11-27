import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()

id=int(input("Enter bookcode: "))
npr=float(input("Enter new price to update: "))

curs.execute("select*from Books where Bookcode=%d"%id)
data= curs.fetchall()
if data:
    curs.execute("update Books set Price=%.2f where Bookcode=%d"%(npr,id))
    con.commit()
    print("Price updated successfully")
else:
    print("Book does not exist")