
from Tkinter import *
import Tkinter as tk
import os

root = tk.Tk()
root.resizable(width=False, height=False)

w = Label(root, text="BLINK WRITER",bg="gold",font=("Helvetica", 20))
w.pack()
w = Label(root, text="\n\n1. The matrix of alphabets/words will appear in front of you.",font=("Helvetica", 16))
w.pack()

w = Label(root, text="\n2. First you have to select the row of the letter/word you want to choose and then the letter",font=("Helvetica", 16))
w.pack()


w = Label(root, text="\n3. Close your eyes for atleast one second to make a selection \n",font=("Helvetica", 16))

w.pack()
w = Label(root, text="\n4. See the lower half of the screen without blinking for atleast 3 seconds after you have pressed GOT IT\n\n\n\n",font=("Helvetica", 16))

w.pack()



root.geometry('{}x{}'.format(1000, 500))
def myfunc():

	q=1
def quit():
    root.destroy()
    os.system("sh a.sh")
    
b = Button(root, text="GOT IT",fg="white", command=quit,bg="Black",padx=20,pady=10)
b.pack()


mainloop()
