from pwn import *

ssh = ssh(user = 'random', host = 'pwnable.kr', password = 'guest', port = 2222)
process=ssh.process(executable = './random')


payload = str(int(0x6b8b4567 ^ 0xdeadbeef)).encode()
print(payload)
process.sendline(payload)

result=process.recvline()
print(result)

process.interactive()
