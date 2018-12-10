from tkinter import OptionMenu
import tkinter as Tkinter

class GasGen(Tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.vars = []
		self.initialize()
		self.grid()

	def initialize(self):
		for i in range(8):
			t = Tkinter.StringVar()
			t.set("Not Selected")
			self.vars.append(t)

		for i in range(len(self.vars)):
			OptionMenu(self, self.vars[i], "methane", "ethane", "propane", "iso-butane", "n-butane", "iso-pentane", "n-pentane", "benzene").grid(column = 0, row = i)

		Tkinter.Button(self, text="Show Values", command=self.show).grid(pady=10)

	def show(self):
		Tkinter.Label(self, text="\n".join([k.get() for k in self.vars])).grid(pady=10)

if __name__ == "__main__":
	app = GasGen()
	app.title('Gas mixture generator')
	app.configure(background = "slate gray")
	app.mainloop()