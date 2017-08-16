# -*- coding:utf-8 -*-
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
#少了冒号
def print_first_word(words):
    """Prints the first word after popping it off."""
#pop写成poop
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
#少了反括号
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"
#此处数值不对
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
#/写成\
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# =写成了==,start_point写成了start-point
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#start_point写成start_pont，少了反括号
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

#good写成了god,wait写成weight,
sentence = "All good things come to those who wait."
#在文件中调用函数不需要加ex25.
words = break_words(sentence)
sorted_words = sort_words(words)
#
print_first_word(words)
print_last_word(words)
#此处多了.
print_first_word(sorted_words)
print_last_word(sorted_words)
#在文件中调用函数不需要加ex25.
sorted_words = sort_sentence(sentence)
#print书写不正确
print sorted_words
#first书写不正确
print_first_and_last(sentence)
#此处多了tab,and书写不正确,sentence书写不正确
print_first_and_last_sorted(sentence)
