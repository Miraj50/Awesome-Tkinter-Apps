#importing requirements
import tkinter as tk

class TTT(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Tic Tac Toe")
		self.btns = []
		self.turn = True
		self.count = 0
		self.resizable(False, False)
		self.Start()

	def Start(self):
		for i in range(0, 3):
			row = []
			for j in range(0, 3):
				row.append(tk.Button(self, width=10, height=5, font="time 12 bold", command=lambda x=i, y=j: self.clicked(x, y)))
				row[j].grid(row=i, column=j)
			self.btns.append(row)
		tk.Button(self, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.Restart).grid(row=3, column=1,sticky='WE')

	def clicked(self, x, y):
		self.count += 1
		if self.turn:
			char='X'
			self.btns[x][y].config(text='X', bg='black', state="disabled")
		else:
			char='O'
			self.btns[x][y].config(text='O', bg='gray', state="disabled")
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
		top.geometry('200x90+' + str(self.winfo_x()+60) + "+" + str(self.winfo_y()+120))
		if char == "DRAW":
			topText = tk.Label(top, text=f"--- Its a DRAW ! ---", font="Verdana 12 bold")
		else:
			topText = tk.Label(top, text=f" {char} is the WINNER !! ", font="Verdana 12 bold")
		topButton = tk.Button(top, text="Restart", bg='blue', fg='white', activebackground='blue3', activeforeground='white', command=self.Restart)
		topText.grid(row=0, column=0, padx=10, pady=10, sticky="WE")
		topButton.grid(row=1, column=0)


	def Restart(self):
		for widget in self.winfo_children():
			widget.destroy()
		self.btns = []
		self.turn = True
		self.count = 0
		self.Start()

TTT().mainloop()