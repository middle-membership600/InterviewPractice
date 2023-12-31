# only works when nums cannot contain a 0
def BruteForce(nums : list[int]) -> list[int]:
    res = [0] * len(nums)
    product = 1
    for i in nums:
        product *= i
    for i in range(len(res)):
        res[i] = product // nums[i]
    return res

# def SmartSol(nums : list[int]) -> list[int]:
#     prefix = [1] * len(nums)
#     prefix[0] = nums[0]
#     for i ,x  in enumerate(nums[1:]):
#         prefix[i + 1] = prefix[i] * x
#     postfix = [1] * len(nums)
#     postfix[-1] = nums[-1]
#     j = -2
#     while j >= -len(postfix):
#         postfix[j] = postfix[j + 1] * nums[j]
#         j -= 1
#     res = [1] * len(nums)
#     for i in range(len(res)):
#         if i != 0 and i != len(res) -1:
#             res[i] = prefix[i-1] * postfix[i+1]
#         elif i == 0:
#             res[i] = postfix[i+1]
#         elif i == len(res) -1:
#             res[i] = prefix[i-1]
#     return res

# This new approach is faster and more elegant because it doesn't compute the prefix arrays saving memory. The key realization
# is that the left prefix and right postfix multiplication don't have to happen at the same time. One pass multiplies all the indices by corresponding
# left prefix and another does right

# Still O(n) approach since we iterate only through the number of elements in the input nums

def SmartSol(nums : list[int]) -> list[int]:
    res = [1] * len(nums)
    reversenums = nums[::-1]
    l = 1
    r = 1
    for i in range(len(nums)):
        res[i] *= l
        l *= nums[i]
    for i in range(len(nums)):
        res[-(i+1)] *= r
        r *= reversenums[i]
    return res


# The SmartSol does not use division and acheives O(n) time complexity because it takes O(n) time to create each of the prefix and
# postfix arrays, and it takes O(n) time to make the res array because we only have to iterate through at most the number of elements in
# nums.

# This could definitely be read more elegantly and readable

if __name__ == "__main__":
    print(BruteForce([1,2,3,4,5]))
    print (SmartSol([1,2,3,4,5]))

   
    