import sqlite3
from Customer import Customer
class CustomerDAO:


    def __init__(self,db_file:str) -> None:
        self.__con = sqlite3.connect(db_file)


    def __enter__(self):
        return self
    
    def __exit__(self,*exc):
        print(*exc)
        self.__con.close()
        return True


    def findAll(self):
        sql = "SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)

        for row in rs:
            c = Customer(*row)
            yield c        



    def __del__(self):
        if self.__con:
            self.__con.close()



def main():

    with CustomerDAO("customers_db.db") as dao:
        print(list(dao.findAll()))

if __name__ == '__main__':
    main()