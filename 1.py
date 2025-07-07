sd = float(input('qual o valor a definir como salario maximo para reajuste de + 15%?'))
salario = float(input('qual o seu sario?'))
if salario > sd:
    bonus  = (salario * 10)/100
    reajust1 = (salario + bonus )
    print('seu reajuste e de {}'.format(reajust1))
elif salario <= sd:
    bonus2 = (salario * 15)/100
    reajust1 = (salario + bonus2)
print('seu reajuste e de {}'.format(reajust1))





