from tkinter import *
import tkinter
from tkinter import Tk, Canvas, Frame, BOTH
from Victory import Victory

root = Tk()
root.geometry("1920x1080")
root.title("Dominion Counter")
es_temp = PhotoImage(file = r"Images\background.png")
es = es_temp.zoom(2,2)
coun = Label(root, image = es)
coun.place(x=0, y = 0)

# Totals
totalduchy1 = 0
counter = tkinter.IntVar()
counter2 = tkinter.IntVar()

# Images
estate_temp = PhotoImage(file = r"Images\estate.png")
estate = estate_temp.subsample(3)
curse_temp = PhotoImage(file = r"Images\curse.png")
curse = curse_temp.subsample(3)
duchy_temp = PhotoImage(file = r"Images\duchy.png")
duchy = duchy_temp.subsample(3)
duke_temp = PhotoImage(file = r"Images\duke.png")
duke = duke_temp.subsample(3)
province_temp = PhotoImage(file = r"Images\province.png")
province = province_temp.subsample(3)
province_temp = PhotoImage(file = r"Images\colony.png")
colony = province_temp.subsample(3)

# Cards
curse_card = Victory("Curse", -1, 0, 0)
estate_card = Victory("Estate", 1, 2, 0)
duchy_card = Victory("Duchy", 3, 5, totalduchy1)
province_card = Victory("Province", 6, 8, 0)
colony_card = Victory("Colony", 10, 11, 0)


# Functions
# P1
def onClick(victory):
    counter.set(counter.get() + victory.value)
# P2
def onClickP2(victory):
    counter2.set(counter2.get() + victory.value)

counter_1 = Label(root, textvariable = counter, font = 'size, 80')
counter_2 = Label(root, textvariable = counter2, font = 'size, 80')
#root.wm_attributes("-transparent", "#FCF3CF")
counter_1.place(x=435, y = 200)
counter_2.place(x=1485, y = 200)

# Buttons
# P1
Button_curse = Button(root, command = lambda: onClick(curse_card), image = curse)
Button_estate = Button(root, command = lambda: onClick(estate_card), image = estate)
Button_duchy = Button(root, command = lambda: onClick(duchy_card), image = duchy)
Button_province = Button(root, command = lambda: onClick(province_card), image = province)
Button_colony = Button(root, command = lambda: onClick(colony_card), image = colony)
Button_duke = Button(root, command = lambda: onClick(), image = duke)
Button_curse.place(x=50, y=400)
Button_estate.place(x=250, y=400)
Button_duchy.place(x=450, y=400)
Button_duke.place(x=50, y=650)
Button_province.place(x=650, y=400)
Button_colony.place(x=250, y=650)
# P2
Button_curse2 = Button(root, text="Curses", command = lambda: onClickP2(curse_card), image = curse)
Button_estate2 = Button(root, text="Estate", command = lambda: onClickP2(estate_card), image = estate)
Button_duchy2 = Button(root, text="Duchy", command = lambda: onClickP2(duchy_card), image = duchy)
Button_province2 = Button(root, text="Province", command = lambda: onClickP2(province_card), image = province)
Button_colony2 = Button(root, text="Colony", command = lambda: onClickP2(colony_card), image = colony)
Button_curse2.place(x=1780, y=0)
Button_estate2.place(x=1780, y=200)
Button_duchy2.place(x=1780, y=400)
Button_province2.place(x=1780, y=600)
Button_colony2.place(x=1780, y=800)

can = Canvas(root, bg = 'black', height = 1080, width = 1)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()