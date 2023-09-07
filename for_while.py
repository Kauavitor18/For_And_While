'''Estudos de estruturas de repetição. For e While'''

#for

nomes = ['Kauã', 'Douglas', 'Pedro', 'João']
for n in nomes:
    print(n)

else: 
    print("\nSeus amigos estão sendo printados no laço for\n")


#While 

usuario = str(input("Digite seu nome de Usuário: "))
senha = int(input("Digite sua senha: "))

while senha != 12345:
    print("Sua senha está incorreta :( Tente novamente !")
    senha = int(input("Digite sua senha: "))

else:
    print(f"Sua senha correta :) Seja bem vindo, {usuario}")