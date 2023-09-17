import random

def appendLast(dig):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    last = random.choice(nums)

    full = str(last) + str(last)
    full = int(full)

    return full


def EcoVitality(enviromental):
    if enviromental >= 60:
        weights = [0, 0, 0, 0, 0, 0, 2, 2, 4, 2]
    elif enviromental >= 50 & enviromental <= 59:
        weights = [0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 1]
    elif enviromental >=40 & enviromental <= 49:
        weights = [0, 0, 1, 1, 1, 2, 2, 1, 0, 0, 0]
    elif enviromental >= 30 & enviromental <= 39:
        weights = [1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0]
    elif enviromental >= 20 & enviromental <= 29:
        weights = [1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]
    else:
        weights = [3, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    firstDig = random.choices(nums, weights, k=1)
    firstDig = firstDig[0]
    full = appendLast(firstDig)
    return full

def NatureHarmony(enviromental):
    full = EcoVitality(enviromental)/2
    return full