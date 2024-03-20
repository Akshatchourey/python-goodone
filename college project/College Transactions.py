import mysql.connector
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("College Transactions")
        self.iconbitmap("logo.ico")
        self.geometry("920x610+175+90")
        self.minsize(900,550)
        self.bind('<Escape>', lambda event: self.quit())

        menu = tk.Frame(self, borderwidth=4)
        menu.pack(side='left', fill='y')

        title = ttk.Label(menu, text="College Transactions", font="comic 12 bold")
        home = ttk.Button(menu, text="Home Page", command=lambda: self.show_frame(HomePage))
        add = ttk.Button(menu, text="Data Page", command=lambda: self.show_frame(Add))
        analyse = ttk.Button(menu, text="Analysis Page", command=lambda: self.show_frame(Analyse))

        title.pack()
        home.pack()
        add.pack()
        analyse.pack()

        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.HomePage = HomePage
        self.Add = Add
        self.Analyse = Analyse

        for F in {HomePage, Add, Analyse}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, frame):
        self.frames[frame].tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Home Page", font=('Times', '20'))
        label.pack()


class Add(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        add_t = tk.Label(self, text="Add Transactions", font=('Times', '20'))
        add_t.pack()

        courser.execute("select count(*) from entry;")
        self.no = tk.IntVar(value=courser.fetchone()[0]+1)
        date_value = tk.StringVar(value="2024-mm-dd")
        note_value = tk.StringVar(value="note")
        type_value = tk.StringVar(value="Category")
        mode_value = tk.BooleanVar()
        amount_value = tk.DoubleVar()

        add_f1 = tk.Frame(self)
        add_f1.pack(fill='x')
        add_f1.columnconfigure((0,1,2,3,4,5,6), weight=1)
        add_f1.rowconfigure(0, weight=1)

        types = ["food","pocket money","friend/partner","stationary","events","personal","shopping","other"]
        date_entry = ttk.Entry(add_f1, textvariable=date_value)
        note_entry = ttk.Entry(add_f1, textvariable=note_value)
        type_entry = ttk.Combobox(add_f1, textvariable=type_value)
        type_entry['value'] = types
        mode_online = ttk.Radiobutton(add_f1, text="Online", value=False, variable=mode_value)
        mode_offline = ttk.Radiobutton(add_f1, text="Offline", value=True, variable=mode_value)
        amount_entry = ttk.Entry(add_f1, textvariable=amount_value)

        tk.Label(add_f1, textvariable=self.no).grid(row=0, column=0,rowspan=2, sticky='ew')
        date_entry.grid(row=0, column=1,rowspan=2, sticky='ew')
        note_entry.grid(row=0, column=2,rowspan=2, sticky='ew')
        mode_online.grid(row=0, column=3)
        mode_offline.grid(row=1, column=3)
        type_entry.grid(row=0, column=4,rowspan=2, sticky='ew')
        amount_entry.grid(row=0, column=5,rowspan=2, sticky='ew')
        add_data = ttk.Button(add_f1, text="Add Data"
                              ,command=lambda: self.add_data(date_value,note_value,type_value,mode_value,amount_value))
        add_data.grid(row=0, column=6, rowspan=2)

        show_t = tk.Label(self, text="Show Transactions", font=('Times', '20'))
        show_t.pack()
        add_f2 = tk.Frame(self)
        add_f2.pack()

        refresh = ttk.Button(add_f2, text="Refresh Data"
                             ,command=lambda:   self.show_data("select * from entry order by Date desc;"))
        refresh.pack(side='left')

        dicti = {
            '2023': "select * from entry where YEAR(Date)=2023;",
            '2024': "select * from entry where YEAR(Date)=2024;",
            'Online': "select * from entry where Mode=False order by Date desc;",
            'Offline': "select * from entry where Mode=True order by Date desc;",
            'amount+': "select * from entry where Amount>0 order by Date desc;",
            'amount-': "select * from entry where Amount<0 order by Date desc;",
            'amount+desc': "select * from entry where Amount>0 order by Amount desc;",
            'amount-desc': "select * from entry where Amount<0 order by Amount;"
        }
        filters = ['2023','2024','Online','Offline','amount+','amount-','amount+desc','amount-desc']
        filter_value = tk.StringVar(value="Filters")
        combo = ttk.Combobox(add_f2, textvariable=filter_value)
        combo['values'] = filters
        combo.pack(side='left')
        combo.bind('<<ComboboxSelected>>', lambda event:self.show_data(dicti[filter_value.get()]))

        type_combo = ttk.Combobox(add_f2)
        type_combo['values'] = types
        type_combo.set("Type Filters")
        type_combo.pack(side='left')
        type_combo.bind('<<ComboboxSelected>>',
                        lambda event: self.show_data(
                            f"select * from entry where Type='{type_combo.get()}' order by Date desc;"))

        self.tree = ttk.Treeview(self, columns=('sno', 'date', 'note', 'category', 'amount'), show='headings')
        self.tree.column("sno", width=50)
        self.tree.column("date", width=80)
        self.tree.heading('sno', text='SNo.')
        self.tree.heading('date', text='Date')
        self.tree.heading('note', text='Note')
        self.tree.heading('category', text='Category')
        self.tree.heading('amount', text='Amount')
        self.tree.pack(expand=True,fill='both',padx=9, pady=9)
        self.tree.tag_configure("colour_blue", foreground="blue")

        self.show_data("select * from entry order by Date desc;")

    def show_data(self, query):
        self.tree.delete(*self.tree.get_children())
        courser.execute(query)
        i = 1
        for t in courser:
            row = (i, t[1], t[2], t[3], t[5])
            if t[4]: self.tree.insert('', 'end', values=row, tags=('colour_blue',))
            else: self.tree.insert('', 'end', values=row)
            i += 1

    def add_data(self, date_value, note_value, type_value, mode_value, amount_value):
        courser.execute(f"insert into entry values({self.no.get()},'{date_value.get()}','{note_value.get()}'"
                        f",'{type_value.get()}',{mode_value.get()},{amount_value.get()});")
        db.commit()
        self.no.set(self.no.get() + 1)
        self.show_data("select * from entry order by Date desc;")


class Analyse(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Analyzing Page", font=('Times', '20'))
        frame3 = tk.Frame(self)
        label.pack()
        frame3.pack()
        dect = {
            "food":"select Amount from entry where Type ='food' order by Date;",
            "small entries":"select Amount from entry where Amount>-500 and Amount<500 order by Date;",
            "all entries":"select Amount from entry order by Date;"
        }
        ttk.Button(frame3, command=lambda: self.clear_graph(), text="Clear Graph").pack()
        box1 = ttk.Button(frame3, text="food", command=lambda: self.graph(dect.get("food"), "food"))
        box2 = ttk.Button(frame3, text="small entries", command=lambda: self.graph(dect.get("small entries"),"small entries"))
        box3 = ttk.Button(frame3, text="all entries", command=lambda: self.graph(dect.get("all entries"),"all entries"))
        box1.pack(side='left')
        box2.pack(side='left')
        box3.pack(side='left')

        self.fig = Figure(figsize=(7, 6), dpi=110)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(expand=True,fill='both',padx=20, pady=20)
        self.plt = self.fig.add_subplot(111)

    def clear_graph(self):
        self.fig.clf()
        self.plt = self.fig.add_subplot(111)
        self.canvas.draw()

    def graph(self, query, legend):
        courser.execute(query)
        x_axis, values = [], []
        data = courser.fetchall()
        x_axis = [i for i in range(len(data))]
        for t in data: values.append(t[0])

        self.plt.plot(x_axis, values, label=legend)
        self.plt.set_title("Graph")
        self.plt.set_ylabel("Amount")
        self.plt.set_xlabel("Entries")
        self.plt.legend()
        self.canvas.draw()


if __name__ == "__main__":
    db = mysql.connector.connect(host='localhost', password='12345akshat', user='root', database="money")
    courser = db.cursor()
    if db.is_connected(): print("Connection successfully...")
    app = App()
    app.mainloop()
    db.close()
