import json

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


def tarefa_10(path):
    cachorras = []

    with open(path, 'r') as some_file:
        dicionario = json.load(some_file)
        for nome_da_cachorra in dicionario:
            nova_cachorra = Cachorro(
                dicionario[nome_da_cachorra]['peso'],
                dicionario[nome_da_cachorra]['altura'],
                dicionario[nome_da_cachorra]['cor'],
            )
            cachorras.append(nova_cachorra)

    return cachorras


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    import os
    print(tarefa_10('exemplo.json'))


if __name__ == '__main__':
    main()
