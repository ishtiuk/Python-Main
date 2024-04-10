def divisible_by3and5(num):
    result = []
    for i in range(num):
    #or for i in range(0, num): --> this will do the same thing
        if i%3 == 0 and i%5 == 0:
            result.append(i)
    return result

numrid = int(input("Enter number range: "))
num = divisible_by3and5(numrid)
#or print(divisible_by3and5(numrid)) --> this will do same thing, it will do the two works in one line.
print(num)