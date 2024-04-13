# Раньше (до изобретений классов) заводили очень много переменных под каждый предмет
# 3 космических корабля со своими характеристиками выглядели так

ship1_speed = 1
ship1_width = 3
ship1_height = 3

ship2_speed = 1
ship2_width = 3
ship2_height = 3

ship3_speed = 1
ship3_width = 3
ship3_height = 3
ship3_nitro = 5

class Ship():
    def __init__(self):
        self.speed = 1
        self.width = 3
        self.height = 3

class NitroShip(Ship):
    def __init__(self):
        Ship.__init__
        self.nitro = 5

ship1 = Ship()
ship2 = Ship()

ship3 = NitroShip()

ships = [ship1, ship2, ship3]

for i in range(1, 101):
    ships.insert(Ship())


for ship in ships:
    ship.speed += 5