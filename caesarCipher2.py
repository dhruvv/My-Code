# Caesar Cipher Program for Python2

from Tkinter import *


def cipher():
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    cipherlist = []
    plaintext = textentry.get()
    plaintext = plaintext.lower()
    shift = int(shiftentry.get())
                
    for c in plaintext:
        if c == ' ' or c == '.':
            cipherlist.append(c)
        else:
            count = 0
            for s in alphabet:
                if s != c:
                    count += 1
                else:
                    break
        cipherlist.append(alphabet[count + shift])
    ciphertext = ''.join(cipherlist)

    answindow = Tk()
    cipherlabel = Label(answindow,text = ciphertext, bg = "gray", fg = "red")
    cipherlabel.pack()
    answindow.mainloop()

window = Tk()
window.configure(background = "gray")

framet = Frame(window, height = 100)
framet.pack(side = TOP)

frameb = Frame(window, height = 100)
frameb.pack(side = BOTTOM)

heading = Label(window, text = 'Caesar Cipher', fg = "black", font = ("Courier", 36))
heading.pack(side = TOP)

textlabel = Label(window, text = 'Text:     ', fg = "black", font = ("Courier", 14))
textlabel.pack(side = LEFT)
textentry = Entry(window, bd = 4,bg = "green")
textentry.pack(side = LEFT)

shiftlabel = Label(window, text = '     Shift Number:     ', fg = "black", font = ("Courier", 14))
shiftlabel.pack(side = LEFT)
shiftentry = Entry(window, bd = 4, bg = "green")
shiftentry.pack(side = LEFT)

enterbutton = Button(window, text = "Get ciphered text!", command = cipher)
enterbutton.pack(side = BOTTOM)

window.mainloop()
