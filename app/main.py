# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, client_add = server_socket.accept() # wait for client
    print(client_socket)
    data = client_socket.recv(4096).decode()
    lst = list(data.split('\r\n'))
    # print(lst)
   
    print(lst[0].split(' '))
    if lst[0].split(' ')[1] == '/':
        client_socket.sendall("HTTP/1.1 200 OK\r\n\r\n".encode('ASCII'))
    elif lst[0].split(' ')[1][:6] == '/echo/':
        string = lst[0].split(' ')[1][6:]
        http_response = f'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(string)}\r\n\r\n{string}'
        client_socket.sendall(http_response.encode('ASCII'))
    else:
        client_socket.sendall('HTTP/1.1 404 Not Found\r\n\r\n'.encode('ASCII'))
    client_socket.close()
    
if __name__ == "__main__":
    main()
