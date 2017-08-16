# -*- coding:utf-8 -*-
class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        #print "self.subject:", subject
        self.verb = verb[1]
        self.object = obj[1]

# peek a list of words and return what type of word it is
# 返回当前word_list的类型
def peek(word_list):
        if word_list:
            #print "peek word_list:",word_list
            # 返回第一组tuple数据
            word = word_list[0]
            #print word[0]----word[0]对应类型，word[1]对应值
            #返回word[0]的类型
            return word[0]
        else:
            return None

#弹出当前的tuple数据
def match(word_list, expecting):
    if word_list:
        # pop之后word_list列表中的数据减少
        word = word_list.pop(0)
        print "type(word):", type(word)
        print "match word:", word
        print "match after pop:", word_list

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
# 过滤word_type类型
def skip(word_list, word_type):
    # 如果word_list中第一个元素word_list[0]的类型和指定的类型一致，则调用match函数
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    print "parse_verb_word_list", word_list
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    print "parse_object_word_list", word_list
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    print "parse_subject_word_list", word_list
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    print "subj:", subj
    print "verb:", verb
    print "obj:", obj

    return Sentence(subj, verb, obj)

# 测试程序的调用是否正确
# a = parse_sentence([('verb','eat'),('stop','the'),('noun','bear')])
# print "a.subject:", a.subject
# print "a.verb:", a.verb
# print "a.object:", a.object
