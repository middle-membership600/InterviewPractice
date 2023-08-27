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

def DumbSol (nums: list[int]) -> int:

    return 0

        

if __name__ == "__main__":
    # print("Hello World")
    print(DumbSol([3, 4, -1, 1]))
