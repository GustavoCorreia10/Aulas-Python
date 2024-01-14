SNAKE CASE
PALAVRAS COMPOSTAS
DECLARAÇÕES SEMÂNTICAS

nome_do_usuario = input("Digite seu nome: ")
print(nome_do_usuario)

condatenar - juntar uma variável com um número
numero1 = 'g'
numero2 = 20
print(numero1,numero2)

pedir para o usuário digitar o nome a idade e a cidade e depois concatenar tudo

name = input ('Digite seu nome: ')
age = input ('Digite sua idade: ')
city = input ('Digite sua cidade: ')

print('O nome do usário é', name, 'sua idade é,', age, 'Ele mora na cidade:', city)

Crie um sistema que peça ao usuário o estado civil
Em seguida concatene com a seguinte frase - 'O usuário é'

estado_civil = input('Digite seu Estado Civil: ')
print('O usuário é',estado_civil,)

DADOS PRIMITIVOS

dinheiro_real = 1.25
boleano = True or False #BOLEANOS
char = 'Text' #STRINGS OU CARACTERES
inteiro = 2  #INTEIRO
print(dinheiro_real, boleano, char, inteiro)


constantes
EM PYTHON SÃO CONVENÇÕES

variáveis são sempre em letra minúscula

1  -  CRIE UM SISTEMA QUE SOME 2 NUMEROS

numero1 = int (input ('Digite o primeiro número: '))
numero2 = int (input ('Digite o segundo número: '))

print(numero1+numero2)

2 - CRIE UM SISTEMA QUE IMPRIMA SEU NOME NA TELA

nome = input ('Digite o nome mais lindo do mundo: ')
print(nome)

3 - CRIE UM SISTEMA QUE IMPRIMA SEU NOME E UM CUMPRIMENTO APÓS nome(CONCATENE)

name = input ('Digite seu nome: ')
cumprimento = 'Boa Tarde!'
print ( name+',' , cumprimento)

4 - CRIE UM SISTEMA QUE MULTIPLIQUE 2 NÚMEROS

numero1 = int (input('Digite um número: '))
numero2 = int (input('Digite um número: '))
print (numero1*numero2)

= ATRIBUIÇÃO
== IGUALDADE
* MULTIPLICAÇÃO
+ SOMA
- SUBTRAÇÃO

> MAIOR
< MENOR
<= MENOR OU IGUAL
>= MAIOR OU IGUAL
!= DIFERENTE DE

CONDICIONAIS (SE) E SINAIS DE COMPARAÇÃO

declare uma variável de número inteiro e verifique se ele é positivo

senha_correta = '123456'
senha_digitada = input("Digite uma senha")

if senha_digitada == senha_correta:
   print("Acesso autorizado")

else:
  print ('Acesso negado')

idade = int(input('Digite sua idade ->'))
print ("Acesso ao show")

if idade <= 17:
  print('Acesso Negado')
else:
  print('Acesso Autorizado')


rua = "rua 10"

if rua != 'rua 10':
    print('A festa não é na', rua)
else:
    print('A festa é na', rua)


print ('Vacinas para pessoas com 18 anos')
idade = 17

if idade != 18:
  print('Não precisa tomar a vacina')
else:
  print('Precisa se vacinar')



n1 = int(input('digite um número->'))
n2 = int(input('digite um número->'))

if n1 > n2:
  print ('O primeiro é maior')
else:
  print ('O segundo é maior')

if = SE
else = SE NÃO

1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?

