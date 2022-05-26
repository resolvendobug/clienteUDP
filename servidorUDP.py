import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

s.bind((host,port))

mensagem = '\nOlá cliente!'

while 1:
    dados , end = s.recvfrom(4096)

    if dados:
        print('Enviando Msg:')
        s.sendto(dados + (mensagem.encode()),end)

