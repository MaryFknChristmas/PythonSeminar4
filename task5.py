file1 = '5x^5 + 3 x ^ 2 + 3 * x - 22 * x^7 - 77'
file2 = '3x^2 - 2x + 5'
 
 
def get_ones(line):
    tmp = []
    last = 0
    positive = True
    for i, item in enumerate(line):
        if item in {'+', '-'}:
            if positive:
                tmp.append(line[last:i])
            else:
                tmp.append('-' + line[last:i])
            last = i + 1
            positive = item == '+'
 
    if positive:
        tmp.append(line[last:])
    else:
        tmp.append('-' + line[last:])
    return tmp
 
 
def get_coef(one):
    for i, item in enumerate(one):
        if item == 'x':
            return int(one[:i]), one[i:]
    return int(one), None
 
 
lst1 = get_ones(file1.replace(' ', '').replace('*', ''))
lst2 = get_ones(file2.replace(' ', '').replace('*', ''))
 
dct1 = {item[1]: item[0] for item in map(get_coef, lst1)}
dct2 = {item[1]: item[0] for item in map(get_coef, lst2)}
 
 
print(dct1)
print(dct2)