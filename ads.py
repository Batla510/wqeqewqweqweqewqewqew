# class Point:
#     def __new__(cls, *args, **kwargs):
#         print(f"Вызов функции __new__ ждя {str(cls)}")
#         return super().__new__(cls)
#
#     def __init__(self,x,y):
#         print(f"Вызов функции __init__ ля {str(self)}")
#         self.x = x
#         self.y = y
# p = Point(1,5)
class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return  cls.__instance
    def __init__(self,user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port
    def connect(self):
        print(f'соединение с БД с настройками: user = {self.user}, psw = {self.psw},port = {self.port}')
    def close(self):
        print("Соединение разорвано")
    def read(self):
        print("Чтение данных")
    def write(self,data):
        print(f'Запись данных: {data}')
    def __del__(self):
       DataBase.__instance = None


d1 = DataBase("user1","psw1",3000)
d1.connect()
print(d1)
# del d1
d2 = DataBase("user1","psw1",3000)
d2.connect()
print(d2)