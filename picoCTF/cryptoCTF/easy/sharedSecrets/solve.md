# Shared Secrets

**Link**: https://play.picoctf.org/practice/challenge/715

**Difficulty**: easy

## Description

A message was encrypted using a shared secret... but it looks like one side of the
exchange leaked something. Can you piece together the secret and get the flag?

## Resources

- **message.txt**: the public Diffie–Hellman parameters, the leaked value, and the ciphertext
- **encryption.py**: the script that produced the ciphertext
- **script.py**: the ready-to-run solver

## The vulnerability

This is Diffie–Hellman key exchange. Normally each side keeps its private exponent
secret, and an attacker who only sees `g`, `p`, `A`, `B` cannot cheaply compute the
shared key (that's the discrete-log problem).

But `message.txt` **leaks the client's private exponent `b`** — the thing that was
supposed to stay secret. In `encryption.py`:

    shared = pow(A, b, p)                          # needs A, b, p — all known!
    enc    = bytes([x ^ (shared % 256) for x in flag])

The flag is just XORed with the single byte `shared % 256`. Since `A`, `b`, `p`,
and `enc` are all in `message.txt`, we can rebuild `shared` and undo the XOR.

## How to solve

Run the solver (`script.py`):

    g   = 2
    p   = 2446679304842267403903261424638695191543543507774999818596978578082983456498...
    A   = 862422939115067914192700651276043434274373147037214152184085135733177420381110...
    b   = 179441385236892902713172352171903829494663627897925180405252254807924564944611...
    enc = "ffe6ece0ccdbc9f4ebe7d0fcbcecfdbcfbd0b9ebeeebbfb6ecebf2"

    shared = pow(A, b, p)
    flag   = bytes([x ^ (shared % 256) for x in bytes.fromhex(enc)])
    print(flag)

Then:

    python3 script.py

(The full `p`, `A`, `b` values are in `message.txt` / `script.py`.)

## Flag

    picoCTF{dh_s3cr3t_6dad09cd}
