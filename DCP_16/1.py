class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Log:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        temp = self.root
        while temp.next != None:
            temp = temp.next
        new = Node(data)
        temp.next = new

    def print(self,index):
        temp = self.root
        while index > 0 and temp != None:
            print(temp.data)
            index -= 1
            temp = temp.next

if __name__ == '__main__':
    newLog = Log()
    newLog.add(1)
    newLog.add(2)
    newLog.add(3)
    newLog.add(4)
    newLog.add(5)
    newLog.add(6)
    newLog.add(7)
    newLog.add(8)
    newLog.add(9)

    newLog.print(20)

