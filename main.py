import random
aposta = []
estrelas_aposta = []
chave = []
chave_estrelas = []
num_acertos = 0
estrelas_acertos = 0
resultado_num = []
resultado_estrela = []


#Aletórios os numeros:
for x in range(0, 5):
    num_sorteado = random.randint(1, 50)
    while num_sorteado in chave:
        num_sorteado = random.randint(1, 50)
    chave.append(num_sorteado)
chave.sort()


#Aletórios estrelas:
for x in range(0, 2):
    estrela = random.randint(1, 12)
    while estrela in chave_estrelas:
        estrela = random.randint(1, 12)
    chave_estrelas.append(estrela)
chave_estrelas.sort()


#Aposta números
for n in range(0, 5):
    num_aposta = int(input(f'Insira o {n + 1} numero entre 1 e 50:  '))
    while num_aposta > 50 or num_aposta < 1 or num_aposta in aposta:
        num_aposta = int(input(f'Insira o {n + 1} numero entre 1 e 50:  '))
    aposta.append(num_aposta)
    aposta.sort()
print(f'Os número selecionador por você, em ordem, foram: {aposta}\n')

#Aposta estrelas
for n in range(0, 2):
    estrela_apos= int(input(f'Insira a {n+1} estrela entre 1 e 12:  '))
    while estrela_apos > 12 or estrela_apos < 1 or estrela_apos in estrelas_aposta:
        estrela_apos = int(input(f'Insira a {n+1} estrela entre 1 e 12:  '))
    estrelas_aposta.append(estrela_apos)
estrelas_aposta.sort()
print(f'As estrelas selecionadar por você, em ordem, foram: {estrelas_aposta}\n')

#comparar os números:
for a in aposta:
    for b in chave:
        if a == b:
            resultado_num.append(a)
            num_acertos += 1

#comparar as estrelas:
for c in chave_estrelas:
    for d in estrelas_aposta:
        if c == d:
            resultado_estrela.append(c)
            estrelas_acertos += 1

#impressões:
print ('-=' * 40)

print(f'Os selecionados pelo utilizador foram: {aposta}')
print(f'Os selecionados pelo utilizador foram: {estrelas_aposta}')
print(f'Os valores aletórios gerados foram: {chave}')
print(f'As estrelas aletórias geradas foram: {chave_estrelas}')
print ('-=' * 40)

if num_acertos == 0 and estrelas_acertos == 0:
    print('Sinto mto você não acertou nenhum número e nenhuma estrela')
    print('-=' * 40)
else:
    print(f'Parabéns! Acertou: {num_acertos}  números e {estrelas_acertos} estrelas !')
    print(f'Os número acertados foram {resultado_num} e as estrelas acertadas foram {resultado_estrela}') # coloquei só de curiosidade!
    print('-=' * 40)
#random.randint(1, 50)