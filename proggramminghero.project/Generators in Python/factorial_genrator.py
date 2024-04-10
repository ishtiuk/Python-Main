
def fac(n):
    facto = 1

    for j in range(1, n+1):
        for i in range(1, j+1):
            facto *= i

        yield facto
        facto = 1

gen = fac(10)

print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
