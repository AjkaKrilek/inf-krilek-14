import tkinter as tk
win = tk.Tk()

at = tk.Label(win,text='koeficient a:')
at.pack()
a = tk.Entry(win)
a.pack()

bt = tk.Label(win,text='koeficient b:')
bt.pack()
b = tk.Entry(win)
b.pack()

ct = tk.Label(win,text='koeficient c:')
ct.pack()
c = tk.Entry(win)
c.pack()


def executor():
    print(a.get(),b.get(),c.get())
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2-4*ka*kc
    if d<0:
        v = tk.Label(text='nema riesenie v R')
        v.pack()
    elif d==0:
        vx = tk.Label(win, str(text='x=' + (-kb/(2*ka))))
        vx.pack()
    else:
        vy = tk.Label(str(text='x1=' + (-kb + d ** 0.5) / (2 * ka)))
        vy.pack()
        vz = tk.Label(str(text='x2=' + (-kb - d ** 0.5) / (2 * ka)))
        vz.pack()

button = tk.Button(win,text='Click me!',command=executor)
button.pack()

win.mainloop()
