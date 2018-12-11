import tkinter as tk
import tkinter.ttk as ttk

class DrawApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Draw Your Heart Out!")
		self._xold = None
		self._yold = None
		self.canvas = None
		self.color = "Black"
		self.thickness = 1
		self.tag = ["tag", "0"] #Don't know why but tags can't be just a number
		self._create_widgets()

	def _create_widgets(self):
		topframe = tk.Frame(self)
		topframe.grid(row=0, column=0, pady=10)

		self.col_select = tk.StringVar()
		colorList = ttk.Combobox(topframe, textvariable=self.col_select, values=['Black', 'Red', 'Green', 'Yellow', 'Brown'], state="readonly", width=10)
		colorList.current(0)
		self.option_add('*TCombobox*Listbox.selectBackground', 'skyblue')
		colorList.bind('<<ComboboxSelected>>', self._change_color)
		colorList.grid(row=0, column=0, padx=5)

		self.t_select = tk.StringVar()
		tList = ttk.Combobox(topframe, textvariable=self.t_select, values=[1, 2, 3, 4, 5], state="readonly", width=2)
		tList.current(0)
		tList.bind('<<ComboboxSelected>>', self._change_thickness)
		tList.grid(row=0, column=1, padx=5)

		tk.Button(topframe, text="Undo", bg="blue", fg="white", activebackground="blue4", activeforeground="white", command=self._undo).grid(row=0, column=2, padx=5)
		tk.Button(topframe, text="Clear", bg="brown", fg="white", activebackground="brown4", activeforeground="white", command=self._clear).grid(row=0, column=3, padx=5)
		self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
		self.canvas.grid(row=1, column=0, padx=10, pady=(0,10))
		self.canvas.bind("<ButtonRelease-1>", self._on_up)
		self.canvas.bind("<B1-Motion>", self._on_motion)

	def _change_color(self, event=None):
		self.color = self.col_select.get()

	def _change_thickness(self, event=None):
		self.thickness = int(self.t_select.get())

	def _clear(self):
		self.canvas.delete("all")
		self.tag = ["tag", "0"]

	def _undo(self):
		cur_tag = int(self.tag[1])
		if cur_tag >= 1:
			self.canvas.delete("tag"+str(cur_tag-1))
			self.tag = ["tag", str(cur_tag - 1)]

	def _on_up(self, event):
		self._xold = None
		self._yold = None
		self.tag = ["tag", str(int(self.tag[1])+1)]

	def _on_motion(self, event):
		tag = "".join(self.tag)
		x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
		x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
		event.widget.create_oval(x1, y1, x2, y2, width=0, fill=self.color, tag=tag)
		if self._xold is not None and self._yold is not None:
			self.canvas.create_oval(x1, y1, x2, y2, width=0, fill=self.color, tag=tag)
			self.canvas.create_line(self._xold, self._yold, event.x, event.y, smooth=True, width=2*self.thickness, fill=self.color, tag=tag)
	# here's where you draw it. smooth. neat.
		self._xold = event.x
		self._yold = event.y

DrawApp().mainloop()