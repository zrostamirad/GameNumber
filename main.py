import random
import tkinter.messagebox
from tkinter import *

Root = Tk()
Root.geometry("%dx%d+%d+%d" % (400, 400, 500, 200))
# size & place of screen
Root.configure(background="#CBF5E1")
Root.resizable(False, False)
Root.title("بازی حدس عدد")

def Rand(x, y):
    try:
        w = random.randint(x, y)
        return w
    except:
        tkinter.messagebox.showwarning("اخطار", " مشکلی پیش اومده")


def Start(e):
    try:
        LblStart.place_forget()
        LblQuestion.place(x=165, y=130)
        LblClick.place_forget()
        LblGuess.place(x=25, y=50)
        Txt.focus_set()
        TxtOkVar.set(Rand(1, 99))
    except:
        tkinter.messagebox.showwarning("اخطار", " مشکلی پیش اومده")


def Iguess(e):
    try:
        if TxtOkVar.get() != "":
            if TxtVar.get() != "":
                if int(TxtVar.get()) < int(TxtOkVar.get()):
                    LblFewer.place_forget()
                    LblMore.place(x=80, y=180)
                    TxtVar.set("")
                elif int(TxtVar.get()) > int(TxtOkVar.get()):
                    LblMore.place_forget()
                    TxtVar.set("")
                    LblFewer.place(x=80, y=180)
                else:
                    LblQuestion.place_forget()
                    LblGuess.place_forget()
                    LblMore.place_forget()
                    LblFewer.place_forget()
                    TxtVar.set("")
                    TxtOkVar.set("")
                    LblYes.place(x=70, y=70)
                    BtnRetry.place(x=100, y=290)
                    Btn.place_forget()
                    TxtVar.set("")
            else:
                tkinter.messagebox.showwarning("اخطار", "!فیلدت که خالیه")
        else:
            tkinter.messagebox.showwarning("اخطار", "اول روی تصویر کلیک کن تا بازی شروع بشه!")
    except:
        tkinter.messagebox.showwarning("اخطار", "عدد وارد کن")


def Again(e):
    try:
        BtnRetry.place_forget()
        Btn.place(x=100, y=290)
        LblYes.place_forget()
        LblStart.place(x=130, y=100)
        LblClick.place(x=80, y=50)
    except:
        tkinter.messagebox.showwarning("اخطار", " مشکلی پیش اومده")

#Images
ImgQuestion = PhotoImage(file="img/question-mark.png")
ImgGo = PhotoImage(file="img/Go128.png")
ImgYes = PhotoImage(file="img/yes256.png")

#Lables
LblClick = Label(Root, text="برای شروع بازی کلیک کن", font="nazanin 20 bold", bg="#CBF5E1")
LblClick.place(x=80, y=50)
LblGuess = Label(Root, text="فکر میکنی چه عددی انتخاب کردم؟", font="nazanin 20 bold", bg="#CBF5E1")
LblGuess.place_forget()
LblMore = Label(Root, text=" :D نچ عدد من بزرگتره", fg="red", font="nazanin 20 bold", bg="#CBF5E1")
LblMore.place_forget()
LblFewer = Label(Root, text=" :) نچ عدد من کوچیکتره", fg="red", font="nazanin 20 bold", bg="#CBF5E1")
LblFewer.place_forget()
LblStart = Label(Root, text="*", image=ImgGo, bg="#CBF5E1")
LblStart.bind("<Button-1>", Start)
LblStart.place(x=130, y=100)
LblQuestion = Label(Root, text="*", image=ImgQuestion, bg="#CBF5E1")
LblQuestion.place_forget()
LblYes = Label(Root, text="*", image=ImgYes, bg="#CBF5E1")
LblYes.place_forget()

#Entry
TxtVar = StringVar()
TxtOkVar = StringVar()
TxtOk = Entry(Root, width=30, textvariable=TxtOkVar).place_forget()
Txt = Entry(Root, width=30, textvariable=TxtVar, justify="center")
Txt.place(x=100, y=250)

#Buttons
Btn = Button(Root, text="حدس میزنم", font="titr 10 bold")
Btn.bind("<Button-1>", Iguess)
Btn.place(x=100, y=290)

BtnRetry = Button(Root, text="دوباره", font="titr 10 bold")
BtnRetry.bind("<Button-1>", Again)
BtnRetry.place_forget()


Root.mainloop()
