nome = input("Digite o seu nome: ")
disciplina = input("Digite a disciplina: ")
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print('Nota inválida, tente novamente.')

else:
    if nota >= 5.5 and nota <= 6:
        nota = 6

    if nota >= 6 and nota <= 10:
        status = "aprovado(a)"
        print(f'{nome} está {status} em {disciplina} com nota {nota}.')

    if nota < 6:
        status = "reprovado(a)"
        print(f'{nome} está {status} em {disciplina} com nota {nota}.')