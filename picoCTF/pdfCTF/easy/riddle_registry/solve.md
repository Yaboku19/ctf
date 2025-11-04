# Riddle Registry

**Difficulty**: Easy

## Description

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here and uncover the flag within the metadata.

## Resources

**confidential.pdf**: pdf file with the flag

## How to solve

The text clearly sends an hint. It says to see for metadata.

By running:

```bash
pdfinfo confidential.pdf
```

The output will be

```bash
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
```

The Author looks like it is crypted. In fact it is in base64 format.

By running:

```bash
echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=' | base64 -d
```

The output will be the flag

```bash
picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
```