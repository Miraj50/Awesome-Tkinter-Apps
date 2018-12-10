import tkinter as tk

win = tk.Tk()

def show_values():
    a = " ".join([str(i.get()) for i in values])
    tk.Label(win, text=a).grid()

results = ["RB1: ", "RB2: ", "RB3: "]
values = [tk.IntVar() for i in range(len(results))]
i = 0
for r in results:
    r1 = tk.Radiobutton(win, text="Yes", variable=values[i], value=1)
    r2 = tk.Radiobutton(win, text="No", variable=values[i], value=2)
    r1.grid(column=1, row=i)
    r2.grid(column=2, row=i)

    item_Label = tk.Label(win, text=r)
    item_Label.grid(column=0, row=i)
    i += 1

tk.Button(win, text='Show Values', command=show_values).grid(columnspan=2)

win.mainloop()