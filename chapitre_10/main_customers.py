import tkinter
from tkinter import Tk
from tkinter import ttk # themed toolkit
from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO('customers_db.db')
    customers = dao.findAll()

    ws = Tk()
    ws.title('Customers')
    ws.geometry('800x600')

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Name', 'FirstName')

    tv.column('Id',  anchor=tkinter.CENTER,stretch=tkinter.NO)
    tv.column('Name', anchor=tkinter.CENTER, width=80)
    tv.column('FirstName', anchor=tkinter.CENTER, width=80)

    tv.heading('Id', text='Id', anchor=tkinter.CENTER)
    tv.heading('Name', text='Name', anchor=tkinter.CENTER)
    tv.heading('FirstName', text='FirstName', anchor=tkinter.CENTER)

    for customer in customers:
        tv.insert(parent='', index=customer.id, iid=customer.id, text='', values=(customer.id,customer.last_name,customer.first_name))

    tv.pack(fill=tkinter.BOTH,expand=True)

    ws.mainloop()    



if __name__ == '__main__':
    main()