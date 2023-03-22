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
        print('nema riesenie v R')
    elif d==0:
        print('x=',-kb/(2*ka))
    else:
        print('x1=', (-kb + d ** 0.5) / (2 * ka))
        print('x2=', (-kb - d ** 0.5) / (2 * ka))
button = tk.Button(win,text='Click me!',command=executor)
button.pack()

win.mainloop()

#vieme spravit label a priradit ho do label
#vieme spravit editbox a priradit ho tam