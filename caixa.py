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


print('Bem Vindo ao FLEC Supermercado!\n')

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
       finalizar = str(input("Deseja realmente finalizar? (S = Sim | N = Não): "))

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

cedula100Valor = 100
cedula100Qnt = 4

cedula50Valor = 50
cedula50Qnt = 6

cedula10Valor = 10
cedula10Qnt = 10

cedula5Valor = 5
cedula5Qnt = 10

moeda1Valor = 1
moeda1Qnt = 20

moeda50Valor = 0.5
moeda50Qnt = 20

somaCaixa = (cedula200Qnt*cedula200Valor)+(cedula100Qnt*cedula100Valor)+(cedula50Qnt*cedula50Valor)+(cedula10Qnt*cedula10Valor)+(cedula5Qnt*cedula5Valor)+(moeda1Qnt*moeda1Valor)+(moeda50Qnt*moeda50Valor)

caixa = 1280.00
valorPago = float(input('Valor pago: R$'))
troco = 0
trocoCedula = 0

if valorPago == valorTotal:
    print('NÃO HÁ TROCO.')

elif valorPago > valorTotal:
    troco = valorPago - valorTotal

    if troco>cedula200Total:
        
        
    
    print(f'Troco: R${troco}')

else:
    print('Valor pago insuficiente!)
    valorPago = float(input('Insira novamente valor pago: R$'))


print(somaCaixa)