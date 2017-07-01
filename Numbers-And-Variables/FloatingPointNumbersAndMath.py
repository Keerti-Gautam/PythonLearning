print "Some Math here"
print "8%4: ", 8 % 4
print "8/4: ", 8 / 4
print "8*4: ", 8*4
print "8+4: ", 8+4
print "8-4: ", 8-4
print "56/13: ", 56/13

print "Notice that the last answer is in whole numbers. That is, the result is automatically floored. We need to use floating point numbers (i.e. with decimal points) to get these answers in floating point representation."
print "Let us see"
print "56.0/13.0: ", 56.0/13.0
print "Hooray!"
print "What is integer division or floor division?"
print "// is used for floor division which works in floats too."
print "56.0//13.0: ", 56.0//13.0
print "In all python version floor division remains same but normal division is different. Python 2.x versions will make 2/3 = 0 while 3.x versions will give the result as 0.6666."
print "If you want Py 2.x to behave like 3.x, just perform a from __future__ import division (with double underscores and spaces between from and import) and should occur at the beginning of the file like I have done in the next file named FromFutureImport.py"
