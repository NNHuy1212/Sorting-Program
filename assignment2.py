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

# Get user input for the list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
nums = [int(num) for num in user_input.split()]

result = split_and_sort(nums)

if isinstance(result, str):
    print(result)
else:
    odd_nums, even_nums = result
    print("Input:", nums)
    print("Odd numbers:", odd_nums)
    print("Even numbers:", even_nums)
