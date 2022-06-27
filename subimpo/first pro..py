import tkinter as tk
aks = tk.Tk()
button = tk.Button(aks, text="good morning", bg='gray', fg='red')
button.pack()
HEIGHT = 850
WIDTH = 850

canvas = tk.Canvas(aks, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = tk.Frame(aks, bg='blue')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

aks.mainloop()
