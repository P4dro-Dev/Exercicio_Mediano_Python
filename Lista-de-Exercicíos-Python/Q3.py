# Monitora o estoque de produtos, classificando em Baixo, Médio ou Alto.
# No final, exibe o total de produtos em cada categoria e a média do estoque.

num_produtos = int(input("Número de produtos: "))
baixo = medio = alto = total_quantidade = 0

for _ in range(num_produtos):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade em estoque: "))
    total_quantidade += quantidade
    
    if quantidade < 5:
        print(f"{nome}: Estoque Baixo")
        baixo += 1
    elif 5 <= quantidade <= 15:
        print(f"{nome}: Estoque Médio")
        medio += 1
    else:
        print(f"{nome}: Estoque Alto")
        alto += 1

media = total_quantidade / num_produtos
print(f"Total Baixo: {baixo}, Médio: {medio}, Alto: {alto}")
print(f"Média de estoque: {media:.2f}")