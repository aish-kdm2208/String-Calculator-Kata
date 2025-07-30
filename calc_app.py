def add(string):
    if string=="":
        return 0
    
    elif string.startswith('//'):
        delimiter = ';'
        simple_string = string.replace('\n', delimiter)
        list = simple_string.split(delimiter)
        num=list[2:]

    else:
        string = string.replace("\n", ",")
        num=string.split(',')

    return sum(int(i) for i in num)

