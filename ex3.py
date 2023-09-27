class Cliente:
    def __init__(self, nome, cpf, senha):
        self. nome = nome
        self. __cpf = cpf
        self. __senha= senha

    def get_senha(self):
        return self.__senha 


class ContaBancaria:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo

    def get_saldo(self, senha):
        return self.__saldo
    
    def depositar(self, senha, valor):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
            return True
        else:
            print('Erro. Senha incoreta')
            return False
    
    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            if valor <= self. __saldo:
                self.__saldo -= valor
                print('Saque realizado com sucesso')
            else:
                print('Erro. Saldo indisponivel')
        else:
            print('senha incorreta')

    

cliente1= Cliente('alana', '43320099822', 1)
conta = ContaBancaria(123, cliente1, 0)

senha = int(input('Informe o senha do usuario: '))
valor = float(input('informe o valor de deposito: '))
conta.depositar(senha, valor)

print('-------------------')

senha = int(input('Informe a senha usuario para visualizar o saldo: '))
print(f'Saldo: {conta.get_saldo(senha)}')


print('-------------------')
valor = float(input('informe o valor para sacar: '))
senha = int(input('Informe a senha: '))
conta.sacar(valor,senha)
print(f'Saldo: {conta.get_saldo(senha)}')
