class Clock:
    __DAY = 86400

    def __init__(self, seconds:int):
        if not isinstance(seconds, int):
            raise TypeError('здесь нужен целый тип ')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{h} : {m} : {s}'
    def __lt__(self, other):
        if not isinstance(other, (int,Clock)):
            raise TypeError('неверный формат')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc
    def __le__(self, other):
        if not isinstance(other, (int,Clock)):
            raise  TypeError("Ne tot type")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc
    def __add__(self, other):
        if not isinstance(other, (int,Clock)):
            raise ArithmeticError('Можно сложить только целые числа ')
        sc = other if isinstance(other,int) else other.seconds
        return Clock(self.seconds + sc)
    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Можно сложить только целые числа ')
        sc = other if isinstance(other,int) else other.seconds
        self.seconds += sc
        return self



c1 = Clock(34255)
print(c1.get_time())
c2 = Clock(500)
# c3 = Clock(800)
# c1 = c1 + c2 + c3
c1 += c2
print(c1.get_time())
