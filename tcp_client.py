import socket

HOST = "127.0.0.1"
PORT = 5001

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

valor = input("Digite o valor em reais: ")
moeda = input("Digite a moeda desejada (ex: dolar): ")

mensagem = f"{valor};{moeda}"

cliente.send(mensagem.encode())

resposta = cliente.recv(1024)

print("\nResultado da conversão:")
print(resposta.decode())

cliente.close()