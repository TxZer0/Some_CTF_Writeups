from pwn import *

hashcode = 0x21DD09EC
num = hashcode // 5
mod = hashcode % 5

payload = p32(num)*4
payload += p32(num + mod)
print(payload)

ssh = ssh(user = 'col', host = 'pwnable.kr', password = 'guest', port = 2222)
process=ssh.process(executable = './col', argv = ['col',payload])

result = process.recvline()
print(result)

process.interactive()
