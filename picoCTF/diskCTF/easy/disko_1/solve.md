# Disko 1

**Link**: https://play.picoctf.org/practice/challenge/505

**Difficulty**: easy

## Description

Can you find the flag in this disk image?
Download the disk image here.

## Resources

**disko-1.dd.gz**: the disk

## How to solve

unzip the the disk

    gunzip disko-1.dd.gz

Then let's search for the flag

    strings disko-1.dd | grep -i pico

in the output there will be

    picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}