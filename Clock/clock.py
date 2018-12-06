import tkinter
import time
from tkinter import scrolledtext

class Clock(tkinter.Label):
    def __init__(self, parent=None, seconds=True):
        tkinter.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time = time.strftime('%I:%M:%S')
        else:
            self.time = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        self.after(200, self.tick)

    def tick(self):
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)

def timestamp():
    print(time.strftime("%I:%M:%S"))

if __name__ == "__main__":

    window = tkinter.Tk()
    frame = tkinter.Frame(window, width=800, height=800)
    frame.pack()

    tkinter.Label(frame, text="Current time: ").pack()

    text = scrolledtext.ScrolledText(frame, height=10)
    text.pack()

    clock1 = Clock(frame)
    clock1.pack()
    clock1.configure(bg='white', fg='black', font=("helvetica", 65))

    tkinter.Label(frame, text=" ").pack()

    b = tkinter.Button(frame, text='Quit', command=quit)
    b.pack(side=tkinter.RIGHT)
    b2 = tkinter.Button(frame, text='Current Time', command=lambda :text.insert("end", time.strftime("%I:%M:%S")+'\n'))
    b2.pack(side=tkinter.LEFT)

    window.mainloop()