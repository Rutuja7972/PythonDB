import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()
print("Name the author and publication:")
at=input("Author: ")
pub=input("Publication: ")

curs.execute("select*from Books where Author='%s' and Publication='%s'"%(at,pub))
data=curs.fetchall()
if data:
    print(data)
else:
    print("Not available")
