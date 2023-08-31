def SmartSol(msg : str) -> int:
    msglist = list(msg)
    total = 0
    def RecSol(msglist : list[int]) -> int:
        global total
        if msglist[0] == '0':
            return 0
        elif len(msglist) <= 1: # This covers empty string
            return 1
        if int(s[:2]) <= 26:
            total += RecSol(msglist[2:])

        total += RecSol(msglist[1:])
        
    return RecSol(msglist)   

# not fully getting recursion

if __name__ == '__main__':
    print(SmartSol('1111'))