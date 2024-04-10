class Ran:
    def gen(self, l, u):
        self.l = l
        self.u = u
        
        if self.l > 0:
            for i in range(l, u):
                yield i

        else:
            for i in range(u):
                yield i


for i in Ran().gen(0, 7):
    print(i)
