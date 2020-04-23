class Node:
    def __init__(self, data):
        self.data =  data
        self.both = None

class LL:
      def __init__(self):
          self.head = None

      def add (self, data):
          newNode = Node(data)
          if self.head ==  None:
              self.head = newNode
          else:
              a = newNode
              print a
              print id(a)
              #print dereference_pointer (a)

      def get(self, index):
          print "node.data"


def main():
    Linked_list = LL()
    Linked_list.add(1)
    Linked_list.add(2)

if __name__ == "__main__":
    main()
