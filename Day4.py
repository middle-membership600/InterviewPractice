#O(n) Space
# def DumbSol (nums: list[int]) -> int:
#     solset = set()
#     for i in nums:
#         if i <= 1:
#             continue
#         if i in solset:
#             solset.remove(i)
#         solset.add(i + 1)
#         solset.add(i - 1)
#     return min(solset)

def DumbSol (nums: list[int]) -> int:
    s = set(nums)
    i = 1
    while i in s:
        i+=1
    return i

def SmartSol (nums: list[int]) -> int:
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            val = nums[i]
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
            if nums[i] == i + 1:
                break
    for i, num in enumerate(nums,1):
        if num != i:
            return i
    return len(nums) + 1

        

if __name__ == "__main__":
    # print("Hello World")
    print(DumbSol([3, 4, -1, 1]))
    print(SmartSol([3, 4, -1, 1]))
