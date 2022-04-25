def get_input():
    n = int(input())
    nums = [0] * n
    for i in range(n):
        nums[i] = int(input())
    return nums
def maxProduct(nums):
        max_product = nums[0] * nums[1]
        for i in range(len(nums)-1):
            product = nums[i] * nums[i+1]
            if product >= max_product:
                max_product = product
            for j in range(i+2,len(nums)):
                product *= nums[j]
                if product >= max_product:
                    max_product = product
                else:
                    break
        return max_product
nums = get_input()
print(maxProduct(nums))