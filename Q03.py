nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print(f'{nome}, você está apto(a) a votar.')

else:
    print(f'{nome}, você não está apto(a) a votar.')