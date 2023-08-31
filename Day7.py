def SmartSol(msg : str) -> int:
    memo = {}
    def RecSol(index: int) -> int:
        if index in memo:
            return memo[index]
        if index == len(msg):
            return 1
        if msg[index] == '0':
            return 0
        if index == len(msg) - 1:
            return 1
        
        if (int(msg[index] + msg[index + 1]) <= 26):
            memo[index] = RecSol(index + 1) + RecSol(index + 2)
        else:
            memo[index] = RecSol(index + 1) + RecSol(index + 2)
        return memo[index]

    
    return RecSol(0)

# not fully getting recursion

if __name__ == '__main__':
    print(SmartSol('1111'))