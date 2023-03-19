class Vetor:
    def __init__(self):
        self._tamanho = int(input('Quantos elementos você quer dentro do vetor: '))
        self._elementos = [0 for _ in range(self.tamanho)]

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, value):
        self._tamanho = value

    @property
    def elementos(self):
        return self._elementos

    @elementos.setter
    def elementos(self, value):
        self._elementos = value

    def gerar_vetor(self):
        for i in range(self.tamanho):
            try:
                self.elementos[i] = int(input(f'Digite um valor para posição [{i+1}]: '))
            except ValueError:
                print('Digite somente números inteiros!')
                self.elementos[i] = int(input(f'Digite um valor para posição [{i + 1}]: '))
