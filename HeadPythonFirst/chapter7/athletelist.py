class AthleteList(list):
    def __init__(self,a_name,a_dob,a_times=[]):
        ##
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([scrinize(t) for t in self]))[0:3])

def scrinize(time_string):
    splitter=''
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

# sarah =get_data('sarah2.txt')
# sarah.append('1.31')
# print(sarah.name+str(sarah.top3()))
