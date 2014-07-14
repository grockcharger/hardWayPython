# By guoshu 
# 2014/7/8 16:28

from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()

print "Ready, hit RETURN to continue, ^C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "done"

out_file.close()
