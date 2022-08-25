import os


def menu():
    os.system('cls')
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

    print(f'Original data > {data}')
    xi = set(data)
    xi = list(xi)
    xi.sort()
    
    fi = absolute_freq(data)

    print('Xi | fi |')
    print('---|----|')
    for i in xi:
        print(i, '|', fi.get(str(i)))
    


def absolute_freq(data):
    fi = {'':''}
    for i in data:
        if i not in fi:
            fi.setdefault(i,1)
        elif i in fi:
            temp = int(fi.get(i)) + 1
            temp = {i : temp}
            fi.update(temp)
    return fi

            

    print(xf)

if __name__ == '__main__':
    menu()