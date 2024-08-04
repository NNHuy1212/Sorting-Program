def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        print("Error: Input list should not contain more than 20 integers.")
        print("-----------------------------------------------------------")
        return None

    # check if input list contains any non-positive integers
    if any(num < 0 for num in nums):
        print("Error: The input list should only contain positive integers.")
        print("-----------------------------------------------------------")
        return None
    
     # check if 0 is in the input list
    if 0 in nums:
        print ("Error: The number 0 is not a valid input.")
        print("-----------------------------------------------------------")
        return None


    nums = set(nums)
    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates and sort
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)

    return odd_nums, even_nums

while True:
    user_input = input("Enter a list of positive integers separated by spaces: ")
    try:
        nums = [int(num) for num in user_input.split()]
        result = split_and_sort(nums)
    except ValueError:
        print("Error: The input should only contain positive integers.")
        print("-----------------------------------------------------------")
        continue

    if result is None:
        continue
    else:
        odd_nums, even_nums = result
        print("Input:", nums)
        print("Odd numbers:", odd_nums)
        print("Even numbers:", even_nums)
        break
