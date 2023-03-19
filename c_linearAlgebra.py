class AlgebraLinear:
    @staticmethod
    def sum(termo1, termo2):
        try:
            if len(termo1) != len(termo2) or len(termo1[0]) != len(termo2[0]):
                return None
            m_resultante = [[0 for _ in range(len(termo1[0]))] for _ in range(len(termo1))]
            for i in range(len(termo1)):
                for j in range(len(termo1[0])):
                    m_resultante[i][j] = termo1[i][j] + termo2[i][j]
            return m_resultante
        except TypeError:
            try:
                m_resultante = [[0 for _ in range(len(termo1[0]))] for _ in range(len(termo1))]
                for i in range(len(termo1)):
                    for j in range(len(termo1[0])):
                        m_resultante[i][j] = termo1[i][j] + termo2
                return m_resultante
            except TypeError:
                try:
                    if len(termo1) != len(termo2):
                        return None
                    m_resultante = [0 for _ in range(len(termo1))]
                    for i in range(len(termo1)):
                        m_resultante[i] = termo1[i] + termo2[i]
                    return m_resultante
                except TypeError:
                    m_resultante = [0 for _ in range(len(termo1))]
                    for i in range(len(termo1)):
                        m_resultante[i] = termo1[i] + termo2
                    return m_resultante

    @staticmethod
    def times(termo1, termo2):
        try:
            if len(termo1) != len(termo2) or len(termo1[0]) != len(termo2[0]):
                return None
            m_resultante = [[0 for _ in range(len(termo1[0]))] for _ in range(len(termo1))]
            for i in range(len(termo1)):
                for j in range(len(termo1[0])):
                    m_resultante[i][j] = termo1[i][j] * termo2[i][j]
            return m_resultante
        except TypeError:
            try:
                m_resultante = [[0 for _ in range(len(termo1[0]))] for _ in range(len(termo1))]
                for i in range(len(termo1)):
                    for j in range(len(termo1[0])):
                        m_resultante[i][j] = termo1[i][j] * termo2
                return m_resultante
            except TypeError:
                try:
                    if len(termo1) != len(termo2):
                        return None
                    m_resultante = [0 for _ in range(len(termo1))]
                    for i in range(len(termo1)):
                        m_resultante[i] = termo1[i] * termo2[i]
                    return m_resultante
                except TypeError:
                    m_resultante = [0 for _ in range(len(termo1))]
                    for i in range(len(termo1)):
                        m_resultante[i] = termo1[i] * termo2
                    return m_resultante

    @staticmethod
    def dot(matriz1, matriz2):
        if len(matriz1[0]) != len(matriz2):
            return None
        m_resultante = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
        for i in range(len(matriz1)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    m_resultante[i][j] += matriz1[i][k] * matriz2[k][j]
        return m_resultante

    @staticmethod
    def transpose(termo):
        try:
            m_resultante = [[0 for _ in range(len(termo))] for _ in range(len(termo[0]))]
            for i in range(len(termo)):
                for j in range(len(termo[0])):
                    m_resultante[j][i] = termo[i][j]
            return m_resultante
        except TypeError:
            m_resultante = [[0 for _ in range(1)] for _ in range(len(termo))]
            for i in range(len(termo)):
                for j in range(1):
                    m_resultante[i][j] = termo[i]
            return m_resultante

    @staticmethod
    def gauss(matriz):
        try:
            m = len(matriz)
            n = m + 1

            for k in range(m):
                pivots = [abs(matriz[i][k]) for i in range(k, m)]
                i_max = pivots.index(max(pivots)) + k
                matriz[k], matriz[i_max] = matriz[i_max], matriz[k]

                for i in range(k + 1, m):
                    f = matriz[i][k] / matriz[k][k]
                    for j in range(k + 1, n):
                        matriz[i][j] -= matriz[k][j] * f
                    matriz[i][k] = 0

            resolucao = []
            for i in range(m - 1, -1, -1):
                resolucao.insert(0, matriz[i][m] / matriz[i][i])
                for k in range(i - 1, -1, -1):
                    matriz[k][m] -= matriz[k][i] * resolucao[0]
            return matriz

        except ZeroDivisionError:
            return None

        except IndexError:
            return None

    @staticmethod
    def solve(matriz):
        try:
            m = len(matriz)
            n = m + 1

            for k in range(m):
                pivots = [abs(matriz[i][k]) for i in range(k, m)]
                i_max = pivots.index(max(pivots)) + k
                matriz[k], matriz[i_max] = matriz[i_max], matriz[k]

                for i in range(k + 1, m):
                    f = matriz[i][k] / matriz[k][k]
                    for j in range(k + 1, n):
                        matriz[i][j] -= matriz[k][j] * f
                    matriz[i][k] = 0

            resolucao = []
            for i in range(m - 1, -1, -1):
                resolucao.insert(0, matriz[i][m] / matriz[i][i])
                for k in range(i - 1, -1, -1):
                    matriz[k][m] -= matriz[k][i] * resolucao[0]
            return resolucao

        except ZeroDivisionError:
            return None

        except IndexError:
            return None
