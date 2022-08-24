from ntpath import join
import os


def menu():
    option = input("""
Bienvenido a Statistics in Python (beta)

Como desea ingresar los datos?
[1] Separado por comas
[2] Separado por espacios

> """)
    os.system('cls')

    variables = input("""
Inserte los datos a continuación:

--> """)
    
    data = []
    temp = []

    if option == '1':
        for i in variables:
            if i == ',':
                data.append(''.join(temp))
                temp = []
                continue
            if i != ' ':
                temp.append(i)
            
    elif option == '2':
        for i in variables:
            if i.isnumeric() == False:
                data.append(''.join(temp))
                temp = []
                continue
            temp.append(i)
            
    
    


    print(data)

if __name__ == '__main__':
    menu()