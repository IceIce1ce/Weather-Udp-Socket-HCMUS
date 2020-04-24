import socket
from datetime import datetime

# this UDPServer class will be inherited by UDPServerMultiClient class for handling multi client connect to server
class UDPServer:    
    # this function use for displaying time for udp_server
    def print_info(self, msg):
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'{current_time} {msg}')

    # this function use for creating a UDP socket use IPv4 and binding server to the address
    # TCP --> SOCK_STREAM, UDP --> SOCK_DGRAM
    # AF_INET use for IPv4, AF_INET6 use for IPv6
    def setup_server(self):
        self.print_info('Đang tạo socket UDP')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.print_info('Đã tạo socket')
        self.print_info(f'Liên kết server đến địa chỉ {self.host}:{self.port}')
        self.sock.bind((self.host, self.port))
        self.print_info(f'Server đã liên kết đến địa chỉ {self.host}:{self.port}')

    # this function use for receiving query from client and returning result to clients
    def receive_query_from_client(self, name_city):
        province_data = {'HaNoi': '30 độ C, Có mưa', 'DaNang': '32 độ C, Trời nắng', 'LongAn': '26 độ C, Trời nắng', 'Hue': '28 độ C, Có mưa', 'NgheAn': '30 độ C, Trời nắng', 'DongNai': '33 độ C, Trời nắng', 'BinhDinh': '23 độ C, Có mưa', 'QuangNam': '24 độ C, Trời nắng', 'DaLat': '20 độ C, Có mưa', 'BenTre': '35 độ C, Trời nắng'}
        help_function = {'h': 'Nhập all để truy vấn thông tin thời tiết của toàn bộ tỉnh/thành phố hoặc nhập 1 tỉnh/thành phố nào đó để có thông tin thời tiết của tỉnh/thành phố đó, danh sách các tỉnh/thành phố có thể truy vấn: HaNoi, DaNang, LongAn, Hue, NgheAn, DongNai, BinhDinh, QuangNam, DaLat, BenTre'}
        all_country = {'all': 'Thông tin thời tiết:'}
        if name_city in help_function.keys():
            return f"{help_function[name_city]}"
        if name_city in all_country.keys():
            return f"{all_country[name_city]}\nHaNoi: 30 độ C, Có mưa\nDaNang: 32 độ C, Trời nắng\nLongAn: 26 độ C, Trời nắng\nHue: 28 độ C, Có mưa\nNgheAn: 30 độ C, Trời nắng\nDongNai: 33 độ C, Trời nắng\nBinhDinh: 23 độ C, Có mưa\nQuangNam: 24 độ C, Trời nắng\nDaLat: 20 độ C, Có mưa\nBenTre: 35 độ C, Trời nắng"
        if name_city in province_data.keys():
            return f"Thông tin thời tiết của {name_city}: {province_data[name_city]}"
        else:
            return f"Tỉnh/thành phố {name_city} hiện không có sẵn trong danh sách, các tỉnh thành được hỗ trợ hiện tại: HaNoi, DaNang, LongAn, Hue, NgheAn, DongNai, BinhDinh, QuangNam, DaLat, BenTre"

    # this function use for setting up host and port for UDP server
    def __init__(self, host, port):
        self.host = host    
        self.port = port    
        self.sock = None