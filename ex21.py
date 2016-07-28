def add(a, b):
    print "%d + %d " % (a, b)
    return a + b

def sub(a, b):
    print "%d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "%d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "%d / %d" % (a, b)
    return a / b
print "do some math"

height = int( sub(189, 27))
weight = multiply(60, 2)
age = add(20, 6)
iq = divide(300, 2)

print "hei = %r   wei = %d  age = %d  iq = %d " % (height, weight, age, iq)

    
