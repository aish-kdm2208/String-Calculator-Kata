def add(string):
    if string=="":
        return 0
    
    string = string.replace("\n", ",")
    num=string.split(',')

    return sum(int(i) for i in num)
