class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod 
    def metodo_estatico():
        return 26
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    ian = Pessoa(nome='Ian')
    luciano = Pessoa(ian,nome='Luciano')
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    Pessoa.olhos = 3
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(ian.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(ian.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(ian.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    