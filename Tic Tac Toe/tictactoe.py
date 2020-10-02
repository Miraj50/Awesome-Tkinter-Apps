import tkinter as tk

class TTT(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Tic Tao Toe")
		self.btns = []
		self.turn = True
		self.count = 0
		self.resizable(False, False)
		self.Start()

	def Start(self):
		for i in range(0, 3):
			row = []
			for j in range(0, 3):
				row.append(tk.Button(self, width=5, height=3, font="time 12 bold", command=lambda x=i, y=j: self.clicked(x, y)))
				row[j].grid(row=i, column=j)
			self.btns.append(row)
		tk.Button(self, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.Restart).grid(row=3, column=1)

	def clicked(self, x, y):
		self.count += 1
		if self.turn:
			char='X'
			self.btns[x][y].config(text='X', bg='black', state="disabled")
		else:
			char='O'
			self.btns[x][y].config(text='O', bg='white', state="disabled")
		self.checkWinner(char)
		self.turn = not self.turn

	def checkWinner(self, char): # Can be improved
			#horizontal
		if (((self.btns[0][0]["text"] == char) and (self.btns[0][1]["text"] == char) and (self.btns[0][2]["text"] == char)) or
		((self.btns[1][0]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[1][2]["text"] == char)) or  
		((self.btns[2][0]["text"] == char) and (self.btns[2][1]["text"] == char) and (self.btns[2][2]["text"] == char)) or  
			#vertical
		((self.btns[0][0]["text"] == char) and (self.btns[1][0]["text"] == char) and (self.btns[2][0]["text"] == char)) or
		((self.btns[0][1]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][1]["text"] == char)) or
		((self.btns[0][2]["text"] == char) and (self.btns[1][2]["text"] == char) and (self.btns[2][2]["text"] == char)) or
			#diagonal
		((self.btns[0][0]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][2]["text"] == char)) or
		((self.btns[0][2]["text"] == char) and (self.btns[1][1]["text"] == char) and (self.btns[2][0]["text"] == char))):
			self.Winner(char)
		elif self.count == 9:
			self.Winner("DRAW")

	def Winner(self, char):
		top = tk.Toplevel(self)
		top.title("Congratulations!")
		if char == "DRAW":
			topText = tk.Label(top, text=f"Its a DRAW !", font="Verdana 12 bold")
		else:
			topText = tk.Label(top, text=f"{char} is the WINNER !", font="Verdana 12 bold")
		topButton = tk.Button(top, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.Restart)
		topText.grid(row=0, column=0, padx=10, pady=10)
		topButton.grid(row=1, column=0)


	def Restart(self):
		for widget in self.winfo_children():
			widget.destroy()
		self.btns = []
		self.turn = True
		self.count = 0
		self.Start()

TTT().mainloop()


##########################################################################################
"""you can also try this"""
class tictactoe():
    def newgame(self):
        self.root.destroy()
        import tkinter as tk
        from PIL import ImageTk
        from tkinter import messagebox
        from tkinter.ttk import Progressbar
        self.p1 = 'player1'
        self.p2 = 'player2'
        self.stop_game = False
        self.w = 0
        self.sX = 0
        self.sO = 0
        self.player = 'X'
        self.root = tk.Tk()
        self.root.title('TicTacToe game')
        self.root.resizable(0, 0)
        self.root.tk.call('wm', 'iconphoto', self.root._w, ImageTk.PhotoImage(file='2.png'))
        self.b = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.b[i][j] = tk.Button(font="Arial 60 bold", width=4, bg='powder blue',
                                         command=lambda r=i, c=j: self.callback(r, c))
                self.b[i][j].grid(row=i, column=j)
        self.button = tk.Button(text="Playagain", font="times 14 bold", command=self.newgame)
        self.button.grid(row=10, column=1)
        self.root.mainloop()


    def check_for_winner(self):
        global stop_game
        from tkinter import messagebox
        import tkinter as tk
        for i in range(3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != 0:
                self.b[i][0].config(bg='yellow')
                self.b[i][1].config(bg='yellow')
                self.b[i][2].config(bg='yellow')
                stop_game = True
                self.z = self.state[i][0]
                self.winner = messagebox.showinfo("Winner", f"{self.state[i][0]} Won!")
                self.newgame()

            elif self.state[0][i] == self.state[1][i] == self.state[2][i] != 0:
                self.b[0][i].config(bg='yellow')
                self.b[1][i].config(bg='yellow')
                self.b[2][i].config(bg='yellow')
                stop_game = True
                self.z = self.state[i][0]
                self.winner = messagebox.showinfo("Winner", f"{self.state[i][0]} Won!")
                self.newgame()

            elif self.state[0][0] == self.state[1][1] == self.state[2][2] != 0:
                self.b[0][0].config(bg='yellow')
                self.b[1][1].config(bg='yellow')
                self.b[2][2].config(bg='yellow')
                self.stop_game = True
                self.z = self.state[i][0]
                self.winner = messagebox.showinfo("Winner", f"{self.state[i][0]} Won!")
                self.newgame()

            elif self.state[2][0] == self.state[1][1] == self.state[0][2] != 0:
                self.b[2][0].config(bg='yellow')
                self.b[1][1].config(bg='yellow')
                self.b[0][2].config(bg='yellow')
                self.stop_game = True
                self.z = self.state[i][0]
                self.winner = messagebox.showinfo("Winner", f"{self.state[i][0]} Won!")
                self.newgame()
            elif self.state[0][i] and self.state[1][i] and self.state[2][i] == str:
                self.newgame()
        return

    def callback(self, r, c):
        global player

        if self.player == 'X' and self.state[r][c] == 0 and self.stop_game == False:
            self.b[r][c].configure(text='X', fg='blue', bg='white')
            self.state[r][c] = 'X'
            self.player = 'O'

        if self.player == 'O' and self.state[r][c] == 0 and self.stop_game == False:
            self.b[r][c].configure(text='O', fg='red', bg='white')
            self.state[r][c] = 'O'
            self.player = 'X'
        self.check_for_winner()

    def __init__(self):
        import tkinter as tk
        from PIL import ImageTk
        self.p1 = 'player1'
        self.p2 = 'player2'
        self.stop_game = False
        self.w = 0
        self.sX = 0
        self.sO = 0
        self.player = 'X'
        self.root = tk.Tk()
        self.root.title('TicTacToe game')
        self.root.resizable(0, 0)
        self.root.tk.call('wm', 'iconphoto', self.root._w, ImageTk.PhotoImage(file='2.png'))
        self.b = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.b[i][j] = tk.Button(font="Arial 60 bold", width=4, bg='powder blue',
                                         command=lambda r=i, c=j: self.callback(r, c))
                self.b[i][j].grid(row=i, column=j)
        self.button = tk.Button(text="Playagain", font="times 14 bold", command=self.newgame)
        self.button.grid(row=10, column=1)
        self.root.mainloop()
