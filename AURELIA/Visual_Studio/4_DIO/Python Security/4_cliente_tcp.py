import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()   

print("Socket criado com sucesso")

HostAlvo = input("Digite o Host ou IP a ser conectado: ") #Criando o Host alvo a ser conectado 
PortaAlvo = input("Digite a porta a ser conectada: ") #Porta que irá se conectar

# Tentar a conexão
try:
    s.connect((HostAlvo, int(PortaAlvo)))
    print("Cliente TCP conectado com sucesso no host: " + HostAlvo + " e na porta " + PortaAlvo)
    s.shutdown(2) # Fecha a conexão
except socket.error as e:
    print("Não foi possivel conectar no Host: "+ HostAlvo + "e na porta " + PortaAlvo)    
    print("Erro: {}".format(e))
    sys.exit()
    
# Chamando a função main
if __name__ == "__main__":
    main()