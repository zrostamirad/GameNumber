import random
import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("%dx%d+%d+%d" % (400, 400, 500, 200))
# size & place of screen
root.configure(background="#CBF5E1")
root.resizable(False,False)
root.title("بازی حدس عدد")


def rand(x,y):
    try:
        w =random.randint(x,y)
        return w
    except:
        tkinter.messagebox.showwarning("اخطار"," مشکلی پیش اومده")

def start(e):
    try:
        lblstart.place_forget()
        lblquestion.place(x=165, y=130)
        lbl.place_forget()
        lbl2.place(x=25, y=50)
        txt.focus_set()
        txtok.set(rand(1,99))
    except:
        tkinter.messagebox.showwarning("اخطار"," مشکلی پیش اومده")
def Iguess(e):
    try:
        if txtok.get()!="":
            if txtvar.get() !="":
                if int(txtvar.get()) < int(txtok.get()):
                    lbl4.place_forget()
                    lbl3.place(x=80, y=180)
                    txtvar.set("")
                elif int(txtvar.get()) > int(txtok.get()):
                    lbl3.place_forget()
                    txtvar.set("")
                    lbl4.place(x=80, y=180)
                else:
                    lblquestion.place_forget()
                    lbl2.place_forget()
                    lbl3.place_forget()
                    lbl4.place_forget()
                    txtvar.set("")
                    txtok.set("")
                    lblyes.place(x=70, y=70)
                    btnretry.place(x=100, y=290)
                    btn.place_forget()
                    txtvar.set("")
            else:
                tkinter.messagebox.showwarning("اخطار", "!فیلدت که خالیه")
        else:
            tkinter.messagebox.showwarning("اخطار", "اول روی تصویر کلیک کن تا بازی شروع بشه!")
    except:
        tkinter.messagebox.showwarning("اخطار","عدد وارد کن")

def again(e):
    try:
        btnretry.place_forget()
        btn.place(x=100,y=290)
        lblyes.place_forget()
        lblstart.place(x=130, y=100)
        lbl.place(x=80, y=50)
    except:
        tkinter.messagebox.showwarning("اخطار"," مشکلی پیش اومده")


imgquestion = PhotoImage(file="img/question-mark.png")
imggo = PhotoImage(file="img/Go128.png")
imgyes = PhotoImage(file="img/yes256.png")

#Lable
lbl = Label(root, text="برای شروع بازی کلیک کن", font="nazanin 20 bold",bg="#CBF5E1")
lbl.place(x=80, y=50)
lbl2 = Label(root, text="فکر میکنی چه عددی انتخاب کردم؟", font="nazanin 20 bold",bg="#CBF5E1")
lbl2.place_forget()
lbl3 = Label(root, text=" :D نچ عدد من بزرگتره",fg="red", font="nazanin 20 bold",bg="#CBF5E1")
lbl3.place_forget()
lbl4 = Label(root, text=" :) نچ عدد من کوچیکتره",fg="red", font="nazanin 20 bold",bg="#CBF5E1")
lbl4.place_forget()
lblstart = Label(root, text="*", image=imggo,bg="#CBF5E1")
lblstart.bind("<Button-1>", start)
lblstart.place(x=130, y=100)
lblquestion = Label(root, text="*", image=imgquestion,bg="#CBF5E1")
lblquestion.place_forget()
lblyes = Label(root, text="*", image=imgyes,bg="#CBF5E1")
lblyes.place_forget()

#Entry

txtvar = StringVar()
txtok=StringVar()
txtook = Entry(root, width=30, textvariable=txtok).place_forget()
txt = Entry(root, width=30, textvariable=txtvar,justify="center")
txt.place(x=100, y=250)

btn=Button(root,text="حدس میزنم",font="titr 10 bold")
btn.bind("<Button-1>",Iguess)
btn.place(x=100,y=290)

btnretry=Button(root,text="دوباره", font="titr 10 bold")
btnretry.bind("<Button-1>",again)
btnretry.place_forget()


root.mainloop()
