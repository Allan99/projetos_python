#Projeto ainda não terminado 

def ip_binario(ip:str)->str:
    split_ip = ip.replace('.', ' ').split()
    ip_bin_lista = [format(int(e), 'b') for e in split_ip]
    zeroes=''
    for e in range(0, len(ip_bin_lista)):
        if len(ip_bin_lista[e])<8:
            zeroes = '0'*(8-len(ip_bin_lista[e]))
        ip_bin_lista[e] = zeroes+ip_bin_lista[e]
    return ''.join(ip_bin_lista)

def calcular_octeto_da_mascara(octeto_binario:str)->int:
    acumular = 0
    nums = [128, 64, 32, 16, 8, 4, 2, 1]
    for i in range(0, 8):
        if octeto_binario[i] == '1':
            acumular+=nums[i]
    return acumular

class Calculo_ipv4:
    def __init__(self, ip, mascara_de_subRede):
        self.ip = ip
        self.mascara_de_subRede = mascara_de_subRede

    def numero_de_hosts(self):
        bin_ip = ip_binario(self.ip)
        total_elementos_ip_binario = len(bin_ip)
        num_mascara_subRede = int(self.mascara_de_subRede[1:])

        b = total_elementos_ip_binario-num_mascara_subRede

        return (2**b) - 2

    def mascara_de_subRede_decimal(self):
        bin_ip = ip_binario(self.ip)
        fim = 8
        inicio = 0
        i=0
        while True:
            i+=1
            try:
                octeto = bin_ip[inicio:fim]
                inicio+=8
                fim+=8   
                calc_octeto = calcular_octeto_da_mascara(octeto)
            except IndexError:
                break

if __name__ == '__main__':
    calculos_ipv4 = Calculo_ipv4('10.20.12.45', '/26')
    print(calculos_ipv4.numero_de_hosts())
    print(calculos_ipv4.mascara_de_subRede_decimal())
