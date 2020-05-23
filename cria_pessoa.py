from pessoa import Pessoa, PessoaFisica

pf1 = PessoaFisica("Paulo", "28/09/1945", "123.444.565-45")

print ('Dados da Pessoa 1')
print ('Nome: ', pf1.nome)
print ('cpf: ', pf1.cpf)
print ('data_nascimento: ', pf1.data_nascimento)
pf1.andar()
pf1.comer()
pf1.dormir()
pf1.validar_cpf()
