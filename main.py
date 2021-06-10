from tkinter import *


root = Tk()
root.geometry("1500x1000")
root.title("Dominion")




Bcurses = Button(root, text="Curses", padx=50, pady=50)
Bestate = Button(root, text="Estate", padx=50, pady=50)
Bduchy = Button(root, text="Duchy", padx=50, pady=50)
Bprovince = Button(root, text="Province", padx=50, pady=50)
Bcolony = Button(root, text="Colony", padx=50, pady=50)
Bcurses.place(x=0, y=0)
Bestate.place(x=0, y=250)
Bduchy.place(x=0, y=450)
Bprovince.place(x=0, y=600)
Bcolony.place(x=0, y=850)

Bcurses2 = Button(root, text="Curses", padx=50, pady=50)
Bestate2 = Button(root, text="Estate", padx=50, pady=50)
Bduchy2 = Button(root, text="Duchy", padx=50, pady=50)
Bprovince2 = Button(root, text="Province", padx=50, pady=50)
Bcolony2 = Button(root, text="Colony", padx=50, pady=50)
Bcurses2.place(x=1350, y=0)
Bestate2.place(x=1350, y=250)
Bduchy2.place(x=1350, y=450)
Bprovince2.place(x=1350, y=600)
Bcolony2.place(x=1350, y=850)


root.mainloop()