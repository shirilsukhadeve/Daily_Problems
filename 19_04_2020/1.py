def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(num):
    def left(a,b):
        return a
    return num(left)

def cdr(num):
    def right(a,b):
        return b
    return num(right)

print car(cons(1,2))
print cdr(cons(1,2))
