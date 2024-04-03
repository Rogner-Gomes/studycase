def solve_me_first(a, b, c):
    if c == '+':
        res = a + b
    elif c == '-':
        res = a - b
    elif c == '*':
        res = a * b
    elif c == '/':
        res = a / b
    else:
        res = 'VTNC então vaginildo!'
    return res
    # Hint: Type return a+b below


num1 = int(input('digite o primeiro numero: \n'))
num2 = int(input('digite o segundo numero: \n'))
operador = input('digite a operacao que deseja realizar sendo +(soma), \
-(subtracao), *(mutiplica) e /(divisão): \n')
res = solve_me_first(num1, num2, operador)
print(res)
contop = input('continuar operação com o resiltado? y para sim e n para não. \n')
while contop == 'y':
    num1 = res
    operador = input('digite a operacao que deseja realizar sendo +(soma), \
-(subtracao), *(mutiplica) e /(divisão): \n')
    num2 = int(input('digite o segundo numero: \n'))
    res = solve_me_first(num1, num2, operador)
    print (res)
    contop = input('continuar operação com o resiltado? y para sim e n para não. \n')
#def funcao_teste():
#class ClasseTeste():
#'ele disse:"vai tomar no cu!".'