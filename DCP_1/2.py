def isAvailable(myList, value):
    myList=set(myList)
    for i in myList:
        if (value-i) in myList:
            print "True"
            return
    print "False"
isAvailable([10, 15, 3, 7], 19)
