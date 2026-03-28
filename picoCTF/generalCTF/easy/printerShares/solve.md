# Printer share

**Link**: https://play.picoctf.org/practice/challenge/759

**Difficulty**: easy

## Description

Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?

## Resources


## How to solve

The serve just give the nc command

    nc -vz mysterious-sea.picoctf.net PORT

Here subclient can be used

For listing the available machines

    smbclient -L //mysterious-sea.picoctf.net -p 52883 -N

This one for connect to one of the machine.

    smbclient //mysterious-sea.picoctf.net/shares -p PORT -N

You for reading a file before neads to be downloaded with

    getting file \flag.txt of size 37 as flag.txt

