class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
    def action(self):
        return "не определно"
    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'
class Printer(Equipment):
    def __init__(self,series, name, make, year):
        super().__init__(name, make, year)
        self.series = series
    def action(self):
        return "Печатает"
    def __str__(self):
        return f'{self.series},{self.name}, {self.make}, {self.year}'
class Scaner(Equipment):
    def __init__(self,name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return "Сканирует"
class Xerox(Equipment):
    def __init__(self,name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return "Копирует"
def info(sklad):
    print("На складе имеется: ")
    for item in sklad:
        print(item)
        print(item.action())
def filter_printer(sklad, obj_type):
    for item in sklad:
        if isinstance(item, obj_type):
            print(item)
def remove_printer(sklad, obj_type):
    for item in sklad:
        if isinstance(item, obj_type):
            sklad.remove(item)
sklad = []
s = Scaner('samsung','lp 128',202)
sklad.append(s)
x = Xerox('HP','HP123',2020)
sklad.append(x)
p = Printer(34,'Epson','P 45',2020)
s = Scaner('asdasdadsads','lp 25555',2022)
sklad.append(s)
x = Xerox('HPqwe','HP1223413',2111020)
sklad.append(x)
p = Printer(32224,'Epso213n','P 4445',20331220)
sklad.append(p)
# info(sklad)
remove_printer(sklad, Scaner)
info(sklad)


