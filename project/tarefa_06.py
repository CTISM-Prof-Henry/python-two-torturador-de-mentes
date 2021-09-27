class Animal(object):
    def __init__(self, peso, altura, cor):
        self.peso = peso
        self.altura = altura
        self.cor = cor

    def se_comunica(self):
        raise NotImplementedError('não implementado')

    def respira(self):
        raise NotImplementedError('não implementado')


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    pass


if __name__ == '__main__':
    main()
