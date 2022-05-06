
class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}' 

if __name__ == '__main__':
    ian = Pessoa(nome='Ian')
    luciano = Pessoa(ian,nome='Luciano')
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)