def f(nums):
    return len(list(set(nums))) != len(nums)
nums = list(eval(input()))
print(f(nums))