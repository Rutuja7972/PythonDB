import mysql.connector as s

con=s.connect(host="bualwe2cca6rsts08vrb-mysql.services.clever-cloud.com",user="uayxzatuq5pn1ifa",password="SuEf27AXbjYDYRxfABKQ",database="bualwe2cca6rsts08vrb")
curs=con.cursor()

cd=int(input("Enter Bookcode to see details: "))
try:
    curs.execute("select * from Books where Bookcode=%d"%cd)
    data=curs.fetchall()
    for rec in data:
        print("Bookcode      :%d"%rec[0])
        print("Bookname      :%s"%rec[1])
        print("Category      :%s"%rec[2])
        print("Author        :%s"%rec[3])
        print("Publication   :%s"%rec[4])
        print("Edition       :%s"%rec[5])
        print("Price         :%d"%rec[6])
except:
    print("NOT FOUND")

con.close()