from tkinter import *
import tkinter
from tkinter import Tk, Canvas
from victory import Victory
from non_victory import NonVictory
import math

root = Tk()
root.geometry("1920x1080")
root.title("Dominion Counter")
background_temp = PhotoImage(file = r"Images\background.png")
background = background_temp.zoom(2,2)
bg_image = Label(root, image = background)
bg_image.place(x=0, y = 0)

# Totals
total_silver = 0
total_silver2 = 0
feodum_count = 0
feodum_count2 = 0
totalduchy1 = 0
totalduchy2 = 0
total_cards = 0
total_cards2 = 0
sr_count = 0
sr_count2 = 0
total_non_victory = 0
total_non_victory2 = 0
total_victory = 0
total_victory2 = 0
silk_road_count = 0
silk_road_count2 = 0
counter = tkinter.IntVar()
counter2 = tkinter.IntVar()

silver_temp = PhotoImage(file = r"Images\silver.png")
silver = silver_temp.subsample(5)
card_back_temp = PhotoImage(file = r"Images\card_back.png")
card_back = card_back_temp.subsample(3)
vp_symbol_temp = PhotoImage(file = r"Images\vp.png")
vp_symbol = vp_symbol_temp.zoom(3,3)

vp_plus_temp = PhotoImage(file = r"Images\vp_plus.png")
vp_plus = vp_plus_temp.subsample(14)
vp_minus_temp = PhotoImage(file = r"Images\vp_minus.png")
vp_minus = vp_minus_temp.subsample(5)
curse_temp = PhotoImage(file = r"Images\curse.png")
curse = curse_temp.subsample(3)
estate_temp = PhotoImage(file = r"Images\estate.png")
estate = estate_temp.subsample(3)
great_hall_temp = PhotoImage(file = r"Images\great_hall.png")
great_hall = great_hall_temp.subsample(3)
mill_temp = PhotoImage(file = r"Images\mill.png")
mill = mill_temp.subsample(3)
feodum_temp = PhotoImage(file = r"Images\Feodum.png")
feodum = feodum_temp.subsample(3)
silk_road_temp = PhotoImage(file = r"Images\silk_road.png")
silk_road = silk_road_temp.subsample(3)
castle_temp = PhotoImage(file = r"Images\castle1.png")
castle = castle_temp.subsample(3)
fairgrounds_temp = PhotoImage(file = r"Images\fairgrounds.png")
fairgrounds = fairgrounds_temp.subsample(3)
distant_lands_temp = PhotoImage(file = r"Images\distant_lands.png")
distant_lands = distant_lands_temp.subsample(3)
gardens_temp = PhotoImage(file = r"Images\gardens.png")
gardens = gardens_temp.subsample(3)
cemetery_temp = PhotoImage(file = r"Images\cemetery.png")
cemetery = cemetery_temp.subsample(3)
tunnel_temp = PhotoImage(file = r"Images\tunnel.png")
tunnel = tunnel_temp.subsample(3)
farmland_temp = PhotoImage(file = r"Images\farmland.png")
farmland = farmland_temp.subsample(3)
dame_josephine_temp = PhotoImage(file = r"Images\dame_josephine.png")
dame_josephine = dame_josephine_temp.subsample(3)
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

# Non Victory Cards
silver_card = NonVictory("Silver", 0)
card_back_card = NonVictory("Card Back", 1)
vp_plus_card = Victory("VP Plus", 1, 0)
vp_minus_card = Victory("VP Minus", -1, 0)

# Victory Cards
curse_card = Victory("Curse", -1, 0)
estate_card = Victory("Estate", 1, 2)
great_hall_card = Victory("Great Hall", 1, 3)
mill_card = Victory("Mill", 1, 4)
feodum_card = Victory("Feodum", total_silver, 4)
silk_road_card = Victory("Silk Road", total_victory, 4)
castle1_card = Victory("Castle 1", 1, 3)
castle1_2_card = Victory("Castle 1", 1, 3)
fairgrounds_card = Victory("Fairgrounds", 2, 5)
distant_lands_card = Victory("Distant Lands", 4, 5)
gardens_card = Victory("Gardens", total_non_victory, 4)
cemetery_card = Victory("Cemetery", 2, 4)
tunnel_card = Victory("Tunnel", 2, 5)
farmland_card = Victory("Farmland", 2, 6)
dame_josephine_card = Victory("Dame Josephine", 2, 5)
harem_card = Victory("Harem", 2, 6)
island_card = Victory("Island", 2, 4)
nobles_card = Victory("Nobles", 2, 6)
duchy_card = Victory("Duchy", 3, 5)
duke_card = Victory("Duke", totalduchy1, 5)
province_card = Victory("Province", 6, 8)
colony_card = Victory("Colony", 10, 11)


# Functions
# P1
def nvClick(nonvictory):
    global total_silver
    global feodum_count
    global total_non_victory
    if nonvictory.name == 'Silver':
        total_silver += 1
        feodum_count = math.floor(total_silver / 3)
    if nonvictory.name == 'Card Back':
        total_non_victory += 1
