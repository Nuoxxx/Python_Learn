class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        # return(sorted(set([scrinitize(t) for t in self.times]))[0:3])
        return(sorted(set([scrinitize(t) for t in self.times]))[0:3])

# def get_data(file):
#     with open('hfpy_ch6_data/'+file) as myfile:
#         datas = myfile.readline().strip().split(',')
#         return(Athlete(datas.pop(0),datas.pop(0),datas))

def get_data(file):
    try:
        with open('hfpy_ch6_data/'+file) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return(Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

def scrinitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
        (min,sec)=time_string.split(splitter)
        return(min+'.'+sec)

sarah = get_data('sarah2.txt')
print(sarah.name+"'s fastest times are:'"+sarah.top3())
