def compute(arr, lenArr):
    if lenArr >len(arr):
        print("Window value greater than the array")
    for i in range(len(arr)+1-lenArr):
        j = i + lenArr
        print("max among:",arr[i:j], "is", max(arr[i:j]) )

if __name__ == '__main__':
    compute([10, 5, 2, 7, 8, 7], 6)
