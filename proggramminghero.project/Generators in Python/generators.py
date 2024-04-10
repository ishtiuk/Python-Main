

#   Generators is nothing but a Holder, cause it holds datas at advance. 

# we have already used the most popular Generator 'range' in Python...

# like below...
import time


for i in range(355):
    i

# here, the for loop looping for 0 to 10 and printing this, but it has no pre-stored data, right? 
# so, it's using our Memory or RAM 😏, boring....... our Computer going to be slow for this.....


# so, here comes the concept of Generator, 😁 Generator basically generates value on the fly and gets ready with those datas and we can call that anytime and use them.
# so, that our RAM will not use more .........

# Generator

def gen(n):
    for i in range(n):
        yield i

gen1 = gen(355)
print(gen1)

print(gen1.__next__())              # iterable
print(gen1.__next__())              
print(gen1.__next__())


m = 'hello'
gen_m = iter(m)                     # iterator || we have used 'iter(m)' to convert 'str' to 'iterator', otherwise we can't use the '__next__()' function on 'str'
print(gen_m)
print(gen_m.__next__())
print(gen_m.__next__())
print(gen_m.__next__())