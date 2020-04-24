import socket
from datetime import datetime

class UDPClient:
    # this function use for displaying time for udp_client
    def print_info(self, msg):
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'{current_time} {msg}')
    
    # this function use for creating a UDP socket use IPv4
    # TCP --> SOCK_STREAM, UDP --> SOCK_DGRAM
    # AF_INET use for IPv4, AF_INET6 use for IPv6
    def setup_client(self):
        self.print_info('Đang tạo socket UDP')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.print_info('Đã tạo socket')

    # this function use for sending query to server from client and receiving info of wether of that city/province
    def send_query_to_server(self):
        try:
          while True:
            # send data to server
            self.print_info('Gửi truy vấn của bạn đến server để lấy thông tin thời tiết của tỉnh/thành phố')
            name = input('Tên tỉnh/thành phố cần truy vấn: ')
            self.sock.sendto(name.encode('utf-8'), (self.host, self.port))
            # receive data from server
            server_response, server_address = self.sock.recvfrom(1024) # buffer size is 1024
            self.print_info('Phản hồi từ server\n')
            print(server_response.decode(), '\n')
        except OSError as err:
            # print error
            print(err)
        finally:
            # close socket of client
            self.print_info('Đang đóng socket của client')
            self.sock.close()
            self.print_info('Socket của client đã đóng')

    # this function use for setting up host and port for UDP client
    def __init__(self, host, port):
        self.host = host   
        self.port = port    
        self.sock = None  

def main():
    # selenium server
    udp_client = UDPClient('127.0.0.1', 2020)
    # setup client before connecting to server for sending query
    udp_client.setup_client()
    # send query to server
    udp_client.send_query_to_server()

if __name__ == '__main__':
    main()