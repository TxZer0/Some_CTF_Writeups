# -*- coding: utf-8 -*-
from pwn import *  
import re  

def receive_data(connection):
    return connection.recv().decode()  # Nhận dữ liệu và chuyển đổi từ bytes sang string

def parse_data(data):
    return map(int, re.findall("N=(\d+) C=(\d+)", data)[0])  # Sử dụng rex để tìm N và C

def binary_search(connection, N, C):
    start, end = 0, N - 1  
    while start <= end and C > 0:  # Tiếp tục cho đến khi không còn C
        mid = (start + end) // 2  
        connection.sendline(" ".join(map(str, range(start, mid + 1))))
        if int(connection.recvline().strip()) % 10 == 0:
            start = mid + 1  
        else:
            end = mid - 1  
        C -= 1  
    return start, C  

def main():
    p = remote('localhost', 9007)  
    print(receive_data(p))
    for _ in range(100):
        N, C = parse_data(receive_data(p))
        print(N, C) 
        
        start, C = binary_search(p, N, C) 
        while C > 0:  # Lặp cho đến khi hết C 
            p.sendline("0")  
            C -= 1  # Giảm số lượt thử
        p.sendline(str(start))  # Gửi câu trả lời cuối cùng
        print(p.recv())  
    print(p.recv()) # flag 

if __name__ == "__main__":
    main()
