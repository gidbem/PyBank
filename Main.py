from Conta import Conta

cc = Conta('1234', 'Juca', 1000)
print(f'Saldo: {cc.get_saldo()}')
#saque de 500

cc.saque(500)
cc.saque(700)

cc.deposito(500)

#Usuário não pode ter saldo negativo
print(f'Saldo: {cc.get_saldo()}')
