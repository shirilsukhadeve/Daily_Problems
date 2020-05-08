class Node:
    def __init__(self, val, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

class Tree:

    def __init__(self):
        self.root = None

    def serialize(self):
        print "serialize"

    def des(self, string):
        print string

    def getRoot(self):
        return self.root


def main():
    string = raw_input("please in put string:")
    abc = Tree()
    a = abc.des(string)

if __name__=='__main__':
    main()
