def tarefa_2(numero):
    lista_numeros_convertidos = []

    # -1.3|+5.4
    numero_a_ser_convertido = []
    for caractere in numero:
        if caractere in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '+', '-']:
            numero_a_ser_convertido.append(caractere)
        else:
            lista_numeros_convertidos.append(
                float(''.join(numero_a_ser_convertido))
            )
            numero_a_ser_convertido = []

    lista_numeros_convertidos.append(
        float(''.join(numero_a_ser_convertido))
    )

    return lista_numeros_convertidos


def main():
    """
    Use esta função para testar como você está resolvendo os exercícios.
    """
    print(tarefa_2('1,2,3,4'))
    print(tarefa_2('1;2;3;4'))
    print(tarefa_2('1a2b3c4'))
    print(tarefa_2('-1.3|+5.4'))


if __name__ == '__main__':
    main()
