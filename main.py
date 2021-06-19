


from tkinter import *
import tkinter
from tkinter import Tk, Canvas, Frame, BOTH

root = Tk()
root.geometry("1920x1080")
root.title("Dominion Counter")
# bg = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\background.png")
# background_image = bg.zoom(2,2)
# background_image.place(x = 0, y = 0)
# test1 = Label(root, bg = r"C:\Users\Derek\Desktop\DominionVictory\background.png")
# test1.place(x=0, y=0)
es_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\background.png")
es = es_temp.zoom(2,2)
coun = Label(root, image = es)
coun.place(x=0, y = 0)


estate_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\estate.png")
estate = estate_temp.subsample(3)
curse_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\curse.png")
curse = curse_temp.subsample(3)
duchy_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\duchy.png")
duchy = duchy_temp.subsample(3)
duke_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\duke.png")
duke = duke_temp.subsample(3)
province_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\province.png")
province = province_temp.subsample(3)
province_temp = PhotoImage(file = r"C:\Users\Derek\Desktop\DominionVictory\colony.png")
colony = province_temp.subsample(3)

totalduchy1 = 0

class Victory:
  def __init__(self, name, value, cost, total_duchy):
    self.name = name
    self.value = value
    self.cost = cost
    self.total_duchy = total_duchy
  def total():
  	global totalduchy1
  	totalduchy1 = totalduchy1 + 1


p1 = Victory("Estate", 1, 2, 0)
p2 = Victory("Duchy", 3, 5, totalduchy1)

print(p1.name)
print(p1.value)
print(p1.cost)
print(p2.name)
print(p2.value)
print(p2.cost)
print(p2.total_duchy)



total_duchy = 0

counter = tkinter.IntVar()
def onClick():
    counter.set(counter.get() - 1)
def onClick2():
    counter.set(counter.get() + 1)
def onClick3():
    counter.set(counter.get() + 3)
    global total_duchy
    total_duchy =  total_duchy + 1
def onClickduke():
    counter.set(counter.get() + total_duchy)
def onClick4():
    counter.set(counter.get() + 6)
def onClick5():
    counter.set(counter.get() + 10)

counter2 = tkinter.IntVar()
def onClick6():
    counter2.set(counter2.get() - 1)
def onClick7():
    counter2.set(counter2.get() + 1)
def onClick8():
    counter2.set(counter2.get() + 3)
def onClick9():
    counter2.set(counter2.get() + 6)
def onClick10():
    counter2.set(counter2.get() + 10)

counter_1 = Label(root, textvariable = counter, font = 'size, 80')
counter_2 = Label(root, textvariable = counter2, font = 'size, 80', bg = "#FCF3CF")
root.wm_attributes("-transparent", "#FCF3CF")
counter_1.place(x=435, y = 200)
counter_2.place(x=1485, y = 200)

Button_curse = Button(root, command=onClick, image = curse)
Button_estate = Button(root, command=onClick2, image = estate)
Button_duchy = Button(root, command=onClick3, image = duchy)
Button_province = Button(root, command=onClick4, image = province)
Button_colony = Button(root, command=onClick5, image = colony)
Button_duke = Button(root, command=onClickduke, image = duke)
Button_curse.place(x=50, y=400)
Button_estate.place(x=250, y=400)
Button_duchy.place(x=450, y=400)
Button_duke.place(x=50, y=650)
Button_province.place(x=650, y=400)
Button_colony.place(x=250, y=650)

Button_curse2 = Button(root, text="Curses", command=onClick6, image = curse)
Button_estate2 = Button(root, text="Estate", command=onClick7, image = estate)
Button_duchy2 = Button(root, text="Duchy", command=onClick8, image = duchy)
Button_province2 = Button(root, text="Province", command=onClick9, image = province)
Button_colony2 = Button(root, text="Colony", command=onClick10, image = colony)
Button_curse2.place(x=1780, y=0)
Button_estate2.place(x=1780, y=200)
Button_duchy2.place(x=1780, y=400)
Button_province2.place(x=1780, y=600)
Button_colony2.place(x=1780, y=800)

can = Canvas(root, bg = 'black', height = 1080, width = 1)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)

onClickduke()

root.mainloop()