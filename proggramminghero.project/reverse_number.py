def reverse_number(num):
    reverse = 0
    while num > 0:
        last_num = num % 10
        reverse = reverse * 10 + last_num
        num = num // 10
                                                                                # but this algorithom has one vulnerabily that is if "0" contains at the first of the number like: 014505
                                                                                # then this algorithom cann't reverse the number correnctly it will bypass the first '0' of the number like: 14505
                                                                                # because it's an mathmatical algorithom. 
                                                                                # so, to reverse any number even number contains '0' at first like: 0544504154
                                                                                # use have to use the algorithoms which we use to reverse stings.
    return reverse                                                                          

inp = int(input("Enter a number to reverese: "))                                                                            
print("Reversed number: ", reverse_number(inp))                                                 