# By guoshu
# 2014/7/8 13:50

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit (^C)"
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file ..."
target = open(filename,'w')

print "Truncateing the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for Three lines."

line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close the file."
target.close()

