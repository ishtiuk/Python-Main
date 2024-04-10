def second_smallest(nums):
    first_smallest = nums[0]
    second_smallest = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest

num_list = [4,5,3]
print(second_smallest(num_list))