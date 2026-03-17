from Conta import Conta

cc = Conta(1234, 'Juca', 1000)
print(f'Saldo: {cc.get_saldo()}')
#saque de 500

cc.saque(500)
cc.saque(700)

cc.deposito(500)

#Usuário não pode ter saldo negativo
print(f'Saldo: {cc.get_saldo()}')

#_________________________________________________ aula dia 16/03 (continuação)
cc2 = Conta(5432, 'Gigi', 1000)

#print(f'Titular com get: {cc2.get_titular()}')
print(f'Titular com property: {cc2.titular}')


#alterando o titular via função set
#cc2.set_titular('Giovanna de Bem')

#alteranado titular via property
cc2.titular = 'Giovanna Rodrigues'

#print(f'Titular alterando com set: {cc2.get_titular()}')
print(f'Titular alterando com property: {cc2.titular}')

cc2.titular = 'G'
print(f'Titular alterando com property: {cc2.titular}')

cc3 = Conta(1111, 'Ana', 1000)
cc4 = Conta(2222, 'Mauro', 700)


print(f'Saldo antes da transferencia [cc3] {cc3.saldo}')
print(f'Saldo antes da transferencia [cc4] {cc4.saldo}')
#transferir 200 de cc3 para cc4
cc3.transfere(200, cc3)
print(f'Saldo depois da transferencia [cc4] {cc3.saldo} ')
print(f'Saldo depois da transferencia [cc5] {cc4.saldo} ')
