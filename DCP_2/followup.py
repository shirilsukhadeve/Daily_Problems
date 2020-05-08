def array_multiply(numbers):
    array_len = len(numbers)
    new_list = []
    for n in range(0, array_len):
      multiplicaion = 1
      for m in range(0, array_len):
          if m != n:
            multiplicaion *= numbers[m]
      new_list.append(multiplicaion)
    print new_list

array_multiply([1, 2, 3, 4, 5])

def am1(numbers):
    array_len = len(numbers)
    new_list = []
    mult = 1
    for n in range(0, array_len):
      new_list.append(mult)
      mult *= numbers[n]
    mult = 1
    n = array_len-1
    for n in range(array_len-1, -1, -1):
      new_list[n] *= mult
      mult *= numbers[n]
    print new_list

am1([1, 2, 3, 4, 5])