def onClick(victory):
    global totalduchy1
    global total_victory
    global silk_road_count
    global total_cards
    global sr_count
    counter.set(counter.get() + victory.value)
    if victory.name == 'Feodum':
        counter.set(counter.get() + feodum_count)
    if victory.value >= 0:
        total_victory += 1
        silk_road_count += 1
        sr_count = math.floor(silk_road_count / 4)
    if victory.name == 'Gardens':
        total_cards = math.floor((total_victory+total_non_victory)/10)
        counter.set(counter.get() + total_cards)
    if victory.name == 'Silk Road':
        counter.set(counter.get() + total_victory)
    if victory.name == 'Duchy':
        totalduchy1 += 1
    if victory.name == 'Duke':
        counter.set(counter.get() + totalduchy1)
# P2
def nvClickP2(nonvictory):
    global total_silver2
    global feodum_count2
    global total_non_victory2
    if nonvictory.name == 'Silver':
        total_silver2 += 1
        feodum_count2 = math.floor(total_silver2 / 3)
    if nonvictory.name == 'Card Back':
        total_non_victory2 += 1
def onClickP2(victory):
    global totalduchy2
    global total_victory2
    global total_silver2
    global silk_road_count2
    global sr_count2
    counter2.set(counter2.get() + victory.value)
    if victory.name == 'Feodum':
        counter2.set(counter2.get() + feodum_count2)
    if victory.value >= 0:
        total_victory2 += 1
        silk_road_count2 += 1
        sr_count2 = math.floor(silk_road_count2 / 4)
    if victory.name == 'Gardens':
        total_cards2 = math.floor((total_victory2+total_non_victory2)/10)
        counter2.set(counter2.get() + total_cards2)
    if victory.name == 'Silk Road':
        counter2.set(counter2.get() + total_victory2)
    if victory.name == 'Duchy':
        totalduchy1 += 1
    if victory.name == 'Duke':
        counter2.set(counter2.get() + totalduchy1)

# Totals
vp = Label(root, image = vp_symbol)
vp2 = Label(root, image = vp_symbol)
counter_1 = Label(root, textvariable = counter, font = 'size, 90')
counter_2 = Label(root, textvariable = counter2, font = 'size, 90')
vp.place(x= 120, y = 50)
vp2.place(x= 1725, y = 50)
counter_1.place(x=650, y = 10)
counter_2.place(x=1180, y = 0)

# Buttons
# P1
# Non Victory
Button_silver = Button(root, command = lambda: nvClick(silver_card), image = silver)
Button_card_back = Button(root, command = lambda: nvClick(card_back_card), image = card_back)
Button_vp_plus = Button(root, command = lambda: onClick(vp_plus_card), image = vp_plus)
Button_vp_minus = Button(root, command = lambda: onClick(vp_minus_card), image = vp_minus)

# Victory
Button_curse = Button(root, command = lambda: onClick(curse_card), image = curse)
Button_estate = Button(root, command = lambda: onClick(estate_card), image = estate)
Button_great_hall = Button(root, command = lambda: onClick(great_hall_card), image = great_hall)
Button_mill = Button(root, command = lambda: onClick(mill_card), image = mill)
Button_feodum = Button(root, command = lambda: onClick(feodum_card), image = feodum)
Button_silk_road = Button(root, command = lambda: onClick(silk_road_card), image = silk_road)
Button_castle1 = Button(root, command = lambda: onClick(castle1_card), image = castle)
Button_fairgrounds = Button(root, command = lambda: onClick(fairgrounds_card), image = fairgrounds)
Button_distant_lands = Button(root, command = lambda: onClick(distant_lands_card), image = distant_lands)
Button_gardens = Button(root, command = lambda: onClick(gardens_card), image = gardens)
Button_cemetery = Button(root, command = lambda: onClick(cemetery_card), image = cemetery)
Button_tunnel = Button(root, command = lambda: onClick(tunnel_card), image = tunnel)
Button_farmland = Button(root, command = lambda: onClick(farmland_card), image = farmland)
Button_dame_josephine = Button(root, command = lambda: onClick(dame_josephine_card), image = dame_josephine)
Button_harem = Button(root, command = lambda: onClick(harem_card), image = harem)
Button_island = Button(root, command = lambda: onClick(island_card), image = island)
Button_nobles = Button(root, command = lambda: onClick(nobles_card), image = nobles)
Button_duchy = Button(root, command = lambda: onClick(duchy_card), image = duchy)
Button_duke = Button(root, command = lambda: onClick(duke_card), image = duke)
Button_province = Button(root, command = lambda: onClick(province_card), image = province)
Button_colony = Button(root, command = lambda: onClick(colony_card), image = colony)
Button_vp_minus.place(x=50, y=50)
Button_vp_plus.place(x=185, y=50)
Button_card_back.place(x=490, y=10)
Button_silver.place(x=347, y=10)
Button_curse.place(x=20, y=150)
Button_estate.place(x=170, y=150)
Button_great_hall.place(x=320, y=150)
Button_mill.place(x=470, y=150)
Button_feodum.place(x=620, y=150)
Button_silk_road.place(x=770, y=150)
Button_castle1.place(x=20, y=370)
Button_fairgrounds.place(x=170, y=370)
Button_distant_lands.place(x=320, y=370)
Button_gardens.place(x=470, y=370)
Button_cemetery.place(x=620, y=370)
Button_tunnel.place(x=770, y=370)
Button_farmland.place(x=20, y=590)
Button_dame_josephine.place(x=170, y=590)
Button_harem.place(x=320, y=590)
Button_island.place(x=470, y=590)
Button_nobles.place(x=620, y=590)
Button_duchy.place(x=770, y=590)
Button_duke.place(x=20, y=810)
Button_province.place(x=170, y=810)
Button_colony.place(x=320, y=810)

