from tkinter import Tk
from tkinter import ttk # themed toolkit



def say_hello(label:ttk.Label):
    label.config(text='Hello Fred from say_hello')



def main():
    fenetre = Tk()
    frm =ttk.Frame(fenetre,padding=10)
    frm.grid()

    texte = ttk.Label ( frm, text="Hello World" )

    # def h():
    #     texte.config(text="Bonjour Fred")


    texte.grid(column=0,row=0)
    # texte.config(text="Bonjour")
    # btn_hello = ttk.Button(frm,text="Say hello",command=lambda:texte.config(text="Bonjour")).grid(column=0,row=1)
    # btn_hello = ttk.Button(frm,text="Say hello",command=h).grid(column=0,row=1)
    btn_hello = ttk.Button(frm,text="Say hello",command=lambda:say_hello(texte)).grid(column=0,row=1)
    btn_quit = ttk.Button(frm,text="Quit",command=fenetre.destroy).grid(column=0,row=2)
    
    
    fenetre.mainloop()



if __name__ == '__main__':
    main()