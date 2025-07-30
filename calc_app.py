def add(string):
    if string=="":
        return 0
    
    elif string.startswith('//'):
        delimiter_part, string = string.split('\n',1)
        delimit = delimiter_part[2:]
        simple_string = string.replace('\n', delimit)
        num = simple_string.split(delimit)

    else:
        string = string.replace("\n", ",")
        num=string.split(',')

    return sum(int(i) for i in num)

