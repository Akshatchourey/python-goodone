from tkinter import *
from PIL import Image, ImageTk #pillow library full name.
# from page_form2 import *
from snakegame import *
import csv

al = Tk()
al.geometry("1280x900")
al.title("Python with akshat")

f1 = Frame(al, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
Label(f1, text="Beaker section", fg="red", font="comic 12 bold").grid(pady=305)
f2 = Frame(al, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)
Label(f2, text="Game center", fg="red", font="comic 25 bold").grid(padx=280)
f3 = Frame(al)
f3.pack()


def danger():
    ak = Tk()
    ak.geometry("355x555")
    f5 = Frame(ak, borderwidth=10)
    f5.pack(side=LEFT)
    Label(ak, text="Generated Bill", font="comic 25 bold").pack()
    Label(f5, text="|\n" * 30).pack(pady=14)
    f6 = Frame(ak, borderwidth=10)
    f6.pack(side=RIGHT)
    Label(f6, text="|\n" * 30).pack(pady=14)
    totle = (5 * fval.get()) + (10 * sval.get()) + (20 * tval.get()) + (30 * foval.get()) + (100 * fival.get()) + (
            800 * sival.get())
    f7 = Frame(ak)
    f7.pack(side=LEFT)
    Label(f7, text="NAME", font="comic 25 bold").pack()
    Label(f7, text="1.parlay\n2.bitania\n3.gooday\n4.crackjeck\n5.Motalal\n6.yAkshat Namkines",
          font="comic 10 bold").pack()
    f8 = Frame(ak)
    f8.pack(side=LEFT)
    Label(f8, text="No.       Rs.", font="comic 25 bold").pack()
    Label(f8,
          text=f"{fval.get()}\t\t{5 * fval.get()}\n{sval.get()}\t\t{10 * sval.get()}\n{tval.get()}\t\t{20 * tval.get()}\n{foval.get()}\t\t{30 * foval.get()}\n{fival.get()}\t\t{100 * fival.get()}\n{sival.get()}\t\t{800 * sival.get()}\nTOTLE\t\t{totle}",
          font="comic 10 bold").pack()
    ak.mainloop()

def popscreena(oname):
    global pop
    def popend():
        pop.destroy()
        Label(f3, text=f"{oname}", font="comic 10 bold").grid(row=1, column=2)

    pop = Toplevel(al)
    pop.title("my pop")
    pop.geometry('350x120')
    pop.config(bg='green')
    Label(pop, text=f"welcome back {oname}. Have a good day.\n|press hare to continue|", bg="green", fg="white", font=("helvetica",12)).pack(pady=10)
    Button(pop, text="--->",bg="yellow", command = popend).pack()

def login():
    global owl
    owl = Tk()
    owl.geometry("765x445")
    Label(owl, text="username", font="comic 10 bold").grid()
    Label(owl, text="password", font="comic 10 bold").grid()

    def getvals():
        ida = userentry.get()
        password = passentry.get()
        f = open("id_data.csv", "r")
        csv_read = csv.reader(f)
        for row in csv_read:
            if row[0] == ida:
                if row[1] == password:
                    popscreena(oname = row[2])
                    owl.destroy()
            else:
                Label(owl, text="Rowing Details", font="comic 30 bold").grid(row=4, column=4)

    uservalue = StringVar()
    passvalue = StringVar()
    userentry = Entry(owl, textvariable=uservalue)
    passentry = Entry(owl, textvariable=passvalue)
    userentry.grid(row=0, column=1)
    passentry.grid(row=1, column=1)
    Button(owl, text="summit", command=getvals).grid(row=3, column=1)
    owl.mainloop()

def signup():
    global ul
    ul = Tk()
    ul.geometry("765x445")
    Label(ul, text="username", font="comic 10 bold").grid()
    Label(ul, text="user_ID", font="comic 10 bold").grid()
    Label(ul, text="password", font="comic 10 bold").grid()

    def getvals_sign():
        name = userentry.get()
        ID = IDentry.get()
        passw = passentry.get()
        row = [ID, passw , name]
        filename = "id_data.csv"
        with open(filename, 'a', newline='') as f:
            csv_w = csv.writer(f, delimiter=",")
            csv_w.writerow(row)
            ul.destroy()
        f.close()

    uservalue = StringVar()
    IDvalue = StringVar()
    passvalue = StringVar()
    userentry = Entry(ul, textvariable=uservalue)
    IDentry = Entry(ul, textvariable=IDvalue)
    passentry = Entry(ul, textvariable=passvalue)
    userentry.grid(row=0, column=1)
    IDentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    Button(ul, text="submit", command=getvals_sign).grid(row=3, column=1)
    ul.mainloop()

Label(f3, text="Welcom To My Shop", font="comic 20 bold").grid(row=1, column=1)
Label(f3, text="Akshat", font="comic 10 bold").grid(row=1, column=2)
login = Button(f3, text="login", bg="gray", fg="black", font="comic 10 bold", command=login).grid(row=1, column=3)
sighin = Button(f3, text="signin", bg="gray", fg="black", font="comic 10 bold", command=signup).grid(row=1, column=4)
Label(f3, text="1.parley = 5Rs", font="comic 10 bold").grid(row=2, column=1)
Label(f3, text="  2.britania = 10Rs", font="comic 10 bold").grid(row=3, column=1)
Label(f3, text="  3.gooday = 20Rs", font="comic 10 bold").grid(row=4, column=1)
Label(f3, text="   4.crackjack =30Rs", font="comic 10 bold").grid(row=5, column=1)
Label(f3, text="5.Motilal=100Rs", font="comic 10 bold").grid(row=6, column=1)
Label(f3, text="6.Akshat Namkeens=800Rs", font="comic 10 bold").grid(row=7, column=1)

fval = IntVar()
sval = IntVar()
tval = IntVar()
foval = IntVar()
fival = IntVar()
sival = IntVar()
pree = IntVar()

fint = Entry(f3, textvariable=fval).grid(row=2, column=2)
sint = Entry(f3, textvariable=sval).grid(row=3, column=2)
tint = Entry(f3, textvariable=tval).grid(row=4, column=2)
foint = Entry(f3, textvariable=foval).grid(row=5, column=2)
fiint = Entry(f3, textvariable=fival).grid(row=6, column=2)
siint = Entry(f3, textvariable=sival).grid(row=7, column=2)
preeint = Checkbutton(f3, text="want to prebook your meal?").grid(row=8, column=2)

button = Button(f3, text="Generate Bill.", bg="blue", fg="black", font="comic 10 bold", command=danger).grid(row=9, column=1)
game = Button(f3, text="play game.", bg="blue", fg="black", font="comic 10 bold", command=game).grid(row=89, column=2)
image = Image.open("ak1.png")
photo = ImageTk.PhotoImage(image)
Label(image=photo).pack()

al.mainloop()
