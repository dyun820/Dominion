from tkinter import *
import tkinter



root = Tk()
root.geometry("1500x1000")
root.title("Dominion")


counter = tkinter.IntVar()
def onClick(event=None):
    counter.set(counter.get() - 1)

def onClick2(event=None):
    counter.set(counter.get() + 1)

def onClick3(event=None):
    counter.set(counter.get() + 3)

def onClick4(event=None):
    counter.set(counter.get() + 6)

def onClick5(event=None):
    counter.set(counter.get() + 10)

counter2 = tkinter.IntVar()
def onClick6(event=None):
    counter2.set(counter2.get() - 1)

def onClick7(event=None):
    counter2.set(counter2.get() + 1)

def onClick8(event=None):
    counter2.set(counter2.get() + 3)

def onClick9(event=None):
    counter2.set(counter2.get() + 6)

def onClick10(event=None):
    counter2.set(counter2.get() + 10)


tkinter.Label(root, textvariable=counter).pack()
tkinter.Label(root, textvariable=counter2).pack()


# image = Image.open(file = r"C:\Users\Derek\Desktop\pythonProject\Province.png")
# # photo = PhotoImage(file = r"C:\Users\Derek\Desktop\pythonProject\Province.png")
# resize_image = image.resize((250, 250))
Bcurses = Button(root, text="Curses", command=onClick)
Bestate = Button(root, text="Estate", command=onClick2)
Bduchy = Button(root, text="Duchy", command=onClick3)
Bprovince = Button(root, text="Province", command=onClick4)
Bcolony = Button(root, text="Colony", command=onClick5)
Bcurses.place(x=0, y=0)
Bestate.place(x=0, y=250)
Bduchy.place(x=0, y=450)
Bprovince.place(x=0, y=600)
Bcolony.place(x=0, y=850)

Bcurses2 = Button(root, text="Curses", command=onClick6)
Bestate2 = Button(root, text="Estate", command=onClick7)
Bduchy2 = Button(root, text="Duchy", command=onClick8)
Bprovince2 = Button(root, text="Province", command=onClick9)
Bcolony2 = Button(root, text="Colony", command=onClick10)
Bcurses2.place(x=1350, y=0)
Bestate2.place(x=1350, y=250)
Bduchy2.place(x=1350, y=450)
Bprovince2.place(x=1350, y=600)
Bcolony2.place(x=1350, y=850)

root.mainloop()