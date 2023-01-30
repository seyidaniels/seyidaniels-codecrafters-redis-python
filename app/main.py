# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)


    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        conn, _ = server_socket.accept()
        with conn:
            while True:
                # wait for client
                data = conn.recv(1024).decode().split("\n")
                print(f"The server received this from the client {data}")
                conn.send(b"+PONG\r\n")



if __name__ == "__main__":
    main()
