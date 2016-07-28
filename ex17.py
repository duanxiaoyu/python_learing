from sys import argv
from os.path import exists

scritp, from_file, to_file = argv

print "copy from %s to %s" % (from_file, to_file)
in_file = open(from_file)
in_data = in_file.read()

print "the in_file is %d long" % len(in_data)

print "Does the to_file exists? %s" % exists(to_file)
print "Hit enter to continue, hit CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "All right done"

in_file.close()
out_file.close()
