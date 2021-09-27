
def tarefa_1(N):
    lista_de_fora = []
    for i in range(N):
        lista_de_dentro = []
        for j in range(N):
            lista_de_dentro.append(0)
        lista_de_fora.append(lista_de_dentro)
    return lista_de_fora


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    lista = tarefa_1(3)
    print(lista)


if __name__ == '__main__':
    main()
