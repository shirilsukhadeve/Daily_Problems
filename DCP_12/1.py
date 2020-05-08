stepList = [1,2,3,4]
def nSteps(steps):
    if steps <= 1:
        return 1
    totalSteps = 0
    for n in stepList:
        totalSteps += nSteps(steps-n)

    return totalSteps

print(nSteps(4))