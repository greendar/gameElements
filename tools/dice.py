import random as r 


def d4(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,4))
    return rollsOut

def d6(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,6))
    return rollsOut


def d8(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,8))
    return rollsOut

def d10(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,10))
    return rollsOut

def d12(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,12))
    return rollsOut

def d20(n = 1):
    rollsOut = []
    for i in range(n):
        rollsOut.append(r.randint(1,20))
    return rollsOut
