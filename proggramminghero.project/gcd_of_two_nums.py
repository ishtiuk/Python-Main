# def gcd_finder_of_two_number(x, y):
#     smaller = min(x,y)
    
#     for i in range(1, smaller):
#         if x % i == 0 and y % i == 0:
#             gcd = i
    
#     return gcd


# nums1 = int(input("Enter first num: "))
# nums2 = int(input("Enter second num: "))
# print(gcd_finder_of_two_number(nums1, nums2))




def prime_detector(prime):
    for i in range(2, prime):
        if prime%i == 0:
            return False
    return True

    

number = int(input("Enter number: "))

if prime_detector(number):
    print("number is prime")

else:
    print("number is not prime")
