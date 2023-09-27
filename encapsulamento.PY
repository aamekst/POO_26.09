#encapsulamento

class ContaBancaria:
    def __init__(self, numero, titular, saldo, senha):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            if valor <= self. _saldo:
                self.__saldo -= valor
                print('Saque realizado com sucesso')
            else:
                print('Erro. Saldo indisponivel')
    

    def depositar (self, valor, senha):
       if self.__validar_senha(senha): #chama o metodo privado
            self.__saldo += valor
            print('Deposito realizado com sucesso')


    def get_saldo(self, senha):
        if self.__validar_senha(senha):
            return self.__saldo


    def __validar_senha(self,senha):# metodo privado usa 2 __de validação
        if senha == self.__senha:
            return True
        else:
            print('Erro. Senha incoreta')
            exit()
            return False
    
conta = ContaBancaria(123, 'alana', 0, 1)

while True:
    print('1 - Deposito')
    print('2 - Saque')
    print('3 - Saldo')
    print('4 - Encerrar')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        valor = float(input('Informe o valor:'))
        senha = int(input('Infome a senha: '))
        conta.depositar(valor,senha)
    elif opcao == 2:
        valor = float(input('Informe o valor:'))
        senha = int(input('Infome a senha: '))
        conta.sacar(valor,senha)
    elif opcao == 3:
        senha = int(input('Informe a senha: '))
        print(f'Saldo: {conta.get_saldo(senha)}')
    elif opcao == 4:
        print('Programa finalizado.')
        break
    else:
        print('Opção')


'''
valor = float(input('informe o valor de deposito: '))
senha = int(input('Informe o senha: '))
conta.depositar(valor, senha)

senha = int(input('Informe a senha: '))
print(f'Saldo: {conta.get_saldo(senha)}')

valor = float(input('informe o valor para sacar: '))
senha = int(input('Informe a senha: '))
conta.sacar(valor,senha)

print(f'Saldo: {conta.get_saldo(senha)}')
'''
#print(conta.get_saldo())#ve o saldo pelo metodo