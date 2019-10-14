class Base():
    a = 1
    
    def __init__(self):
        self.b = 2
        
    def tempo(self):
        self.c = 3
        #print(self.c)
        
    def fun(self):
        print(self)
        self.tempo()
        print(Base.a, self.a, self.b, self.c)

class Super():
    c = 30
    def __init__(self):
        #self.b =  20
        self.d = 40
        print('in super.init', self)
    def action(self):
        print('haaaaa')
    def delegate(self):
        print('in delegate', self, self.a, self.b, self.c, self.d)
        self.action()
        
class Provider(Super):
    a=10
    def __init__(self):
        print('in prov.init')
        super().__init__()
        self.b = 20
    def action(self):
        #self.b = 20
        print('in action', self)


if __name__ == '__main__':
    x = Base()
    x.fun()
    #x.tempo()
    y = Provider()
    y.delegate()