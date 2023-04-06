#ABRIR O CAIXA
senha = 0
tentativas = 3

while senha != 2987:
    senha = int(input('Digite a senha:\n'))
    if senha != 2987:

        tentativas = tentativas - 1
        print(f'Senha incorreta, você possui {tentativas} tentativas restantes.')

        if tentativas == 0:
            print('Sistema tem que ser reiniciado!')
            exit() #Comando fechar o programa

    else:
        print('Senha Correta, caixa aberto!\n')


print('Bem Vindo ao Supermercado!\n')

#LEITURA DAS VENDAS
valorTotal = 0
valorInserido = 0
valorComputado = 0
item = 1
finalizar = 'N'

print("INSERÇÃO DOS ITENS VENDIDOS:")

while finalizar == 'N':

    valorInserido = float(input(f'Digite o valor do item {item}: R$'))


    #Opção 0: Continuar ou Finalizar a inserção de valores
    if valorInserido == 0:
       finalizar = str(input("Deseja realmente finalizar? (S = Sim | N = Não): ").upper())

       if finalizar == 'N':
            valorInserido = float(input(f'Digite o valor do item {item}: R$'))
            valorComputado = valorInserido
       elif finalizar == 'S':
            item -= 1
            break
       else:
         while finalizar != 'S' and finalizar != 'N':
                finalizar = str(input('Resposta inválida, responda S para Sim ou N para Não: '))
         if finalizar == 'N':
            valorInserido = float(input(f'Digite o valor do item {item}: R$'))
            valorComputado = valorInserido

    #Opção -1: Corrigir o valor inserido
    elif valorInserido == -1:
        item -= 1
        valorTotal -= valorComputado

        valorInserido = float(input(f'Digite o valor correto do item {item}: R$'))
        valorComputado = valorInserido
        valorTotal += valorComputado
        item += 1

    else:
        item += 1
        valorComputado = valorInserido
        valorTotal += valorComputado

print('\nVenda finalizada!')
print(f'Total R${valorTotal} ||||||||||||||||| {item} itens.')


#FINALIZAÇÃO E CALCULO DO TROCO
cedula200Valor = 200
cedula200Qnt = 2
cedula200Total = cedula200Qnt*cedula200Valor
cedula200Troco = 0

cedula100Valor = 100
cedula100Qnt = 4
cedula100Troco = 0

cedula50Valor = 50
cedula50Qnt = 6
cedula50Troco = 0

cedula10Valor = 10
cedula10Qnt = 10
cedula10Troco = 0

cedula5Valor = 5
cedula5Qnt = 10
cedula5Troco = 0

moeda1Valor = 1
moeda1Qnt = 20
moeda1Troco = 0

moeda50Valor = 0.5
moeda50Qnt = 20
moeda50Troco = 0

somaCaixa = (cedula200Qnt*cedula200Valor)+(cedula100Qnt*cedula100Valor)+(cedula50Qnt*cedula50Valor)+(cedula10Qnt*cedula10Valor)+(cedula5Qnt*cedula5Valor)+(moeda1Qnt*moeda1Valor)+(moeda50Qnt*moeda50Valor)

caixa = 1280.00
valorPago = float(input('Valor pago: R$'))
troco = 0
trocoCedula = 0

if valorPago == valorTotal:
    print('NÃO HÁ TROCO.')

elif valorPago > valorTotal:
    troco = valorPago - valorTotal
    print(f'Troco: R${troco}')

    while (troco//cedula200Valor) >= 1 and cedula200Qnt>0:

        cedula200Qnt -= 1
        troco -= cedula200Valor
        cedula200Troco += 1

    '''
    while (troco//cedula100Valor) >= 1 and cedula100Qnt>0:

        cedula100Qnt -= 1
        troco -= cedula100Valor
        cedula100Troco += 1
    '''
    if (troco//cedula100Valor) >= 1:
        if cedula100Qnt > 0:
            while cedula100Qnt > 0:
                cedula100Qnt -= 1
                troco -= cedula100Valor
                cedula100Troco += 1


    while (troco//cedula50Valor) >= 1 and cedula50Qnt>0:

        cedula50Qnt -= 1
        troco -= cedula50Valor
        cedula50Troco += 1

    while (troco//cedula10Valor) >= 1 and cedula10Qnt>0:

        cedula10Qnt -= 1
        troco -= cedula10Valor
        cedula10Troco += 1

    while (troco//cedula5Valor) >= 1 and cedula5Qnt>0:

        cedula5Qnt -= 1
        troco -= cedula5Valor
        cedula5Troco += 1

    while (troco//moeda1Valor) >= 1 and moeda1Qnt>0:

        moeda1Qnt -= 1
        troco -= moeda1Valor
        moeda1Troco += 1

    while (troco//moeda50Valor) >= 1 and moeda50Qnt>0:

        moeda50Qnt -= 1
        troco -= moeda50Valor
        moeda50Troco += 1

    print(f' {cedula200Troco} cedulas de R$200')
    print(f' {cedula100Troco} cedulas de R$100')
    print(f' {cedula50Troco} cedulas de R$50')
    print(f' {cedula10Troco} cedulas de R$10')
    print(f' {cedula5Troco} cedulas de R$5')
    print(f' {moeda1Troco} moedas de R$1')
    print(f' {moeda50Troco} moedas de R$0,50')

else:
    print('Valor pago insuficiente!')
    valorPago = float(input('Insira novamente valor pago: R$'))



