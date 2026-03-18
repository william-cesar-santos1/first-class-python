'''
1. Imprima os números de 1 a [Informado pelo usuário]
2. Para múltiplos de 3, imprima "fizz" ao invés do número
3. Para múltiplos de 5, imprima "buzz" ao invés do número
4. Para múltiplos de 3 e 5, imprima "fizzbuzz" ao invés do número
5. Para os demais números, imprima o número normalmente

Exemplo:
Entrada: 15
Saída:
1
2
fizz
4
buzz
fizz
7
8
buzz
fizz
11
13
14
fizzbuzz
'''
limite = int(input("Digite um número: "))
contador = 1
while contador <= limite:
    if contador % 3 == 0 and contador % 5 == 0:
        print("fizzbuzz")
    elif contador % 3 == 0:
        print("fizz")
    elif contador % 5 == 0:
        print("buzz")
    else:
        print(contador)
    contador += 1