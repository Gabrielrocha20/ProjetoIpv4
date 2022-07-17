class SubMascara:
    def __init__(self, cidr):
        self.iptotal = None
        self.h = None
        self.masc_binario = None
        self.cidr = cidr
        self._masc = ''

    @property
    def masc(self):
        return self._masc

    def numero_binario(self):
        h = 0
        self.masc_binario = (self.cidr * '1').ljust(32, '0')

        self.masc_binario = [self.masc_binario[i:i + 8]for i in range(0, len(self.masc_binario), 8)]
        for host in self.masc_binario[3]:
            if host == '0':
                h += 1
            else:
                h += 0
        self.h = 2 ** h - 2
        self.iptotal = 2 ** h
        self.masc_binario = '.'.join(self.masc_binario)

    def mascara(self):
        n = 8
        self._masc = self.masc_binario.replace('.', '')
        self._masc = [str(int(self._masc[i:n + i], 2))for i in range(0, 32, n)]
        self._masc = '.'.join(self._masc)
        print(f'Máscara de sub-rede:    {self._masc}')

    def chama(self):
        self.numero_binario()
        self.mascara()

    def totalip(self):
        self.numero_binario()
        print(f'Total de IPs:           {self.h + 2}')
        print(f'Total de IPs para uso:  {self.h}')


