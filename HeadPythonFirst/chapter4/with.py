import sys
import nesteramy
import pickle
man = []
other = []
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role =='Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
    # with open("man.txt","w") as man_file:
    #     nesteramy.print_lol(man,fn=man_file)
    # with open("other.txt","w") as other_file:
    #     nesteramy.print_lol(other, False,0,other_file)
    with open('man.txt','wb') as man_file,open('other.txt','wb') as other_file:
        #将list中的数据腌制放入文本中
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+str(perr))
