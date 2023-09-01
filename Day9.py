def maxsumhelper(nums, i ,j):
    if len(nums[i:j]) == 1:
        dp[i,j] = nums[i]
    else:
        dp[i,j] = max((dp[i+2,j-2] + nums[i] + nums[j]),(dp[i,j-2] + nums[j]),(dp[i+2,j] + nums[i]))

    

def maxsum(nums : list[int]) -> int:
    dp = [None * len(nums)] * len(nums)
    return 0

if __name__ == "__main__":
    print("Hello")