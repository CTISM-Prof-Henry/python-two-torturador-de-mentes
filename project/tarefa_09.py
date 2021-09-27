
def tarefa_9():
    tabela_em_codigo = [
       ["preto","preto","preto"],
       ["branco","branco","branco"],
       ["caramelo","caramelo","caramelo"],
       ["preto","branco","malhado"],
       ["caramelo","branco","malhado"],
       ["branco","malhado","malhado"],
       ["preto","malhado","malhado"],
       ["caramelo","malhado","malhado"],
    ]
    with open('tipos_de_pelo.csv', 'w') as some_file:
        for line in tabela_em_codigo:
            some_file.writelines(','.join(line) + '\n')

def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    import pandas as pd
    tarefa_9()
    df = pd.read_csv('tipos_de_pelo.csv', header=None)
    print(df)


if __name__ == '__main__':
    main()
