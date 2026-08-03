# Hashcrack

**Link**: https://play.picoctf.org/practice/challenge/475

**Difficulty**: easy

## Description

A company stored a secret message on a server which got breached due to the admin
using weakly hashed passwords. Can you gain access to the secret stored within the
server?

## Resources

None — everything happens over the network.

## How to solve

Connect to the server:

    nc verbal-sleep.picoctf.net <port>

It presents **three** hashes in sequence, each a different algorithm, and asks you
to supply the cracked plaintext for each:

    Welcome!! Looking For the Secret?
    We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
    Enter the password for identified hash:

These are all weak, common passwords. You can identify the algorithm by hash length
and crack them with any lookup service such as [CrackStation](https://crackstation.net),
or locally with `john`/`hashcat`:

| Hash type | Length      | Example      | Cracked      |
|-----------|-------------|--------------|--------------|
| MD5       | 32 hex      | `482c811d…`  | `password123`|
| SHA-1     | 40 hex      |              | `letmein`    |
| SHA-256   | 64 hex      |              | `qwerty098`  |

> Tip to identify a hash locally: `hashid <hash>` or `hash-identifier`.

Enter each plaintext in order:

    password123
    letmein
    qwerty098

After the third, the server prints the flag.

## Flag

    picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}
