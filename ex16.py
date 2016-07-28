from sys import argv
scritp, filename = argv
print "we are going to erase %s" % filename
print "if you don't want do that, hit CTRL-C(^C)."
print "If you do want do that hit enter."

raw_input("?")

print "Opennint the file..."
target = open(filename, 'w')

print "truncating the file, goodbye!"
target.truncate()

print "I'm going to ask you three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to wright this to the file"

target.write(" %s \n  %s" % (line1, line2))

target.close()


