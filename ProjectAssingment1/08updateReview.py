import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()
'''
curs.execute("alter table Books add Review varchar(500)")
con.commit()
print("altered")
'''


cd=int(input("Enter bookcode: "))
curs.execute("select*from Books where Bookcode=%d"%cd)
data=curs.fetchall()
if data:
    rev=float(input("Riview: "))
    curs.execute("update Books set Review='%s' where Bookcode=%d"%(rev,cd))
    con.commit()
    print("Review updated successfully")
else:
    print("not found")