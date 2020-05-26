from conta import Conta

c1 = Conta("Paulo", "Pagar", "10/06/2020", "200" )

print('Dados da Conta')
print('Nome: ', c1.nome_pessoa)
print('Tipo de Conta: ', c1.tipo_conta)
print('Data Vencimento: ', c1.data_vencimento)
print('Valor: ', c1.valor)

c2 = Conta("Maria", "Receber", "15/08/2020", "1000" )

print('Dados da Conta')
print('Nome: ', c2.nome_pessoa)
print('Tipo de Conta: ', c2.tipo_conta)
print('Data Vencimento: ', c2.data_vencimento)
print('Valor: ', c2.valor)