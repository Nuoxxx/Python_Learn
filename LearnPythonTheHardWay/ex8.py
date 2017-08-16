# -*- coding: utf-8 -*-
#r%使用
formatter = "%r %r %r %r"
#r int值
print formatter %(1, 2, 3, 4)
#r String
print formatter %("one", "two", "three", "four")
#r Boolean
print formatter %(True, False, False, True)
#r formatter
print formatter %(formatter, formatter, formatter, formatter)
#r Sentence
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
