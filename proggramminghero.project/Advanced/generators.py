
# there are, a sort way to make or generated iterators is by using Generators......

# hence, we can make our own iterator class by defining the '__iter__()' and the '__next__()' method inside the Class.



# our most common and familiar in-build generator is our "range()" function, which we uses in 'for' loop 🤩..


#    ||||||||||||||          Generators          ||||||||||||||

# basically, "Generators" is a function which contains at least one "yield" keyword...
# like below....


def gen(num):
    for i in range(num+1):
        yield i


a = gen(4)

print(a.__next__())
print(next(a))
print(a.__next__())
print(next(a))
print(next(a))


#   factorial returner geneartor.....

def fac(n):
    facto = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            facto *= j

        yield facto

        facto = 1
        

a = fac(int(input()))
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
