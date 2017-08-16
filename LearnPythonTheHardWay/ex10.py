# -*- coding: utf-8 -*-
#转义字符
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "\u'\U0001F47E' I'm \\a \\ cat."

test = 10
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Test
print "aa \r\t %d qq." % test
print "%r'%s""" %("sss123","May")


while  True:
    for  i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
