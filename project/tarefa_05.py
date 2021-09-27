
def tarefa_5(x):
    if x <= 0:
        return 1

    if x == 1:
        return 0

    if x == 2:
        return 1

    return 1 + tarefa_5(x // 2)


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """

    import numpy as np

    x = np.arange(3, 33)
    y = list(map(tarefa_5, x))

    for i in range(len(x)):
        if y[i] != np.floor(np.log2(x[i])):
            print('error for', x[i], ':', y[i], ',', np.floor(np.log2(x[i])))


if __name__ == '__main__':
    main()
