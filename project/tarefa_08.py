class Animal(object):
    def __init__(self, peso, altura, cor):
        self.peso = peso
        self.altura = altura
        self.cor = cor

    def se_comunica(self):
        raise NotImplementedError('não implementado')

    def respira(self):
        raise NotImplementedError('não implementado')


class Cachorro(Animal):
    def se_comunica(self):
        return 'au au!'

    def respira(self):
        return '*respirando*'

    def __add__(self, other):
        if isinstance(other, Cachorro):
            novo_peso = (self.peso + other.peso)/2
            nova_altura = (self.altura + other.altura)/2

            novo_pelo = ''
            if self.cor == other.cor:
                novo_pelo = self.cor
            else:
                novo_pelo = 'malhado'

            cachorrinho = Cachorro(novo_peso, nova_altura, novo_pelo)
            return cachorrinho


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    pass


if __name__ == '__main__':
    main()
