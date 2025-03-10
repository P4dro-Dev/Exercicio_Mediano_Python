# Simula uma corrida de carros, calculando a média de tempo dos competidores.
# Compara a média com o tempo ideal e exibe uma mensagem correspondente.

tempo_ideal = float(input("Tempo médio ideal da prova (segundos): "))
num_competidores = int(input("Quantidade de competidores: "))
total_tempo = 0

for _ in range(num_competidores):
    piloto = input("Nome do piloto: ")
    tempo = float(input("Tempo da corrida (segundos): "))
    total_tempo += tempo

media_tempo = total_tempo / num_competidores
print(f"Média de tempo da corrida: {media_tempo:.2f} segundos")

if media_tempo > tempo_ideal:
    print("Média de tempo da corrida superior ao tempo ideal!")
else:
    print("Tempo ideal alcançado!")