def get_input():
    n = int(input())
    nums = [0] * n
    for i in range(n):
        nums[i] = int(input())
    return nums

def divideArray(nums):
        if len(nums) % 2 == 0:
            nums = sorted(nums)
            i = 0
            while i < len(nums):
                if nums[i] != nums[i+1]:
                    return False
                i += 2
            return True
        return False
nums = get_input()
print(divideArray(nums))
