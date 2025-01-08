import math
import random

def main():
    list_p = [0.62, 0.76, 0.75, 0.66, 0.81, 0.38, 0.44]
    p_no_cloud = 1.0
    for i in range(len(list_p)):
        p_no_cloud *= 1 - binom(list_p[i], 1, 1)
    print(p_no_cloud)

    cloud = [
        [(-50, -5), (-150, 0)], 
        [(-50, -5), (-70, 15)]
    ]
    sun = [
        [(-50, 50), (0, 0)], 
        [(-50, 50), (-70, 15)]
    ]

    outcome = []

    for i in range(len(cloud)):
        tempArr = []
        for j in range(len(cloud[i])):
            tempTuple = ((1 - p_no_cloud) * cloud[i][j][0] + p_no_cloud * sun[i][j][0], 
                         (1 - p_no_cloud) * cloud[i][j][1] + p_no_cloud * sun[i][j][1]
                        )
            tempArr.append(tempTuple)
        outcome.append(tempArr)

    #all_possible_choices = [outcome[0][0], outcome[0][1], outcome[1][0], outcome[1][1]]
    #for i in range(0, 100000):
#
    #    player1Choice = random.choice(outcome)[0]
    #    player2Choice = random.choice(outcome)[1]
    #    pass

    pretty2DPrint(outcome)
    return

def binom(proba:float, number:int, success_number:int):
    res = math.comb(number, success_number) * (proba ** success_number) * ((1 - proba) ** (number - success_number))
    return res

def binom_equal(proba:float, number:int, success_number:int):
    res = binom(proba, number, success_number)

    print("P( X = ", success_number, ") = ", res)
    return

def binom_inf(proba:float, number:int, success_number:int):
    res = 0
    for i in range(0, success_number):
        res += binom(proba, number, i)

    print("P( X < ", success_number, ") = ", res)
    return
def binom_inf_or_equal(proba:float, number:int, success_number:int):
    res = 0
    for i in range(0, success_number + 1):
        res += binom(proba, number, i)

    print("P( X <= ", success_number, ") = ", res)
    return

def binom_sup(proba:float, number:int, success_number:int):
    res = 0
    for i in range(success_number + 1, number + 1):
        res += binom(proba, number, i)

    print("P( X > ", success_number, ") = ", res)
    return

def binom_sup_or_equal(proba:float, number:int, success_number:int):
    res = 0
    for i in range(success_number, number + 1):
        res += binom(proba, number, i)

    print("P( X >= ", success_number, ") = ", res)
    return


def ponderation(value:float, factor:float):
    return value * factor

def pretty2DPrint(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

if(__name__ == "__main__"):
    main()