# P2
# Non Victory
Button_silver2 = Button(root, command = lambda: nvClickP2(silver_card), image = silver)
Button_card_back2 = Button(root, command = lambda: nvClickP2(card_back_card), image = card_back)
# Victory
Button_vp_plus2 = Button(root, command = lambda: onClickP2(vp_plus_card), image = vp_plus)
Button_vp_minus2 = Button(root, command = lambda: onClickP2(vp_minus_card), image = vp_minus)
Button_curse2 = Button(root, command = lambda: onClickP2(curse_card), image = curse)
Button_estate2 = Button(root, command = lambda: onClickP2(estate_card), image = estate)
Button_great_hall2 = Button(root, command = lambda: onClickP2(great_hall_card), image = great_hall)
Button_mill2 = Button(root, command = lambda: onClickP2(mill_card), image = mill)
Button_feodum = Button(root, command = lambda: onClickP2(feodum_card), image = feodum)
Button_silk_road2 = Button(root, command = lambda: onClickP2(silk_road_card), image = silk_road)
Button_castle1_2 = Button(root, command = lambda: onClickP2(castle1_2_card), image = castle)
Button_fairgrounds2 = Button(root, command = lambda: onClickP2(fairgrounds_card), image = fairgrounds)
Button_distant_lands2 = Button(root, command = lambda: onClickP2(distant_lands_card), image = distant_lands)
Button_gardens2 = Button(root, command = lambda: onClickP2(gardens_card), image = gardens)
Button_cemetery2 = Button(root, command = lambda: onClickP2(cemetery_card), image = cemetery)
Button_tunnel2 = Button(root, command = lambda: onClickP2(tunnel_card), image = tunnel)
Button_farmland2 = Button(root, command = lambda: onClickP2(farmland_card), image = farmland)
Button_dame_josephine2 = Button(root, command = lambda: onClickP2(dame_josephine_card), image = dame_josephine)
Button_harem2 = Button(root, command = lambda: onClickP2(harem_card), image = harem)
Button_island2 = Button(root, command = lambda: onClickP2(island_card), image = island)
Button_nobles2 = Button(root, command = lambda: onClickP2(nobles_card), image = nobles)
Button_duchy2 = Button(root, command = lambda: onClickP2(duchy_card), image = duchy)
Button_duke2 = Button(root, command = lambda: onClickP2(duke_card), image = duke)
Button_province2 = Button(root, command = lambda: onClickP2(province_card), image = province)
Button_colony2 = Button(root, command = lambda: onClickP2(colony_card), image = colony)
Button_vp_minus2.place(x=1650, y=50)
Button_vp_plus2.place(x=1785, y=50)
Button_card_back2.place(x=1330, y=10)
Button_silver2.place(x=1473, y=10)
Button_curse2.place(x=1000, y=150)
Button_estate2.place(x=1150, y=150)
Button_great_hall2.place(x=1300, y=150)
Button_mill2.place(x=1450, y=150)
Button_feodum.place(x=1600, y=150)
Button_silk_road2.place(x=1750, y=150)
Button_castle1_2.place(x=1000, y=370)
Button_fairgrounds2.place(x=1159, y=370)
Button_distant_lands2.place(x=1300, y=370)
Button_gardens2.place(x=1450, y=370)
Button_cemetery2.place(x=1600, y=370)
Button_tunnel2.place(x=1750, y=370)
Button_farmland2.place(x=1000, y=590)
Button_dame_josephine2.place(x=1150, y=590)
Button_harem2.place(x=1300, y=590)
Button_island2.place(x=1450, y=590)
Button_nobles2.place(x=1600, y=590)
Button_duchy2.place(x=1750, y=590)
Button_duke2.place(x=1000, y=810)
Button_province2.place(x=1150, y=810)
Button_colony2.place(x=1300, y=810)

can = Canvas(root, bg = 'black', height = 1080, width = 1)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()