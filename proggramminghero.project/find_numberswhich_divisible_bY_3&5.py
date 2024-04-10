num_range = int(input())
result = []

for i in range(num_range):
    if i%3 == 0 and i%5 == 0:
        result.append(i)
print(result)
