import mysql.connector
from tkinter import *
from tkinter import ttk

db = mysql.connector.connect(host='localhost', password='12345akshat', user='root', database="school")
school = db.cursor()
if db.is_connected():
    print("Connection seccessfull...")

ak = Tk()
ak.geometry("515x650")
ak.title("Scope Analysis.")
Label(ak, text="SCOPE IN DIFFERENT FIELDS", pady=25).grid()
frm = ttk.Frame(ak, padding=90)
frm.grid()
ttk.Label(frm, text="No.").grid(column=0, row=0)
ttk.Label(frm, text="FIELDS").grid(column=1, row=0)
ttk.Label(frm, text="VALUES").grid(column=2, row=0)

def create_scrollable_frame(root):
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    return frame
def increment(no):
    school.execute(f"update scopes set value = value+1 where No = {no}")
    db.commit()
    render()
def decrement(no):
    school.execute(f"update scopes set value = value-1 where No = {no}")
    db.commit()
    render()
def add_field(no, st, entry):
    entry.destroy()
    school.execute(f"insert into scopes values({no},'{st}', 1)")
    db.commit()
    render()


def render():
    school.execute("select * from scopes")
    i = 1
    entry = ttk.Entry(frm)
    for t in school:
        ttk.Label(frm, text=t[0]).grid(column=0, row=i)
        ttk.Label(frm, text=t[1]).grid(column=1, row=i)
        ttk.Label(frm, text=t[2]).grid(column=2, row=i)
        ttk.Button(frm, text="-", command=lambda t=t: decrement(t[0])).grid(column=3, row=i)
        ttk.Button(frm, text="+", command=lambda t=t: increment(t[0])).grid(column=4, row=i)
        i += 1

    entry.grid(column=1, row=i)
    ttk.Button(frm, text="ADD", command=lambda t=t: add_field(i, entry.get(), entry)).grid(column=3, row=i)
    ak.mainloop()


render()

school.close()
db.close()
input("Enter to exit:-")
