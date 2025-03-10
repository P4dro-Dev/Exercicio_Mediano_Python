numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
somatorio = sum(numeros)
primeiro_impar = numeros[0] % 2 != 0
ultimo_par = numeros[-1] % 2 == 0
media = somatorio / 10

if somatorio % 2 == 0 and primeiro_impar and ultimo_par and media > 5:
    print("Acesso permitido!")
else:
    print("Acesso negado! Tente novamente.")