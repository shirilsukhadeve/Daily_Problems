def ar(numbers):
    positive_number_start = 0
    length = len(numbers)
    for n in range(length):
        temp = 0
        if numbers[n]<0:
            temp = numbers[positive_number_start]
            numbers[positive_number_start] = numbers[n]
            numbers[n] = temp
            positive_number_start+=1

    for n in range(length):
      if (abs(numbers[n]) - 1 < length and numbers[abs(numbers[n]) - 1] > 0):
        numbers[abs(numbers[n]) - 1] = -numbers[abs(numbers[n]) - 1]

    for n in range(length):
      if (numbers[n] > 0):
        print n + 1
        return
    print length
    return

ar([1, 2, 0])
ar([3, 4, -1, 1])
