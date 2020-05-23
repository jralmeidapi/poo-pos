class Pessoa:
    
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def andar(self):
        print('Caminhando...')

    def comer(self):
        print('Comendo...')

    def dormir(self):
        print('Dormindo...')
        

class PessoaFisica(Pessoa):
    
    def __init__(self, nome, cpf=None, data_nascimento):
        self.cpf = cpf
        super().__init__(nome, data_nascimento)

    def validar_cpf(self):
        if len(self.cpf) == 14:
            print('CPF Válido')
        else:
            print('CPF Inválido')
    

class PessoaJuridica:
    pass
