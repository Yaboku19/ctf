#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Scheletro pwntools: solo setup iniziale, nessuna funzione

from pwn import *
# ---------- Configurazione ----------
BINARY       = 'flag.o'           # percorso al binario locale
REMOTE_HOST  = 'titan.picoctf.net'  # host remoto (ncat / netcat)
REMOTE_PORT  = 54593                     # porta remota
USE_LIBC     = False                # True se vuoi caricare una libc esterna
LIBC_PATH    = './libc.so.6'        # percorso della libc (se USE_LIBC = True)

# ---------- Context ----------
context.binary = ELF(BINARY)        # carica ELF e imposta arch/endianness automaticamente
context.log_level = 'info'          # livelli: debug / info / warning / error / critical

# Carica ELF e (opzionale) libc
elf  = context.binary
libc = ELF(LIBC_PATH) if USE_LIBC else None

# ---------- GDB script / parametri ----------
gdbscript = '''
# put your gdb commands here, e.g.:
# b main
# continue
'''
# ---------- Arg parsing convenzionale ----------
# Avviare lo script in 3 modi:
#   python3 exploit.py           -> locale (process)
#   python3 exploit.py GDB       -> avvia con gdb
#   python3 exploit.py REMOTE    -> connetti in remoto
#
# Non eseguiamo nulla ora; qui definiamo solo le variabili/setting.
mode = 'LOCAL'
if 'REMOTE' in args:
    mode = 'REMOTE'
elif 'GDB' in args:
    mode = 'GDB'

# ---------- Placeholder I/O (non eseguito) ----------
io = None
if mode == 'REMOTE':
    io = remote(REMOTE_HOST, REMOTE_PORT)
elif mode == 'GDB':
    io = gdb.debug([BINARY], gdbscript=gdbscript)
else:
    io = process([BINARY])

print(io.recvuntil(b'Word: ').decode())
word = io.recvuntil(b'Enter the Little Endian representation:').decode().split("\n")[0]
print(word)
little = word.encode()[::-1]
big = word.encode()
io.sendline(little.hex().encode())
print(io.recvuntil("Big Endian representation: "))
io.sendline(big.hex().encode())
print(io.recvall(1))



