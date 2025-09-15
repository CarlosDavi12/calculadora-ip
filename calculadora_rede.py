# Programa de cálculo de rede, broadcast e faixa de endereços válidos
# Linguagem: Python 3

import ipaddress

def calcular_rede(ip_input, mask_input):
    try:
        network = ipaddress.IPv4Network(f"{ip_input}/{mask_input}", strict=False)
    except ValueError:
        print("IP ou máscara inválidos.\n")
        return

    print(f"\nEndereço da Rede: {network.network_address}")
    print(f"Endereço de Broadcast: {network.broadcast_address}")

    hosts = list(network.hosts())
    if hosts:
        print(f"Faixa de Endereços Válidos: {hosts[0]} a {hosts[-1]}\n")
    else:
        print("Não há endereços válidos nesta rede.\n")

def main():
    print("=== Calculadora de Rede IPv4 ===")
    while True:
        ip_input = input("Digite o endereço IP (ou 'sair' para encerrar): ")
        if ip_input.lower() == "sair":
            print("Encerrando programa...")
            break
        mask_input = input("Digite a máscara de rede: ")
        calcular_rede(ip_input, mask_input)

if __name__ == "__main__":
    main()
