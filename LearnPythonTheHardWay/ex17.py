# -*- coding: utf-8 -*-
#Copy文件、判断文件长度len()、判断文件是否存在exists()
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

#we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exists? %r" %exists(to_file)
print "Ready,hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
out_file.write("Morning ")

print "Alright, all done."

out_file.close()
#in_file.close()
