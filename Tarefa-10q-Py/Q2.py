temperatura = float(input("Temperatura atual: "))
umidade = float(input("Nível de umidade do ar (%): "))

if temperatura > 30 and umidade < 40:
    print("Dia quente e seco! Hidrate-se bem!")
elif 15 <= temperatura <= 30 and umidade > 60:
    print("Provável chuva! Não esqueça o guarda-chuva.")
elif temperatura < 10:
    print("Frio intenso! Use roupas quentes.")
else:
    print("Clima agradável! Aproveite o dia.")