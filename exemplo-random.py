import random
import os

os.system("cls")

print("Olá, você terá 10 tentativas de acertas os números de 1 a 10 sorteados pelo computador.")

acertos = 0
tentativas = 1
while (tentativas <= 10):
    numeroSorteado = random.randrange(1,11) ##o random sorteia numeros de 1 a 10
    numeroInformado = int(input("Informe um numero de 1 a 10: ")) #o usuário informa um numero entre a 1 a 10
    if (numeroInformado == numeroSorteado):
        acertos = acertos + 1
    tentativas = tentativas + 1
    print("O numero sorteado pelo computador foi: ", numeroSorteado)

if (acertos >= 0) and (acertos <= 3):
    mensagem = 'Você foi mau.'
elif (acertos >= 4) and (acertos <= 6):
    mensagem = 'Você foi bem.'
else:
    mensagem = 'Você foi muito bem.'

print("Voce acertou apenas ",acertos," dos numeros sorteados de a 1 a 10 pelo computador.")
print(mensagem)