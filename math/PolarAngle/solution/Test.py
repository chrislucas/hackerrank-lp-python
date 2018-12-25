'''
https://www.somatematica.com.br/emedio/complexos/complexos8.php

Formula trigonométrica ou polar
Considere o numero complexo a+bi

Modulo z: Distancia entre a origem dum sistema de coordenadas e o Ponto (a, b) dado como |z|

Argumento: Angulo theta formado pelo seguimento de reta (0, 0)(Origem) e Ponto P(a, b)
e a reta das abscissas

'''

from math import acos, asin, sqrt, pi, cos, sin


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


'''
https://pt.khanacademy.org/math/precalculus/trig-equations-and-identities-precalc/inverse-trig-functions-precalc/a/inverse-trigonometric-functions-review
Usamos as funcoes inversas de sin e cos (asin e acos respectivamente)
para descobrirmos que angulo originou tal resultado pela funcao seno e cosseno

Exemplo: 
sabemos que cosseno de 90 graus eh 0, a funcao acos(0) nos retorna pi/2 = 90 graus
sabemos que seno de 90 graus eh 1, a funcao asin(1) nos retorna pi/2 = 90 graus
'''

'''
Exemplos de : https://www.somatematica.com.br/emedio/complexos/complexos8.php
'''


def to_trigonometric_form(p):
    modulo = sqrt(p.x * p.x + p.y * p.y)
    arg_cos = acos(p.x / modulo)
    arg_sin = asin(p.y / modulo)
    print("Modulo %.6f, z = %.6f * (cos %.6f° + i*sin %.6f°)" % (modulo, modulo, arg_cos * 180 / pi, arg_sin * 180 / pi))
    print("Modulo %.6f, z = %.6f * (cos %.6f rad + i*sin %.6f rad)" % (modulo, modulo, arg_cos, arg_sin))


def to_algebraic_form(modulo, arg1, arg2):
    # modulo * (cos(arg1) + sin(arg2))
    print("z = %f * (%f + %f)" % (modulo, cos(arg1), sin(arg2)))
    return


if __name__ == '__main__':
    #to_trigonometric_form(Point(0, 8))
    #to_trigonometric_form(Point(1, 1))
    to_algebraic_form(8, 7*pi/6, 7*pi/6)
