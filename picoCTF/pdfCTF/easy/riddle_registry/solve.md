# Riddle Registry

**Link**: https://play.picoctf.org/practice/challenge/530

**Difficulty**: Easy

## Description

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here and uncover the flag within the metadata.

## Resources

**confidential.pdf**: pdf file with the flag

## How to solve

The challenge hint suggests checking the file’s metadata.

By running:

    pdfinfo confidential.pdf

The output will be:

    Author:          cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=
    Producer:        PyPDF2
    Custom Metadata: no
    Metadata Stream: no
    Tagged:          no
    UserProperties:  no
    Suspects:        no
    Form:            none
    JavaScript:      no
    Pages:           1
    Encrypted:       no
    Page size:       612 x 792 pts (letter)
    Page rot:        0
    File size:       182705 bytes
    Optimized:       no
    PDF version:     1.7

The `Author` field clearly looks encoded, and its format matches Base64.

Decode it:

    echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=' | base64 -d

The decoded value is the flag:

    picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
