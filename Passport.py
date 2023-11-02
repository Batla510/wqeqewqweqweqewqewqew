class Passport:
    def __init__(self,first_name,last_name,country,date_of_birth,numb_of_pasport):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.numb_of_pasport = numb_of_pasport

    def print_info(self):
        print(f'''Имя: {self.first_name}\nФамилия: {self.last_name}\nДата рождения: {self.date_of_birth}\nНомер паспорта: {self.numb_of_pasport}\nСтрана: {self.country}''')
class ForgeinPassport(Passport):
    def __init__(self,first_name,last_name,country,date_of_birth,numb_of_pasport,visa):
        super().__init__(first_name,last_name,country,date_of_birth,numb_of_pasport)
        self.visa = visa
    def print_info(self):
        super().print_info()
        print('Виза',self.visa)
def passportList(obj):
    return (obj.print_info())

p1 = Passport("Alex",'Sgfdfdg','Russia',"17.01.2007",123912939)
# p1.print_info()
fp = ForgeinPassport('Petrushka','Ivanov',"France","17.10.1999",1312123123, 'China')
# fp.print_info()
# print(passportList(p1))
# print(passportList(fp))
pl = []
pl.append(p1)
pl.append(fp)
for passport in pl:
    passport.print_info()

