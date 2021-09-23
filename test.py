import unittest
from inspect import signature


class TestaTudo(unittest.TestCase):
    def testa_soma(self):
        from project.tarefa_00 import tarefa_0 as func
        params = signature(func).parameters
        self.assertEqual(len(params), 2, "A função deveria ter 2 parâmetros")
        self.assertEqual(func(3, 2), 5, "3 + 2 com função soma deveria ser igual a 5")

    def test_01(self):
        from project.tarefa_01 import tarefa_1 as func
        n_params = 1

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)
        self.assertListEqual(func(4), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "Saída incorreta para N=4")
        self.assertListEqual(func(3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "Saída incorreta para N=3")
        self.assertListEqual(func(2), [[0, 0], [0, 0]], "Saída incorreta para N=2")
        self.assertListEqual(func(1), [[0]], "Saída incorreta para N=1")

    def test_02(self):
        from project.tarefa_02 import tarefa_2 as func
        n_params = 1

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)
        self.assertListEqual(func('1,2,3,4'), [1, 2, 3, 4], "Saída incorreta para '1,2,3,4'")
        self.assertListEqual(func('1;2;3;4'), [1, 2, 3, 4], "Saída incorreta para '1;2;3;4'")
        self.assertListEqual(func('1a2b3c4'), [1, 2, 3, 4], "Saída incorreta para '1a2b3c4'")
        self.assertListEqual(func('-1.3|+5.4'), [-1.3, 5.4], "Saída incorreta para '_1.3|+5.4'")

    def test_03(self):
        from project.tarefa_03 import tarefa_3 as func
        n_params = 2

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)
        self.assertEqual(func({'a': 1, 'b': 2}, 2), True, "2 é valor de 'b' no dicionário {'a': 1, 'b': 2}")
        self.assertEqual(func({2: 1, 3: 2}, 2), True, "2 é valor de 3 no dicionário {2: 1, 3: 2}")
        self.assertEqual(func({2: 1, 3: 1}, 2), False, "2 não é valor de nenhuma chave em {2: 1, 3: 1}")

    def test_04(self):
        from project.tarefa_04 import tarefa_4 as func
        import inspect
        from project import tarefa_04
        n_params = 1

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)

        modules = inspect.getmembers(tarefa_04, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')
        modules = inspect.getmembers(func, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')

        import numpy
        for x in range(3, 33):
            inferred = func(x)
            correct = numpy.floor(numpy.log2(x))
            self.assertEqual(inferred, correct, 'log_2(%d) deveria ser %d, mas é %d' % (x, correct, inferred))
            break

    def test_05(self):
        from project.tarefa_05 import tarefa_5 as func
        import inspect
        from project import tarefa_05
        n_params = 1

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)

        modules = inspect.getmembers(tarefa_05, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')
        modules = inspect.getmembers(func, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')

        import numpy
        for x in range(3, 33):
            inferred = func(x)
            correct = numpy.floor(numpy.log2(x))
            self.assertEqual(inferred, correct, 'log_2(%d) deveria ser %d, mas é %d' % (x, correct, inferred))
            break

    def test_06(self):
        from project.tarefa_06 import Animal
        obj = Animal(peso=37., altura=40., cor='branco')
        try:
            obj.respira()
            raise ValueError('O método respira da classe Animal deveria lançar uma exceção do tipo NotImplementedError!')
        except NotImplementedError:
            pass

        try:
            obj.se_comunica()
            raise ValueError(
                'O método se_comunica da classe Animal deveria lançar uma exceção do tipo NotImplementedError!')
        except NotImplementedError:
            pass

    def test_07(self):
        import inspect
        from project.tarefa_07 import Cachorro

        supers = inspect.getmro(Cachorro)
        self.assertTrue(any(['Animal' in str(x) for x in list(supers)]), 'Cachorro não herdou a classe animal!')

        obj = Cachorro(peso=37., altura=40., cor='branco')
        try:
            res = obj.respira()
            self.assertEqual(res.lower(), '*respirando*', 'Método respira deveria retornar uma string!')
        except NotImplementedError:
            raise ValueError('O método respira da classe cachorro não deveria lançar uma exceção!')

        try:
            res = obj.se_comunica()
            self.assertEqual(res.lower(), 'au au!', 'Método se_comunica deveria retornar uma string!')
        except NotImplementedError:
            raise ValueError('O método se_comunica da classe cachorro não deveria lançar uma exceção!')

    def test_08(self):
        from project.tarefa_08 import Cachorro
        import itertools as it

        a = Cachorro(peso=1., altura=3., cor='branco')
        b = Cachorro(peso=2., altura=2., cor='preto')
        c = Cachorro(peso=5., altura=7., cor='caramelo')

        combs = it.combinations([a, b, c], 2)
        for c1, c2 in combs:
            res = c1 + c2
            self.assertEqual(res.peso, (c1.peso + c2.peso) / 2., "O peso do filhote deve ser a média do peso dos pais!")
            self.assertEqual(res.altura, (c1.altura + c2.altura) / 2., "A altura do filhote deve ser a média da altura dos pais!")
            if c1.cor == c2.cor:
                self.assertEqual(res.cor, c1.cor, 'Quando os pais possuem a mesma pelagem, a pelagem do filhote é igual!')
            else:
                self.assertEqual(res.cor, 'malhado', 'Quando os pais possuem pelagens diferentes, a pelagem do filhote é malhada')

    def test_09(self):
        from project.tarefa_09 import tarefa_9 as func
        import inspect
        from project import tarefa_09
        n_params = 0

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)

        modules = inspect.getmembers(tarefa_09, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')
        modules = inspect.getmembers(func, inspect.ismodule)
        self.assertEqual(len(modules), 0, 'Você não deveria usar nenhuma biblioteca para resolver este exercício!')

        import pandas as pd
        import numpy as np
        import os
        df = pd.read_csv(os.path.join('project', 'tipos_de_pelo.csv'), header=None)
        self.assertEqual(len(df), 8, "A tabela deve possuir 8 linhas!")
        self.assertEqual(len(df.columns), 3, "A tabela deve possuir 3 colunas!")
        self.assertTrue(np.any(df.values == "preto"), "Não achei a cor 'preto' na tabela. Certeza que escreveu certo?")
        self.assertTrue(np.any(df.values == "branco"), "Não achei a cor 'branco' na tabela. Certeza que escreveu certo?")
        self.assertTrue(np.any(df.values == "caramelo"), "Não achei a cor 'caramelo' na tabela. Certeza que escreveu certo?")
        self.assertTrue(np.any(df.values == "malhado"), "Não achei a cor 'malhado' na tabela. Certeza que escreveu certo?")

    def test_10(self):
        from project.tarefa_10 import tarefa_10 as func
        from project.tarefa_10 import Cachorro
        n_params = 1

        # testa número de parâmetros
        params = signature(func).parameters
        self.assertEqual(len(params), n_params, "A função deveria ter %d parâmetros" % n_params)

        import os
        read_dogs = func(os.path.join('project', 'exemplo.json'))
        actual_dict = {
            "frida": {
                "peso": 5.3,
                "altura": 20.7,
                "cor": "branca"
            },
            "poly": {
                "peso": 15.3,
                "altura": 40.0,
                "cor": "preta"
            }
        }
        inst_dogs = [
            Cachorro(
                peso=actual_dict['frida']['peso'],
                altura=actual_dict['frida']['altura'],
                cor=actual_dict['frida']['cor']
            ),
            Cachorro(
                peso=actual_dict['poly']['peso'],
                altura=actual_dict['poly']['altura'],
                cor=actual_dict['poly']['cor']
            )
        ]

        import itertools as it
        count_equal = 0
        for a, b in it.product(inst_dogs, read_dogs):
            if (a.cor == b.cor) and (abs(a.peso - b.peso) < 0.1) and (abs(a.altura - b.altura) < 0.1):
                count_equal += 1

        self.assertEqual(count_equal, 2, "As listas de cachorras não são iguais!")


if __name__ == '__main__':
    unittest.main()
