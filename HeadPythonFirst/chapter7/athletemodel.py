## -*- coding:utf-8 -*-
import pickle
from athletelist import AthleteList

def get_data(file):
    try:
        with open('txt/'+file) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error:'+str(ioerr))

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ##将各个文件转换为一个Athletelist对象实例，并将选手的数据增加到字典
        ath = get_data(each_file)
        ##每个选手的名字作为字典的“键”，“值”是Athletelist对象实例
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File errror(put_to_store):'+str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):'+str(ioerr))
    return(all_athletes)

def get_names_from_store():
    athletes = get_from_store()
    response = [athletes[each_ath].name for each_ath in athletes]
    return(response)

the_files =['sarah2.txt','james2.txt']
data = put_to_store(the_files)
print(data)
