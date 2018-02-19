
'''
Quantos zeros consecutivos a esquerda n! possui

Teoreama:

Se n! puder ser descrito como 2^a * 5^b * k onde k eh diferente de 2 e 5, entao o numero de zeros sera min(a, b)

https://brilliant.org/wiki/trailing-number-of-zeros/

'''

'''
Usando o teorema acima podemos fatorar um numero n!, (n-1)!, (n-2)! ate 1 verificando
quanto n-x! for divisivel por 2 e/ou 5 e contarmos quantas vezes 2 e 5 aparecem.
 
'''


def count(value, divisor):
    acc = 0
    while value % divisor == 0:
        value //= divisor
        acc += 1
    return acc


# nao parece muito eficiente para fatoriais
def countFactor2And5(value):
    acc2, acc5 = (0, 0)
    for i in range(value, 0, -1):
        if i % 2 == 0:
            acc2 += count(i, 2)
        if i % 5 == 0:
            acc5 += count(i, 5)
    return acc2 if acc2 < acc5 else acc5

'''
print(countFactor2And5(10))
print(countFactor2And5(5))
print(countFactor2And5(11))
print(countFactor2And5(24))
print(countFactor2And5(120))
print(countFactor2And5(4000))
'''


def countFactor2And5V2(value):
    acc2, acc5 = (0, 0)
    for i in range(value, 0, -1):
        if i % 2 == 0:
            acc2 += count(i, 2)
        if i % 5 == 0:
            acc5 += count(i, 5)
    return acc2, acc5

'''
print((countFactor2And5V2(5)))
print((countFactor2And5V2(50000)))
'''

'''
Um observacao interenssante eh que conforme contamos quantas vezes podemos dividir  n!, (n-1)!
(n-2)! por 2 e por 5, verificamos que o numero 2 aparece sempre mais vezes do que 5, logo
para o problema de contagem de zeros a esquerda de um numero n! podemos contar somente, quantos multiplos
de cinco aparecem. 

Se n! pode se expresso na forma 5^a 8 k onde k e != 5, a eh numero de zeros a esquerda

Cada muliutplo de 5 encontrado em n! contribui com 1 zero a esquerda,e a cada multiplo de 25
com 2
'''


def log(logt, base):
    from math import log10
    return log10(logt) / log10(base)


def countTrailingZerosNFactorial(n):
    acc = 0
    divisor = 5
    while divisor <= n:
        acc += n // divisor
        divisor *= 5
    return acc


def countTrailingZerosNFactorialV2(n):
    from math import floor
    k = int(floor(log(n, 5)))
    acc = 0
    divisor = 5
    for i in range(0, k):
        acc += int(floor(n/divisor))
        divisor *= 5
    return acc


def test(value):
    print('%d: %d, %s, %d'
          % (value
             , countTrailingZerosNFactorial(value)
             , countFactor2And5V2(value)
             , countTrailingZerosNFactorialV2(value)
             ))


test(500)
test(30)
test(4000)
test(1000)






if __name__ == '__main__':
    pass