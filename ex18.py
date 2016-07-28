#print two args like script
def print_two(*args):
    arg1, arg2 = args
    print "arg1 = %s, arg2 = %s" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1 = %s, arg2 = %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1 = %s" % arg1


print_two("hello", "world")
print_two_again("hello", "world")
print_one("OK")
