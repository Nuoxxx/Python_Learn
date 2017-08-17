class Athlete(list):
    def __init__(self,a_name,a_dob = None,a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])


def get_data(file):
    try:
        with open('hfpy_ch6_data/'+file) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return(Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)

vera = Athlete('Vera Vi')
vera.append('1.21')
print(vera.top3)
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())
#sarah = get_data('sarah2.txt')
# (sarah_name, sarah_dob)= sarah.pop(0),sarah.pop(0)
# print(sarah_name+"'s fastest times are:'"+
#     str(sorted(set(sanitize(t) for t in sarah))[0:3]))

#print(sarah.name+"'s fastest times are:'"+str(sarah.top3()))
