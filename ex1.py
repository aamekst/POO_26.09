class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__salario
    
    def set_nome(self,nome):
        self.__nome = nome

    def set_cpf(self,cpf):
        self.__cpf = cpf

    def set_salario(self,salario):
        self.__salario = salario


        



func1 = Funcionario("alana", "111222333-22", 1500.0)
print(func1.get_nome())
print(func1.get_cpf())
print(func1.get_salario())

print('-----------------')

func1.set_nome('luara')
func1.set_cpf('43366789990')
func1.set_salario(1000.00)
print(func1.get_nome())
print(func1.get_cpf())
print(func1.get_salario())

