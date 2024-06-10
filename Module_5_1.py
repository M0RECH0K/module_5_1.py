class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = None

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors:
            print('Такого этажа/дома не существует')
        else:
            for i in range(1, self.new_floor + 1):
                print(i)


h1 = House('ЖК Жемчужный', 11)
h2 = House('Дом у моря', 5)
h1.go_to(3)
h2.go_to(6)
