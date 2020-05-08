def maxSum(list):
    incl = 0
    excl = 0
    for i in list:
        new_excl = excl if excl>incl else incl

        incl = excl + i
        excl = new_excl

    return (excl if excl>incl else incl)

if __name__=='__main__':
    print(maxSum([2, 4, 6, 2, 5]))