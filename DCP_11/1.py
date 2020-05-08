import string
def getSubstring(s1,s2):
    new_list = []
    for st in s2:
        s = st[:len(s1)]
        if s == s1:
            new_list.append(st)
    print(new_list)

getSubstring('de',['dog','deer','deal'])