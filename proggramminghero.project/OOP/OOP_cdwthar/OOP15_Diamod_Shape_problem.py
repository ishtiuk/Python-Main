
class A:
    def method(self):
        print("This is a method from class A")   # 'Diamond Shape Problem' is just a Confusion that causes by using of 'Multiple Inheritance'
                                                 # that's it
class B(A):
    # def method(self):
    #     print("This is a method from class B")
        pass

class C(A):
    def method(self):
        print("This is a method from class C")
        pass

class D(B, C):
    # def method(self):
    #     print("This is a method from class D")
        pass

                                    # 'Diamond Shape Problem' can easily solvable in Python,

                                    # but, other languages like: 'JAVA' don't allow 'Multiple Inheritance' 
                                    # to avoid 'Diamond Shape Problem'...!!!


                                    # Python & C++ allow 'Multiple Inheritance'

a = A()
b = B()
c = C()
d = D()


d.method()