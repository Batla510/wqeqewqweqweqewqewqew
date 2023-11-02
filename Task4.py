class dis:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def Distance(self):
        a = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        b = ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**0.5
        c = ((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2)**0.5
        print(abs(a) + abs(b) + abs(c))
Tr = dis(2,4,6,9,6,0)
Tr.Distance()