def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  
    ans = 0
    for num in nums:
      ans += num
    return ans


print("sum_nums returned", sum_nums([1, 2, 3, 4]))
