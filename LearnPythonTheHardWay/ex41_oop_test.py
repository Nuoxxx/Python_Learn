# -*- coding:utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
# 字典
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)***@@@":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# strip()方法用于移除字符串头尾指定的字符（默认为空格）
# 将链接中的文字添加到WORDS中
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
#print "WORDS :" ,WORDS


#
def convert(snippet, phrase):
    #  capitalize()将字符串的第一个字母变成大写,其他字母变小写。
    #  对于 8 位字节编码需要根据本地环境。

###从WORDS中选取%%%，***，@@@对应数量的单词用来替换
    # random.sample(seq, n) 从序列seq中选择n个随机且独立的元素
    class_names_percent= [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    print "class_names_percent:", class_names_percent
    other_names_star = random.sample(WORDS, snippet.count("***"))
    print "other_names_star:", other_names_star
    results = []
    param_names_a = []

    #
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        print "param_count:", param_count
        #将多个单词组成用，隔开组成一个字符串
        param_names_a.append(', '.join(random.sample(WORDS, param_count)))
        print "param_names_a:", param_names_a

#分别将snippet、phrase中包含的 %%%，***，@@@替换成其他内容
        # 依次将 snippet,phrase的值赋给sentence
    for sentence in snippet, phrase:
        #print "sentence:", sentence
        # ??????
        result = sentence[:]
        #print "result:", result

        # fake class names
        for word in class_names_percent:
            #str.replace(old, new[, max])返回字符串中的 old（旧字符串）
            #替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过max次
            result = result.replace("%%%", word, 1)
            print "result2:", result

        # fake other names
        for word in other_names_star:
            result = result.replace("***", word, 1)
            print "result3:", result

        # fake parameter lists
        for word in param_names_a:
            result = result.replace("@@@", word, 1)
            print "result4:", result

        results.append(result)
        print "result aaaa:", result

    return results


# keep going until they hit CTRL-D
try:
    while True:
# dict.keys() 字典(Dictionary) keys() 函数以列表返回一个字典所有的键。
        snippets = PHRASES.keys()
# random.shuffle()将一个序列中的元素随机打乱
        random.shuffle(snippets)

        for snippet in snippets:
# 通过key获取value
            phrase = PHRASES[snippet]
            print "snippet&phrase:", snippet, "&", phrase
            question, answer = convert(snippet, phrase)
            print "question:", question
            print "answer:", answer
# 如果PHRASE_FIRST 为真，则question和answer互换
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"
