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

    negative_values = [n for n in num if int(n) < 0]
    if negative_values:
        raise Exception(f"Numbers cannot be negative {','.join(negative_values)}")
 

    return sum(int(i) for i in num)

