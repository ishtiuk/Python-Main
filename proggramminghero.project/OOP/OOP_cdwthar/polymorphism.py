#
# the word "Polymorshism" means Multiple or Different Phases or Conditions. Not a Big Deal 😎

# but, we have to understand it Deeply later...

a = 7
print(a, type(a))

print(str(a), type(str(a)))

# here, 'a's Multiple Phases are present, like at first 'a' is 'int' and then 'str'

class A:
    # @property
    def meth(self):
        self.name = 'Smasher'
        print(self.name)

class B:

    def meth(self):
        self.name = 'Silverhand'
        print(self.name)

class C:

    def meth(self):
        self.name = 'Cyberpunk'
        print(self.name)

classes = [A(), B(), C()]

A().meth()

# print(a.meth)

for clses in classes:
    clses.meth()                    # 'meth()' Function/ Method's Polymorphism... 😉😉