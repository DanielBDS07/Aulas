

acessar = (input('quer entrar na calculadora [s/n]: '))
while acessar == 's':
    quantidade = (input('com quantos algaritimos você quer a sua conta ? :'))


    if quantidade == "2":
        n1 = float(input("Primeiro digito: ")) 
        O1 = input("Operadores Aritméticos (+,-,*,/): ") 
        n2 = float(input("Segundo digito: ")) 

        match O1:
            case "+":
                print("o resultado é:" , n1 + n2)
            case "-":
                print("o resultado é:" , n1 - n2)
            case"*":
                print("o resultado é:" , n1 * n2)
            case "/":
                if n2 == 0:
                    print("Não se pode dividir por 0")
                else:
                    print("o resultado é:" , n1 / n2)

            case _:
                print("Operador incorreto, por favor, coloque um operador valido")

    elif quantidade == "3":
        n1 = float(input("Primeiro digito: ")) 
        O1 = input("Operadores Aritméticos (+,-,*,/): ") 
        n2 = float(input("Segundo digito: ")) 

        match O1:
            case "+":
                nr1 = n1 + n2
                O2 = input("segunda Operadores Aritméticos (+,-,*,/): ") 
                n3 = float(input("terceiro digito: ")) 
                match O2:
                    case "+":
                        print("o resultado é:" , nr1 + n3) 
                    case "-":
                        print("o resultado é:" , nr1 - n3)
                    case"*":
                        print("o resultado é:" , nr1 * n3)
                    case "/":
                        if n3 == 0:
                            print("Não se pode dividir por 0")
                        else:
                            print("o resultado é:" , nr1 / n3)
            case "-":
                nr1 = n1 - n2
                O2 = input("segunda Operadores Aritméticos (+,-,*,/): ") 
                n3 = float(input("terceiro digito: ")) 
                match O2:
                    case "+":
                        print("o resultado é:" , nr1 + n3) 
                    case "-":
                        print("o resultado é:" , nr1 - n3)
                    case"*":
                        print("o resultado é:" , nr1 * n3)
                    case "/":
                        if n3 == 0:
                            print("Não se pode dividir por 0")
                        else:
                            print("o resultado é:" , nr1 / n3)
            case "*":
                nr1 = n1 + n2
                O2 = input("segunda Operadores Aritméticos (+,-,*,/): ") 
                n3 = float(input("terceiro digito: ")) 
                match O2:
                    case "+":
                        print("o resultado é:" , nr1 + n3) 
                    case "-":
                        print("o resultado é:" , nr1 - n3)
                    case"*":
                        print("o resultado é:" , nr1 * n3)
                    case "/":
                        if n3 == 0:
                            print("Não se pode dividir por 0")
                        else:
                            print("o resultado é:" , nr1 / n3)
            case "/":
                if n2 == 0:
                    print("Não se pode dividir por 0")
                else:
                    nr1 = n1 + n2
                O2 = input("segunda Operadores Aritméticos (+,-,*,/): ") 
                n3 = float(input("terceiro digito: ")) 
                match O2:
                    case "+":
                        print("o resultado é:" , nr1 + n3) 
                    case "-":
                        print("o resultado é:" , nr1 - n3)
                    case"*":
                        print("o resultado é:" , nr1 * n3)
                    case "/":
                        if n3 == 0:
                            print("Não se pode dividir por 0")
                        else:
                            print("o resultado é:" , nr1 / n3)
            case _:
                print("Operador incorreto, por favor, coloque um operador valido")

    acessar = (input('quer continuar [s/n]: '))
else: 
    print('muito obrigado por acessar')