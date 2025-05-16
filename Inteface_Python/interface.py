
from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='gato.gif').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá seu tonto!')
text.pack(side=BOTTOM)
root.mainloop()