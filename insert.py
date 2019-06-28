import pymysql
myconn = pymysql.connect(host="localhost", user="root", passwd="root",database="db_sample")

#Insert data into the database based on the parmeter passed to the function
def inserData(fullname,email):
    try:
        cur = myconn.cursor()
        sql = "insert into tbl_employee(full_name,email) values (%s, %s)"
        val = (fullname,email)

        cur.execute(sql, val)
        myconn.commit()
        return  "true"
    except Exception:
        print(Exception)
        myconn.rollback()
    finally:
        myconn.close()

