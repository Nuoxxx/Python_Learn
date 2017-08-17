# -*- coding:utf-8 -*-
"""打印列表，其中有可能包含嵌套列表
"""
import sys
def print_lol(the_list, ident = False,level=0,fn=sys.stdout):
        for each_item in the_list:
                if isinstance(each_item, list):
                        print_lol(each_item,ident, level+1,fn)
                else:
                        if ident:
                                #for num in range(level):
                                        #print("\t", end='')
                                print("\t"*level, end='',file=fn)
                        print(each_item,file= fn)
