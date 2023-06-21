import tkinter as tk

def executor():
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d < 0:
        result_label.config(text="Nema riesenie v R")
    elif d == 0:
        result_label.config(text="x: " + str(-kb / (2*ka)))
    else:
        result_label.config(text="x1: " + str((-kb + d ** 0.5) / (2*ka)))
        result_label.config(text="x2: " + str((-kb - d ** 0.5) / (2*ka)))

win = tk.Tk()
win.title("Quadratic Equation Solver")

atext = tk.Label(win, text="koeficient a:")
atext.pack()
a = tk.Entry(win)
a.pack()

btext = tk.Label(win, text="koeficient b:")
btext.pack()
b = tk.Entry(win)
b.pack()

ctext = tk.Label(win, text="koeficient c:")
ctext.pack()
c = tk.Entry(win)
c.pack()

button = tk.Button(win, text="vysledok", command=executor)
button.pack()

result_label = tk.Label(win, text="")
result_label.pack()

win.mainloop()
