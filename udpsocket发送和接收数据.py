import socket

# 判断模块是否是主模块
if __name__ == '__main__':
    # 创建''udpsocket
    print("123")
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 准备发送的数据
    content = "111"
    # 把数据转成二进制
    # 注意：ubuntu网络调试助手是utf-8编码格式，Windows是gbk编码格式
    data = content.encode("gbk")
    # 发送数据
    print("123")
    udp_socket.sendto(data, ("192.168.110.25", 9090))
    # 关闭socket
    print("123")
    udp_socket.close()

import socket

if __name__ == '__main__':
    # 创建udpsocket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送数据
    content = "你好，python"
    data = content.encode("gbk")
    udp_socket.sendto(data, ("192.168.110.25", 9091))
    # 接收数据 前面为接收的数据，后面为ip地址和端口号
    udp_socket_data, ip_port = udp_socket.recvfrom(1024)
    # 解码数据
    udp_socket_content = udp_socket_data.decode("gbk")
    print(udp_socket_content, ip_port)
    # 关闭udpsocket
    udp_socket.close()

# 这是丁雅琪测试
def hi():
    print("hello")