idade1 = int(input('Digite a primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))

if idade1 > idade2:
  print ('A primeira idade é maior')
else:
  print ('A segunda idade é maior')

2 - Crie um sistema para permitir a verificação de menores em um show

idade = int(input('Digite sua idade: '))
print ("Acesso ao Estádio")

if idade >= 18:
   print('Acesso autorizado, você tem', idade, 'anos') #Concatenação
else:
   print('Acesso não autorizado, você tem', idade, 'anos')  #Concatenação

3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if()
para verificar se o aluno passou.


nota1 = float(input("Digite a nota 1 -  "))
nota2 = float(input("Digite a nota 2 - "))
nota3 = float(input("Digite a nota 3 - "))

media = (nota1  + nota2 + nota3)/3

if media >= 7:
    print("Aprovado")
    print(media)
elif media ==  6:
    print("Recuperação")
    print(media)
else:
    print("Repetiu")
    print(media)


numero = 2*2
print (numero)


nome = 'Gustavo'
sobrenome = 'Correia'

print(nome, sobrenome)


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

print(n1 + n2)


palavra = 'Python'
print(palavra, 20)

and not or

city = input('Digite sua cidade: ')

if city == 'Guarulhos' or city == 'São Paulo' or city == 'RJ' :
   print('Vou Viajar!')
else:
   print('Vou Trabalhar :( ')


var1 = 123
var2 = 'World'
print('Hello to the',var2,var1)

var1 = 123
var2 = 'World'
print('Hello to the {}{}'.format(var2,var1))

var1= 123
var2= 'World'
print(f'Hello to the (var2) (var1)')

var1 = 123
var2 = 'World'
print('Hello to the {}{}' + var2 + str(var1))

n1 = int(input('Digite um número: '))

if n1 >= 1:
  print ('Esse número é positivo,', n1)

elif n1 == 0:
  print ('Esse número é Zero,', n1)

else:
  print ('Esse número é negativo,', n1)


tri1 = float(input('Digite o Comprimento do primeiro lado: '))
tri2 = float(input('Digite o Comprimento do segundo lado: '))
tri3 = float(input('Digite o Comprimento do terceito lado: '))

if tri1 == tri2 == tri3:
   print ('Esse Triângulo é Equilátero')

elif tri1 ==  tri2 != tri3:
   print ('Esse Triângulo é Isósceles')

else:
   print('Esse Triângulo é Escaleno')


if 2%1==0:
   print('É divisível')
else:
   print('Não é divisível')

ano  =  int(input("Digite o ano"))

if  ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("Não é bissexto")

MÉTODOS EM PYTHON AULA 4
MÉTODOS E FUNÇÕES SÃO SOBRE AÇÕES

text = 'Olá Mundo!'
comprimento = len(text)
print(comprimento)

STRING = TEXTO

number = 51
tipo = type(number)
print(tipo)

n1 = '10'
n2 = 15.5
n3 = 25

v1 = int(n1)
print(type(v1))
v2 = str(n2)
print(type(v2))
v3 = float(n3)
print(type(v3))


palavra = 'BRASIL2023'
print(palavra)
lista = list(palavra)
print(lista)

n = [1,2,3,5,7,9]
print(n)

num = range(1,9)  #lista em colunas
print(num)

for num in range(1,9):
  print(num)

numeros = [1, 2, 4, 4, 8] #código para fazer soma de números inteiros
soma = sum(numeros)  # Isso irá retornar 15
print(soma)


numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximo = max(numeros)  # MAX E MIN = comando para localizar o menor e o maior número da sequencia
minimo = min(numeros)
print(maximo,minimo)

numeros = [1, 1, 4, 1, 8, 9, 2, 10, 5, 3, 5] # SORTED = comando para organizar números e alfabeto em ordem
numeros_ordenados = sorted(numeros)  # Isso irá retornar [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(numeros_ordenados)

Estes são apenas alguns dos métodos e funções básicos em Python.
Python oferece uma ampla gama de funções incorporadas para realizar várias tarefas,
o que torna a linguagem muito versátil e poderosa. À medida que você avança em sua jornada de programação em Python,
você aprenderá mais sobre esses métodos e como usá-los efetivamente em seus programas.

loop for
serve para evitar retrabalhos
evita digitar muitas vezes um algoritmo

print('Olá Mundo')

for n in range(1,10): #comandos para fazer loops
    print('Olá Mundo', n) #variavel N = serve apara numerar as palavras do loop


frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


1-
num = range(2,21,2)
for i in num:
  print(i)

2-
numeros = range(5,51,5)
for i in numeros:
  soma = sum(numeros)
  print(i,soma)

3-
identificador = 'oi'
tipo = type(identificador)
print(tipo)

4-
name = input('Digite seu nome Completo: ')
print('Boa tarde Sr', name)

5-
impar = range(1,11,2)
for i in impar:
  soma = sum(range(1,11,2))
print(soma)

for n in range(1,11,2):
  print(n)
