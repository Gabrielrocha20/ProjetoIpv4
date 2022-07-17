class IpdaRede:
    def __init__(self, ipp):
        self._ipp = ipp

    @property
    def ipp(self):
        return self._ipp

    def ip_rede(self):
        valor = self._ipp
        valor = valor.replace('.', ' ')
        cidr = int(valor[-2:])
        valor = valor.split(' ')
        valor = '.'.join(list(map(str, valor[:-1])))
        self._ipp = valor + f'.0/{cidr}'
        print(f'IP da Rede:             {self._ipp}')

    def primeirohost(self):
        self._ipp = self._ipp[:-4] + '1'
        print(f'Primeiro Host:          {self._ipp}')