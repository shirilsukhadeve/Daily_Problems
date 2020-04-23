def array_multiply(numbers):
    multiplicaion = 1
    for n in numbers:
        multiplicaion *= n
    new_list = []
    for n in numbers:
        new_list.append(multiplicaion/n)
    print new_list

array_multiply([1, 2, 3, 4, 5])
