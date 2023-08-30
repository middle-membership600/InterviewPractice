def SmartSol(msg : str) -> int:
    msglist = list(msg)
    def RecSol(msglist : list[int]) -> int:
        if not msglist:
            return 0
        elif len(msglist) == 1:
            return 1
        elif msglist[1] == '0':
            return 1 * RecSol(msglist[2:])
        elif msglist[0] >= '3':
            return 1 * RecSol(msglist[1:])
        else:
            return 1 + RecSol(msglist[1:]) + RecSol(msglist[2:])
    return RecSol(msglist)   

# not fully getting recursion

if __name__ == '__main__':
    print(SmartSol('12345'))