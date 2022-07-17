from funcao.calculador import RecebeIp

print('CALCULO DE MASCARA  DE SUB-REDE IPv4')
print('Apenas digitando o IP/CIDR (ex. 192.168.0.1/24), a classe fará os cálculos necessários para retornar o')
print('endereço IPv4, CIDR, Máscara de sub-rede, IP da rede, IP de broadcast da rede, primeiro IP da rede,')
print('último IP da rede, número total de IPs da rede, e o número de IPs disponíveis para uso.')
print('Faça um teste:')
print()
print('CALCULAR MASCARA DE SUB-REDE IPv4')
print('IP/CIDR(Ex:192.168.0.1/24)')
digita_ip = input('Digite o numero de IP/CIDR  ')
if not '/' in digita_ip:
    print('Endereço IPv4 inválido!')
else:
    for d in digita_ip:
        if d.isalpha():
            print('Endereço IPv4 invalido!')
            break
    else:
        print(f'Configurações de rede para {digita_ip}')
        print()
        i = RecebeIp(digita_ip)
        i.detalhes()