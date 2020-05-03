import string
def myFunc(string):
    strSplit = string.split("\n")
    dirdist = {}

    for index in range(len(strSplit)):
        if not strSplit[index].find('\t'):
            print(len(strSplit[index]),strSplit[index], len(strSplit[index].strip('\t')))

        dirdist[strSplit[index]] = None

    print(dirdist)

if __name__ == '__main__':
    myFunc("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")