class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero
    
    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self,titulo):
        self.__titulo = titulo
    
    def set_titulo(self,genero):
        self.__genero = genero

filmes = []

for f in range(3):
    titulo = str(input('digite o titulo: '))
    genero = str(input('digite o genero: '))
    filme= Filme(titulo, genero)
    filmes.append(filme)

for filme in filmes:
    print(f'filme: {filme.get_titulo()} genero: {filme.get_genero()}')
 
