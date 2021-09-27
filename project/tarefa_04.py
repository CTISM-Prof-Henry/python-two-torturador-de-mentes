
def tarefa_4(x):
    if x <= 0:
        return 1

    if x == 1:
        return 0

    contador = 0
    while x >= 2:
        contador += 1
        x = x // 2
    return contador


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    pass


if __name__ == '__main__':
    main()
