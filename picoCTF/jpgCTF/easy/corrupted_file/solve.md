# Corrupted_file

**Link**: https://play.picoctf.org/practice/challenge/519

**Difficulty**: easy

## Description

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file here.

## Resources

**file**: the corrupted file

## How to solve

By inspecting the file header:

    hexdump -C -n 8 file

The output will be

    00000000  5c 78 ff e0 00 10 4a 46                           |\x....JF|
    00000008

The first two bytes are incorrect for a JPEG file. Overwrite them with the correct JPEG magic bytes:

    printf "\xFF\xD8" | dd of=file bs=1 count=2 conv=notrunc

Create an image file from the repaired data:

    cat file > img.jpeg

Open `img.jpeg` (or inspect it) and you will find the flag:

    picoCTF{r3st0r1ng_th3_by73s_684e09bc}
