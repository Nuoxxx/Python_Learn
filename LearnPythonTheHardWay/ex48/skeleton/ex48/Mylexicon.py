# -*- coding:utf-8 -*-

# 这是自己最初写的文档，思维是对的，但是细节处理有问题
class Tlexicon(object):


    def __init__(self):
        pass
        #numbers = []

    def convert_directions(self, direction):
        return ('direction',direction)

    def convert_verbs(self, verb):
        pass

    def convert_stops(self, stop):
        pass

    def convert_nouns(self, noun):
        pass

    def convert_numbers(self, number):
        try:
            return int(number)
        except:
            return None

    def convert_errors():
        pass


    def scan(self, string):
        self.string = string
        words = self.string.split()
        print "Split words:",words

        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs =['go', 'stop', 'kill', 'eat']
        stops = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet']

        for word in words:
            if word in directions:
                print "direciton bigin"
                first_word = self.convert_directions(word)
            elif word in verbs:
                convert_verbs()
            elif word in stops():
                convert_verbs()
            elif word in nouns():
                convert_nouns()
            else:
                print "Error"
            sentence = [first_word]
            print "sentence:", sentence

# l = lexicon()
# l.scan('north')
