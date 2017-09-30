# Currency Converter for Python3

from tkinter import *

window = Tk()
window.configure(background = "#9dc66b")

heading = Label(window, text = "Currency Converter", fg = "black", bg = "#9dc66b", font = ("times", 42))
heading.pack(side = TOP)

fromlabel = Label(window, text = "Convert from:", bg = "#9dc66b", fg = "black", font = ("times", 16))
fromlabel.pack(side = LEFT)

isDollarFrom = IntVar()
isRupeeFrom = IntVar()
isPoundFrom = IntVar()

dollarCheck = Checkbutton(text = "Dollar", variable = isDollarFrom, onvalue = 1, offvalue = 0, bg = "#9dc66b")
rupeeCheck = Checkbutton(text = "Rupee", variable = isRupeeFrom, onvalue = 1, offvalue = 0, bg = "#9dc66b")
poundCheck = Checkbutton(text = "Pound", variable = isPoundFrom, onvalue = 1, offvalue = 0, bg = "#9dc66b")
dollarCheck.pack(side = RIGHT)
rupeeCheck.pack(side = RIGHT)
poundCheck.pack(side = RIGHT)

tolabel = Label(window, text = "Convert to:", bg = "#9dc66b", fg = "black", font = ("times", 16))
tolabel.pack(side = BOTTOM)
















window.mainloop()
