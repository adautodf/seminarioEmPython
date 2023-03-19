from copy import deepcopy
from d_matriz import Matriz
from e_vetor import Vetor
from c_linearAlgebra import AlgebraLinear


class Programa:
    @staticmethod
    def iniciar():
        while True:
            print('Olá bem vindo ao Cenário 1 de matemática.\n'
                  'Para começarmos, vamos gerar uma matriz.')
            m1 = Matriz()
            m1.gerar_matriz()
            M1 = m1.elementos
            print()

            print('Agora vamos criar outra matriz.')
            m2 = Matriz()
            m2.gerar_matriz()
            M2 = m2.elementos
            print()

            print('Já que criamos as matrizes, vamos para os vetores.')
            v1 = Vetor()
            v1.gerar_vetor()
            V1 = v1.elementos
            print()

            print('Agora vamos criar outro vetor.')
            v2 = Vetor()
            v2.gerar_vetor()
            V2 = v2.elementos
            print()

            while True:
                resposta = int(input('Digite 1 para realizar operações entre matrizes.\n'
                                     'Digite 2 para realizar operações entre vetores.\n'
                                     'Digite 3 para reiniciar o programa.\n'))
                print()

                if resposta == 1:
                    while True:
                        print('Lembrando que as operações serão feitas entre as matrizes já criadas.')
                        resposta = int(input('Digite 0 para sair do programa.\n'
                                             'Digite 1 para fazer a soma das matrizes.\n'
                                             'Digite 2 para fazer a soma de uma matriz com um escalar.\n'
                                             'Digite 3 para fazer a multiplicação termo a termo das matrizes.\n'
                                             'Digite 4 para fazer a multiplicação de uma matriz com um escalar.\n'
                                             'Digite 5 para fazer a multiplicação entre matrizes.\n'
                                             'Digite 6 para fazer a transposta das matrizes.\n'
                                             'Digite 7 para escalonar a matriz.\n'
                                             'Digite 8 para resolver o sistema de equações lineares.\n'))
                        print()

                        if resposta == 0:
                            break

                        if resposta == 1:
                            print('Soma de M1 com M2:')
                            resultado_soma_m = AlgebraLinear.sum(M1, M2)
                            if resultado_soma_m is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_soma_m:
                                    print(_)
                                print()

                        if resposta == 2:
                            print('Soma da M1:')
                            resultado_soma_e_m1 = AlgebraLinear.sum(M1, int(input('Digite o escalar: ')))
                            for _ in resultado_soma_e_m1:
                                print(_)
                            print()

                            print('Soma da M2:')
                            resultado_soma_e_m2 = AlgebraLinear.sum(M2, int(input('Digite o escalar: ')))
                            for _ in resultado_soma_e_m2:
                                print(_)
                            print()

                        if resposta == 3:
                            print('Multiplicação times entre M1 e M2:')
                            resultado_times_m = AlgebraLinear.times(M1, M2)
                            if resultado_times_m is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_times_m:
                                    print(_)
                                print()

                        if resposta == 4:
                            print('Multiplicação times da M1:')
                            resultado_times_e_m1 = AlgebraLinear.times(M1, int(input('Digite o escalar: ')))
                            for _ in resultado_times_e_m1:
                                print(_)
                            print()

                            print('Multiplicação times da M2:')
                            resultado_times_e_m2 = AlgebraLinear.times(M2, int(input('Digite o escalar: ')))
                            for _ in resultado_times_e_m2:
                                print(_)
                            print()

                        if resposta == 5:
                            print('Multiplicação dot entre M1 e M2:')
                            resultado_dot = AlgebraLinear.dot(M1, M2)
                            if resultado_dot is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_dot:
                                    print(_)
                                print()

                        if resposta == 6:
                            print('Transposta da M1: ')
                            resultado_transpose_m1 = AlgebraLinear.transpose(M1)
                            for _ in resultado_transpose_m1:
                                print(_)
                            print()

                            print('Transposta da M2: ')
                            resultado_transpose_m2 = AlgebraLinear.transpose(M2)
                            for _ in resultado_transpose_m2:
                                print(_)
                            print()

                        if resposta == 7:
                            print('Resultado M1:')
                            m1_alterada_g = deepcopy(M1)
                            resultado_gauss1 = AlgebraLinear.gauss(m1_alterada_g)
                            if resultado_gauss1 is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_gauss1:
                                    print(_)
                                print()

                            print('Resultado M2:')
                            m2_alterada_g = deepcopy(M2)
                            resultado_gauss2 = AlgebraLinear.gauss(m2_alterada_g)
                            if resultado_gauss2 is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_gauss2:
                                    print(_)
                                print()

                        if resposta == 8:
                            print('Resolução da M1:')
                            m1_alterada_solve = deepcopy(M1)
                            resultado_solve1 = AlgebraLinear.solve(m1_alterada_solve)
                            if resultado_solve1 is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_solve1:
                                    print(f'{_:.2f}')
                                print()

                            print('Resolução de M2:')
                            m2_alterada_solve = deepcopy(M2)
                            resultado_solve2 = AlgebraLinear.solve(m2_alterada_solve)
                            if resultado_solve2 is None:
                                print('Impossível fazer essa operação!')
                                print()
                            else:
                                for _ in resultado_solve2:
                                    print(f'{_:.2f}')
                                print()

                elif resposta == 2:
                    while True:
                        print('Lembrando que as operações serão feitas entre os vetores já criados.')
                        resposta = int(input('Digite 0 para sair do programa.\n'
                                             'Digite 1 para fazer a soma dos vetores.\n'
                                             'Digite 2 para fazer a soma de um vetor com um escalar.\n'
                                             'Digite 3 para fazer a multiplicação dos vetores.\n'
                                             'Digite 4 para fazer a multiplicação de um vetor com um escalar.\n'
                                             'Digite 5 para fazer a transposta dos vetores.\n'))
                        print()

                        if resposta == 0:
                            break
                            print()

                        if resposta == 1:
                            print('Soma de V1 com V2:')
                            resultado_soma_v = AlgebraLinear.sum(V1, V2)
                            if resultado_soma_v is None:
                                print('Impossível fazer a operação!')
                            else:
                                print(resultado_soma_v)
                            print()

                        if resposta == 2:
                            print('Soma do V1:')
                            resultado_soma_e_v1 = AlgebraLinear.sum(V1, int(input('Digite o escalar: ')))
                            print(resultado_soma_e_v1)
                            print()

                            print('Soma do V2:')
                            resultado_soma_e_v2 = AlgebraLinear.sum(V2, int(input('Digite o escalar: ')))
                            print(resultado_soma_e_v2)
                            print()

                        if resposta == 3:
                            resultado_times_v = AlgebraLinear.times(V1, V2)
                            if resultado_times_v is None:
                                print('Impossível fazer a operação!')
                            else:
                                print(resultado_times_v)
                            print()

                        if resposta == 4:
                            print('Multiplicação do V1:')
                            resultado_times_e_v1 = AlgebraLinear.times(V1, int(input('Digite o escalar: ')))
                            print(resultado_times_e_v1)
                            print()

                            print('Multiplicação do V2')
                            resultado_times_e_v2 = AlgebraLinear.times(V2, int(input('Digite o escalar: ')))
                            print(resultado_times_e_v2)
                            print()

                        if resposta == 5:
                            print('Transposta do V1: ')
                            resultado_transpose_v1 = AlgebraLinear.transpose(V1)
                            for _ in resultado_transpose_v1:
                                print(_)
                            print()

                            print('Transposta do V2: ')
                            resultado_transpose_v2 = AlgebraLinear.transpose(V2)
                            for _ in resultado_transpose_v2:
                                print(_)
                            print()

                elif resposta == 3:
                    break
