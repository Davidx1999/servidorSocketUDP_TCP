import socket
import random

HOST = "127.0.0.1"
PORT = 5001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor TCP rodando em {HOST}:{PORT}")
print("Aguardando conexões...")

while True:
    conexao, endereco_cliente = servidor.accept()

    print(f"\nCliente conectado: {endereco_cliente}")

    dados = conexao.recv(1024)

    mensagem = dados.decode()

    valor_texto, moeda = mensagem.split(";")

    valor_texto = (
        valor_texto
        .replace("R$", "")
        .replace(" ", "")
        .replace(",", ".")
    )

    valor_reais = float(valor_texto)

    cotacao = random.uniform(4.50, 6.00)

    valor_convertido = valor_reais / cotacao

    resposta = (
        f"R$ {valor_reais:.2f} = "
        f"{valor_convertido:.2f} {moeda.upper()} "
        f"(cotação: R$ {cotacao:.2f})"
    )

    conexao.send(resposta.encode())

    print(f"Requisição: {mensagem}")
    print(f"Resposta: {resposta}")

    conexao.close()