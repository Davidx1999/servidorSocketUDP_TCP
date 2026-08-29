import socket
import random

HOST = "127.0.0.1"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST, PORT))

print(f"Servidor UDP rodando em {HOST}:{PORT}")
print("Aguardando conversões...")

while True:
    dados, endereco_cliente = servidor.recvfrom(1024)

    mensagem = dados.decode()

    valor_texto, moeda = mensagem.split(";")
    valor_reais = float(valor_texto)

    cotacao = random.uniform(4.50, 6.00)

    valor_convertido = valor_reais / cotacao

    resposta = (
        f"R$ {valor_reais:.2f} = "
        f"{valor_convertido:.2f} {moeda.upper()} "
        f"(cotação: R$ {cotacao:.2f})"
    )

    servidor.sendto(resposta.encode(), endereco_cliente)

    print(f"Cliente {endereco_cliente}: {mensagem}")
    print(f"Resposta: {resposta}")