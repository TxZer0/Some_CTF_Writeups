from pwn import *
import os

#stage 1
args = ['a']*100
args[65] = '\x00'
args[66] = '\x20\x0a\x0d'

#stage 2
r1, w1 = os.pipe()
os.write(w1,b'\x00\x0a\x00\xff')
r2, w2 = os.pipe()
os.write(w2,b'\x00\x0a\x02\xff')

#stage 3
env = {'\xde\xad\xbe\xef':'\xca\xfe\xba\xbe'}

#stage 4
with open('\x0a','w') as f:
    f.write('\x00\x00\x00\x00')

#stage 5
port = args[67] = '9999'
buf = '\xde\xad\xbe\xef'

#connect
p = process(executable = '/home/input2/input', argv = args,  
    stdin = r1, stderr = r2, env = env)
connect = remote('localhost', int(port))
connect.sendline(buf)
p.interactive()
