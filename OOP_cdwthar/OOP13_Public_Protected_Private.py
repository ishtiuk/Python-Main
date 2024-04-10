
class Example:
    public = 8
    _protected = 38
    __private = 8787

    # def dfj(self):
    #     print(self.public)
    #     print(self._protected)
    #     print(self.__private)               # 'private' Attriubtes are accesable from anywhere of it's own Class, but it's not directly Accessable from any Object
                                            # or 'Child Class' , but yeah there is an Way...!!! 😎😎😎,             check the 39th Line>>>>>>>>>
    def access_private(self):
        return self.__private

tyii = Example()

class Pocket(Example):
    uy = 456454
    
    def dfj(self):
        print(self.public)
        print(self._protected)
        try:
            print(self.__private)
        except AttributeError as erer:
            print(erer)
            print("             ", self._Example__private)


yt = Pocket()
print(yt.public)
print(yt._protected)

try:
    print(yt.__private)
except AttributeError as atrERr:
    print(atrERr)

print(yt._Example__private)

yt.dfj()

print(yt.access_private())




