import os


def menu():
    variables = input("""
Bienvenido a Statistics in Python (beta)
Inserte los datos a continuación:

--> """)
    
    data = []
    temp = []

    variables = variables.replace(',' , '') + ' '
    for i in variables:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            temp.append(i)
        elif i == ' ':
            data.append(''.join(temp))
            temp = []
            continue
    data.sort()  
    
    os.system('cls')
    print('Data in order: [' + '  '.join(data) + ']')
    xi = set(data)
    xi = list(xi)
    xi.sort()
    
    fi = absolute_freq(data)
    fr = relative_freq(fi, data)

    print('\nXi | fi |  fr   |')
    print('---|----|-------|')
    for i in xi:
        print( str(i), '|', fi.get(str(i)), ' |' , fr.get(i), '|')
    print('---|----|-------|')
    total_fr = int(sum(fr.values()) * (10**3))/(10**3)
    print(f'   | {sum(fi.values())} | {float(total_fr)} |')


def absolute_freq(data):
    fi = {'':''}
    for i in data:
        if i not in fi:
            fi.setdefault(i,1)
        elif i in fi:
            temp = int(fi.get(i)) + 1
            temp = {i : temp}
            fi.update(temp)
    fi.pop('')
    return fi


def relative_freq(fi, data):
    fr= {'':''}
    for key, value in fi.items():
        division = int(value) / len(data)
        division = int(division * (10**3))/(10**3)
       # fr.append(str(division))
        fr.setdefault(key, float(division))
    fr.pop('')
    return fr


#print(xf)

if __name__ == '__main__':
    menu()