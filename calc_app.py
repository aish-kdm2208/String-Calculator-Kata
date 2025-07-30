def add(string):
    if string=="":
        return 0
   
    num=string.split(',')
    return sum(int(i) for i in num)
