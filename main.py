from tkinter import *
import tkinter
from tkinter import Tk, Canvas
from Victory import Victory

root = Tk()
root.geometry("1920x1080")
root.title("Dominion Counter")
es_temp = PhotoImage(file = r"Images\background.png")
es = es_temp.zoom(2,2)
coun = Label(root, image = es)
coun.place(x=0, y = 0)

# Totals
total_silver = 0
totalduchy1 = 0
totalduchy2 = 0
total_victory = 0
total_victory2 = 0
counter = tkinter.IntVar()
counter2 = tkinter.IntVar()


curse_temp = PhotoImage(file = r"Images\curse.png")
curse = curse_temp.subsample(3)
estate_temp = PhotoImage(file = r"Images\estate.png")
estate = estate_temp.subsample(3)
feodum_temp = PhotoImage(file = r"Images\feodum.png")
feodum = feodum_temp.subsample(3)
silk_road_temp = PhotoImage(file = r"Images\silk_road.png")
silk_road = silk_road_temp.subsample(3)
mill_temp = PhotoImage(file = r"Images\mill.png")
mill = mill_temp.subsample(3)
harem_temp = PhotoImage(file = r"Images\harem.png")
harem = harem_temp.subsample(3)
island_temp = PhotoImage(file = r"Images\island.png")
island = island_temp.subsample(3)
nobles_temp = PhotoImage(file = r"Images\nobles.png")
nobles = nobles_temp.subsample(3)
duchy_temp = PhotoImage(file = r"Images\duchy.png")
duchy = duchy_temp.subsample(3)
duke_temp = PhotoImage(file = r"Images\duke.png")
duke = duke_temp.subsample(3)
province_temp = PhotoImage(file = r"Images\province.png")
province = province_temp.subsample(3)
province_temp = PhotoImage(file = r"Images\colony.png")
colony = province_temp.subsample(3)

# Cards
curse_card = Victory("Curse", -1, 0)
estate_card = Victory("Estate", 1, 2)
feodum_card = Victory("Feodum", total_silver, 4)
silk_road_card = Victory("Silk Road", total_victory, 4)
mill_card = Victory("Mill", 1, 4)
harem_card = Victory("Harem", 2, 6)
island_card = Victory("Island", 2, 4)
nobles_card = Victory("Nobles", 2, 6)
duchy_card = Victory("Duchy", 3, 5)
duke_card = Victory("Duke", totalduchy1, 5)
province_card = Victory("Province", 6, 8)
colony_card = Victory("Colony", 10, 11)


# Functions
# P1
def onClick(victory):
    global totalduchy1
    global total_victory
    counter.set(counter.get() + victory.value)
    if victory.value > 0:
        total_victory += 1
    if victory.name == 'Silk Road':
        counter.set(counter.get() + total_victory)
    if victory.name == 'Duchy':
        totalduchy1 += 1
    if victory.name == 'Duke':
        counter.set(counter.get() + totalduchy1)
# P2
def onClickP2(victory):
    global totalduchy2
    global total_victory2
    counter2.set(counter2.get() + victory.value)
    if victory.value >= 1:
        total_victory.set(counter.get() + 1)
    if victory.name == 'Silk Road':
        counter2.set(counter2.get() + total_victory2)
    if victory.name == 'Duchy':
        totalduchy1 += 1
    if victory.name == 'Duke':
        counter2.set(counter2.get() + totalduchy1)


counter_1 = Label(root, textvariable = counter, font = 'size, 80')
counter_2 = Label(root, textvariable = counter2, font = 'size, 80')
#root.wm_attributes("-transparent", "#FCF3CF")
counter_1.place(x=435, y = 200)
counter_2.place(x=1485, y = 200)

# Buttons
# P1
Button_curse = Button(root, command = lambda: onClick(curse_card), image = curse)
Button_estate = Button(root, command = lambda: onClick(estate_card), image = estate)
Button_mill = Button(root, command = lambda: onClick(mill_card), image = mill)
Button_silk_road = Button(root, command = lambda: onClick(silk_road_card), image = silk_road)
Button_harem = Button(root, command = lambda: onClick(harem_card), image = harem)
Button_island = Button(root, command = lambda: onClick(island_card), image = island)
Button_nobles = Button(root, command = lambda: onClick(nobles_card), image = nobles)
Button_duchy = Button(root, command = lambda: onClick(duchy_card), image = duchy)
Button_duke = Button(root, command = lambda: onClick(duke_card), image = duke)
Button_province = Button(root, command = lambda: onClick(province_card), image = province)
Button_colony = Button(root, command = lambda: onClick(colony_card), image = colony)
Button_curse.place(x=20, y=400)
Button_estate.place(x=170, y=400)
Button_mill.place(x=320, y=400)
Button_silk_road.place(x=470, y=400)
# Button_harem.place(x=620, y=400)
Button_island.place(x=620, y=400)
Button_nobles.place(x=770, y=400)
Button_duchy.place(x=20, y=650)
Button_duke.place(x=170, y=650)
Button_province.place(x=320, y=650)
Button_colony.place(x=470, y=650)
# P2
Button_curse2 = Button(root, command = lambda: onClickP2(curse_card), image = curse)
Button_estate2 = Button(root, command = lambda: onClickP2(estate_card), image = estate)
Button_mill2 = Button(root, command = lambda: onClick(mill_card), image = mill)
Button_harem2 = Button(root, command = lambda: onClick(harem_card), image = harem)
Button_island2 = Button(root, command = lambda: onClick(island_card), image = island)
Button_nobles2 = Button(root, command = lambda: onClick(nobles_card), image = nobles)
Button_duchy2 = Button(root, command = lambda: onClickP2(duchy_card), image = duchy)
Button_duke2 = Button(root, command = lambda: onClickP2(duke_card), image = duke)
Button_province2 = Button(root, command = lambda: onClickP2(province_card), image = province)
Button_colony2 = Button(root, command = lambda: onClickP2(colony_card), image = colony)
Button_curse2.place(x=1050, y=400)
Button_estate2.place(x=1250, y=400)
Button_duchy2.place(x=1450, y=400)
Button_duke2.place(x=1650, y=400)
Button_province2.place(x=1050, y=650)
Button_colony2.place(x=1250, y=650)

can = Canvas(root, bg = 'black', height = 1080, width = 1)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()