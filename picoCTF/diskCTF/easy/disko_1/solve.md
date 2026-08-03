# Disko 1

**Link**: https://play.picoctf.org/practice/challenge/505

**Difficulty**: easy

## Description

Can you find the flag in this disk image?

## Resources

- **disko-1.dd.gz**: the gzip-compressed disk image (extracts to `disko-1.dd`)

## How to solve

1. Decompress the disk image:

       gunzip disko-1.dd.gz

2. The flag is stored as plain text somewhere on the filesystem, so a raw string
   search across the whole image finds it without mounting anything:

       strings disko-1.dd | grep -i pico

   Output:

       picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}

> If `grep` had come up empty, the next steps would be to inspect the partition
> table (`fdisk -l disko-1.dd`), carve files with `binwalk -e` / `foremost`, or
> mount it read-only (`sudo mount -o ro,loop disko-1.dd /mnt`).

## Flag

    picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
