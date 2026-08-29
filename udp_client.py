import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

valor = input("Digite o valor em reais: R$ ")
moeda = input("Digite a moeda desejada (ex: dolar): ")

mensagem = f"{valor};{moeda}"

cliente.sendto(mensagem.encode(), (HOST, PORT))

resposta, servidor = cliente.recvfrom(1024)

print("\nResultado da conversão:")
print(resposta.decode())

cliente.close()