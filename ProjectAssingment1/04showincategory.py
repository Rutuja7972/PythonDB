import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()

ct=input("Enter category to see that type of books: ")
try:
    curs.execute("select*from Books where Category='%s'"%ct)
    data=curs.fetchall()
    for rec in data:
        print("list of books:")
        print(rec[1])
except:
    print("not found")

