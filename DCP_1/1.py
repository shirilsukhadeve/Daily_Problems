def isAvailable(myList, value):
    myDist = {}
    for i in myList:
        if (value-i) in myDist.keys():
            print "True"
            return
        else:
            myDist[i]=0;

isAvailable([10, 15, 3, 7], 17)
