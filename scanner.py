import socket
from datetime import datetime

def scanneado_portas(alvo, porta_inicial, portal_final):
    try:
        alvo_ip = socket.gethostbyname(alvo)
    except socket.gaierror:
        print("Erro: não foi possível resolver o domínio.")
        return

    print(f"\nEscaneando: {alvo} ({alvo_ip})")
    print(f"Portas: {porta_inicial} - {portal_final}")
    print(f"Início: {datetime.now()}\n")

    portas_abertas = []

    for porta in range(porta_inicial, portal_final + 1):
        conexao_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao_tcp.settimeout(0.5)

        resultado = conexao_tcp.connect_ex((alvo_ip, porta))

        if resultado == 0:
            try:
                service = socket.getservbyport(porta)
            except:
                service = "desconhecido"

            print(f"[ABERTA] Porta {porta} ({service})")
            portas_abertas.append(porta)

        conexao_tcp.close()

    print("\nScan finalizado.")
    print(f"Portas abertas: {portas_abertas}")


if __name__ == "__main__":
    alvo = input("Alvo (IP ou domínio): ")
    porta_inicial = int(input("Porta inicial: "))
    portal_final = int(input("Porta final: "))

    scanneado_portas(alvo, porta_inicial, portal_final)