data = open('sketch2.txt','w+')
print(data.read())
print('123++',file=data)
data.close()
