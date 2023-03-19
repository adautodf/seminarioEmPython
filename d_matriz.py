class Matriz:
    def __init__(self):
        self._linhas = int(input('Número de linhas: '))
        self._colunas = int(input('Número de colunas: '))
        self._elementos = [[0 for _ in range(self.colunas)] for _ in range(self.linhas)]

    @property
    def linhas(self):
        return self._linhas

    @linhas.setter
    def linhas(self, value):
        self._linhas = value

    @property
    def colunas(self):
        return self._colunas

    @colunas.setter
    def colunas(self, value):
        self._colunas = value

    @property
    def elementos(self):
        return self._elementos

    @elementos.setter
    def elementos(self, value):
        self._elementos = value

    def gerar_matriz(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                try:
                    self.elementos[i][j] = int(input(f'Digite os valores para posição [{i + 1}][{j + 1}]: '))
                except ValueError:
                    print('Somente números inteiros!')
                    self.elementos[i][j] = int(input(f'Digite os valores para posição [{i + 1}][{j + 1}]: '))
