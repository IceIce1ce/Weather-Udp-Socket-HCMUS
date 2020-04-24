import socket
import threading
import time
import udp_server
from datetime import datetime

class UDPServerMultiClient(udp_server.UDPServer):
    # this function handle query from client
    def handle_query_from_client(self, data, client_address):
        # handle query
        name = data.decode('utf-8')
        response = self.receive_query_from_client(name)
        self.print_info(f'Đã nhận yêu cầu truy vấn từ client {client_address}')
        print('\n', name, '\n')
        # send response to the client after fnishing handle query
        self.print_info(f'Phản hồi đến client {client_address}')
        with self.socket_lock:
            self.sock.sendto(response.encode('utf-8'), client_address)
        print('\n', response, '\n')

    # this function use for handling multiple clients connect to server
    def wait_for_client_connect_to_server(self):
        try:
            # keep server still connect after responding to a client
            while True: 
                try: 
                    # receive query from client
                    data, client_address = self.sock.recvfrom(1024) # buffer size is 1024
                    SC_thread = threading.Thread(target = self.handle_query_from_client, args = (data, client_address))
                    SC_thread.daemon = True
                    SC_thread.start()
                except OSError as err:
                    # print error
                    self.print_info(err)
        # close socket of server
        except KeyboardInterrupt:
            self.print_info('Đang đóng socket của server')
            self.sock.close()
            self.print_info('Socket của server đã đóng')

    # this function use for setting up host and port for UDP server
    # use lock to ensure only one thread uses sendto() at a time
    def __init__(self, host, port):
        super().__init__(host, port)
        self.socket_lock = threading.Lock()

def main():
    # selenium server
    udp_server_multi_client = UDPServerMultiClient('127.0.0.1', 2020)
    # setup server for receive query from client
    udp_server_multi_client.setup_server()
    # wait for multi client connect to server 
    udp_server_multi_client.wait_for_client_connect_to_server()

if __name__ == '__main__':
    main()