from .ipdarede import Endereco
from .macara import SubMascara
from .Rede import IpdaRede
import time


class RecebeIp:

    def __init__(self, ipp, cidr=''):
        self._ipp = ipp
        self._cidr = cidr
        self.lista = []

    @property
    def ipp(self):
        return self._ipp

    @ipp.setter
    def ipp(self, valor):
        self._ipp = valor

    def retira_caracter(self):
        valor = str(self._ipp)
        valor = valor.replace('.', ' ')
        valor = valor.replace('/', ' ')
        self._cidr = int(valor[-2:])
        valor = valor.split(' ')
        self.ipp = list(map(int, valor[:-1]))

    def calcula(self):
        recebe = ''
        i = 0
        i2 = 128
        i3 = 0
        while i < 8:
            if i3 == 4:
                break
            elif i2 <= self.ipp[i3]:
                recebe += '1'
                self.ipp[i3] -= i2
            else:
                recebe += '0'
            i += 1
            i2 /= 2
            if i2 < 1:
                i3 += 1
                i2 = 128
                i = 0
                self.lista.append(recebe)

                recebe = ''
        print(self.lista)

    def detalhes(self):
        time.sleep(0.2)
        print(f'Endereço/Rede:          {self._ipp}')
        rede = IpdaRede(self._ipp)
        time.sleep(0.3)
        self.retira_caracter()
        time.sleep(0.3)
        endereco = Endereco(self._ipp, self._cidr)
        subrede = SubMascara(self._cidr)
        total = SubMascara(self._cidr)
        self._ipp = '.'.join(list(map(str, self._ipp)))
        print(f'Endereço:               {self._ipp}')
        time.sleep(0.3)
        print(f'Prefixo CIDR:           /{self._cidr}')
        time.sleep(0.3)
        subrede.chama()
        time.sleep(0.3)
        rede.ip_rede()
        time.sleep(0.3)
        endereco.broadcast()
        time.sleep(0.1)
        rede.primeirohost()
        endereco.ultimohost()
        total.totalip()


