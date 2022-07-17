class Endereco:
    def __init__(self, ipp, cidr):
        self._lista3 = []
        self.brod = None
        self._lista1 = []
        self._masc = ''
        self._ipp = ipp
        self._lista = []
        self._lista2 = ''
        self.cidr = cidr

    @property
    def ipp(self):
        return self._ipp

    @property
    def lista(self):
        return self._lista

    @property
    def lista2(self):
        return self._lista2

    @property
    def masc(self):
        return self._masc

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
                self._lista.append(recebe)

                recebe = ''
        self._lista2 = '.'.join(list(map(str, self._lista)))

    def rede_binario(self):
        self._lista1 = self._lista[:-1]
        self._lista1.append('00000000')
        self._lista1 = '.'.join(list(map(str, self._lista1)))

    def broadcast(self):
        self.calcula()
        self._lista = self._lista[:-1]
        i = 0
        while i < 32:
            if i < self.cidr:
                self._masc += '1'
            else:
                self._masc += '0'
            i += 1
        self._masc = [self._masc[i:i + 8] for i in range(0, len(self._masc), 8)]
        ii1 = 0
        self.brod = ''
        while ii1 < 8:
            for bd in self._masc[3]:
                if '0' in bd:
                    self.brod += '1'
                else:
                    self.brod += '0'
                ii1 += 1

        self._lista.append(self.brod)
        self.brod_numero()

    def brod_numero(self):
        global v
        i = 0
        i2 = 128
        i3 = 0
        i4 = 0
        while i < 8:
            if i3 == 4:
                break
            for v in self._lista[i3]:
                if v == '1':
                    i4 += int(i2)
                    i += 1
                    i2 /= 2
                else:
                    i += 1
                    i2 /= 2
            if i2 < 1:
                i3 += 1
                i2 = 128
                i = 0
                self._lista3.append(i4)
                i4 = 0
        self._lista3 = '.'.join(list(map(str, self._lista3)))
        print(f'Brodcast da Rede:       {self._lista3}')

    def ultimohost(self):
        valor = self._lista3
        valor = list(map(int, valor.split('.')))
        valor[3] = valor[3] - 1
        valor = '.'.join(list(map(str, valor)))
        self._lista3 = valor
        print(f'Ultimo Host:            {self._lista3}')

'''class IpdaRede:
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

class SubMascara:
    def __init__(self, cidr):
        self.iptotal = None
        self.h = None
        self.masc_binario = None
        self.i = None
        self.i3 = None
        self.i4 = None
        self._lista = []
        self.i2 = 128
        self.cidr = cidr
        self._masc = ''

    @property
    def masc(self):
        return self._masc

    @property
    def lista(self):
        return self._lista

    def numero_binario(self):
        i = 0
        while i < 32:
            if i < self.cidr:
                self._masc += '1'
            else:
                self._masc += '0'
            i += 1
        self.masc_binario = [self._masc[i:i + 8] for i in range(0, len(self._masc), 8)]
        h = 0
        for host in self.masc_binario[3]:
            if host == '0':
                h += 1
            else:
                h += 0
        self.h = 2**h - 2
        self.iptotal = 2**h
        self.masc_binario = '.'.join(self.masc_binario)

    def mascara(self):
        global v
        self._masc = [self._masc[i:i + 8] for i in range(0, len(self._masc), 8)]
        i = 0
        i2 = 128
        i3 = 0
        i4 = 0
        while i < 8:
            if i3 == 4:
                break
            for v in self._masc[i3]:
                if v == '1':
                    i4 += int(i2)
                    i += 1
                    i2 /= 2
                else:
                    i += 1
                    i2 /= 2
            if i2 < 1:
                i3 += 1
                i2 = 128
                i = 0
                self._lista.append(i4)
                i4 = 0
        self._lista = '.'.join(list(map(str, self._lista)))
        print(f'Máscara de sub-rede:    {self._lista}')

    def chama(self):
        self.numero_binario()
        self.mascara()

    def totalip(self):
        self.numero_binario()
        print(f'Total de IPs:           {self.h + 2}')
        print(f'Total de IPs para uso:  {self.h}')'''
