# Solicita o número de alunos e, para cada um, verifica o tempo de exercício semanal.
# Exibe uma mensagem com base no tempo: menos de 150min, entre 150 e 300min, ou acima de 300min.

num_alunos = int(input("Número de alunos: "))

for _ in range(num_alunos):
    nome = input("Nome do aluno: ")
    minutos = int(input("Total de minutos na semana: "))
    
    if minutos < 150:
        print(f"{nome}: Você precisa se exercitar mais!")
    elif 150 <= minutos <= 300:
        print(f"{nome}: Ótimo! Você está mantendo uma rotina saudável.")
    else:
        print(f"{nome}: Cuidado! Você pode estar exagerando.")