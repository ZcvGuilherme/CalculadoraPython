def soma(v1,v2):
   return v1 + v2

def sub(v1,v2):
   return v1 - v2

def mult(v1,v2):
   return v1 * v2

def divi(v1,v2):
   return v1 / v2

def poten(v1,v2):
   return v1 ** v2

import time


while True:
   print('escolha uma opção: \n 1 - soma \n 2 - subração \n 3 - multiplicação \n 4 - divisão \n 5 - potência')
   op = int(input('digite a opção: '))
   if op == 1:
     v1 = int(input('valor 1: '))
     v2 = int(input('valor 2: '))
     print('resposta: ', v1, '+', v2, '=',  soma(v1, v2))
     
     print('escolha a próxima operação: ')
     time.sleep(2)
     
   elif op == 2:
     v1 = int(input('valor 1: '))
     v2 = int(input('valor 2: '))
     print('resposta: ', v1, '-', v2, '=',  sub(v1, v2))

     print('escolha a próxima operação: ')
     time.sleep(2)

   elif op == 3:
     v1 = int(input('valor : '))
     v2 = int(input('multiplicado por: '))
     print('resposta: ', v1, '*', v2, '=',  mult(v1, v2))

     print('escolha a próxima operação: ')
     time.sleep(2)

   elif op == 4:
     v1 = int(input('número: '))
     v2 = int(input('dividido por: '))
     print('resposta: ', v1, '/', v2, '=',  divi(v1, v2))

     print('escolha a próxima operação: ')
     time.sleep(2)

   elif op == 5:
     v1 = int(input('número: '))
     v2 = int(input('elevado a: '))
     print('resposta: ', v1, '^', v2, '=',  poten(v1, v2))

     print('escolha a próxima operação: ')
     time.sleep(2)

   else:
      print('nenhuma opção válida')
      break
