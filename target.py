# ATIVIDADE 1

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)
# 91 é o resultado da variável SOMA


# ATIVIDADE 2

import math

def Raiz(n):
    s = int(math.sqrt(n))
    return s*s == n

def Fibonacci(n):
    return Raiz(5*n*n + 4) or Raiz(5*n*n - 4)

num = int(input("Digite um número: "))

if Fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
# ATENÇÃO! eu já tinha esse script feito no meu github, portanto, apenas tirei a interface tkinter e coloquei para mostrar no console.


# ATIVIDADE 3
    
# a) 1, 3, 5, 7, ___
# O próximo elemento é 9, pois 7 + 2 = 9.


# b) 2, 4, 8, 16, 32, 64, ____
# O próximo elemento é 128, pois 64 * 2 = 128.

# c) 0, 1, 4, 9, 16, 25, 36, ____
# O próximo elemento é 49, pois 7 2 = 49.

# d) 4, 16, 36, 64, ____
# O próximo elemento é 100, pois (2*5) 2 = 100.

# e) 1, 1, 2, 3, 5, 8, ____
# O próximo elemento é 13, pois 5 + 8 = 13.

# f) 2,10, 12, 16, 17, 18, 19, ____
# O próximo elemento é 20, pois 19 + 1 = 20 e 20 é divisível por 4.
    

# ATIVIDADE 4

# Primeiro, eu ligaria o interruptor 1 e deixaria ele ligado por alguns minutos. 
# Depois, eu desligaria ele e ligaria o interruptor 2. Em seguida, eu iria até a sala das lâmpadas.
# Na sala das lâmpadas, eu veria qual lâmpada está acesa. Essa lâmpada seria controlada pelo interruptor 2. 
# Eu também tocaria nas outras duas lâmpadas para ver qual delas está quente. Essa lâmpada seria controlada pelo interruptor 1. 
# A lâmpada que está fria e apagada seria controlada pelo interruptor 3.
# Depois, eu voltaria para a sala dos interruptores e confirmaria minha resposta ligando e 
# desligando cada um deles e observando as lâmpadas correspondentes.
    
#ATIVIDADE 5
    
s = "Olá, mundo!"

inverso = "" 
for i in range(len(s)):
    inverso = s[i] + inverso 

print(inverso)
