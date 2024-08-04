def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."

    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."

    nums = set(nums)
    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates and sort
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)

    return odd_nums, even_nums

nums = [9, 6, 12, 12, 3, 1, 5, 5, 7, 2]
odd_nums, even_nums = split_and_sort(nums)

print("Input:", nums)
print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)
