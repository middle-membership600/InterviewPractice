from collections import defaultdict

def BruteForce(nums: list, k : int) -> bool:
    for i, x  in enumerate(nums):
        for y in nums[i+1:]:
            if x + y == k:
                return True
    return False

def SmartSol(nums: list, k : int) -> bool:
    valdict = set()
    for i in nums:
        residual = k - i
        if residual in valdict:
            return True
        else:
            valdict.add(i)
    return False

if __name__ == "__main__":
    print(BruteForce([10,5], 15))
    print(SmartSol([10,5], 15))

