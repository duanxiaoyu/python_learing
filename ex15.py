#import a module
from sys import argv
#get argv
scriptname, filename = argv
#open a file
txt = open(filename)
print "here is yor file: %r" % filename
#read txt
print txt.read()

print "type the filename again:"
prompt = ">"
file_again = raw_input(prompt)

txt_again =open(file_again)
print "here is yor file: %r" % file_again
print txt_again.read()
