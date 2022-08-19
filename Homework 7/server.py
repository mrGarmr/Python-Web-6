import socket
from unittest import result

def echo_server(host, port):
     with socket.socket() as sock:

        close = False
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        conn, addr = sock.accept()
        print(f"Connected by {addr}")
        with conn:
            data = conn.recv(1024)
            print(f'Got information: {data}')
            if data != b'Bye':
                try:
                    result = str(eval(data.decode("utf-8")))
                    print(result)
                    conn.send(bytes(result, 'utf-8'))
                except:
                    conn.send(b"Its not so easy to do. Try to easier example. Or write Bye to exit.")
            elif data == b'Bye':
                conn.send(b'Bye')
                close = True
                return close
            else:
                conn.send(b"Its not so easy to do. Try to easier example. Or write Bye to exit.")

                # if data == b'Hello world':
                #     conn.send(b"Oh. I'm just a fake server ;)")
                # elif data == b'Bye':
                #     conn.send(b'Bye')
                #     close = True
                #     return close
                # else:
                #     conn.send(bytes(data.upper()))


if __name__ == '__main__':

    print("Поднимаем сервер с колен...")
    while True:
       if echo_server('127.0.0.1', 8000):
           break