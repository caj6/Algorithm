import math

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

    pretty2DPrint(outcome)
    print(nash(outcome))
    return

def binom(proba:float, number:int, success_number:int):
    res = math.comb(number, success_number) * (proba ** success_number) * ((1 - proba) ** (number - success_number))
    return res

def nash(matrix):
    bestP1Line = -math.inf
    bestP2Line = -math.inf
    bestIndex = (0, 0)

    for i in range(len(matrix)):
        bestP1Line = max(bestP1Line, matrix[i][0][0] + matrix[i][1][0])
        bestIndex = (i, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            bestP2Line = max(bestP2Line, matrix[0][j][1] + matrix[1][j][1])
            bestIndex = (bestIndex[0], j)

    return bestIndex

def pretty2DPrint(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

if(__name__ == "__main__"):
    main()