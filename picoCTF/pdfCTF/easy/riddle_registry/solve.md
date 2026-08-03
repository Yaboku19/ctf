# Riddle Registry

**Link**: https://play.picoctf.org/practice/challenge/530

**Difficulty**: easy

## Description

You've stumbled upon a peculiar PDF filled with what seems like nothing more than
garbled nonsense. Amidst the chaos lies a hidden treasure—an elusive flag waiting
to be uncovered in the metadata.

## Resources

- **confidential.pdf**: the PDF hiding the flag in its metadata

## How to solve

1. The description points straight at the **metadata**, so dump it:

       pdfinfo confidential.pdf

   The `Author` field stands out — it's a Base64 string (mixed case, `+`/`/`,
   trailing `=` padding):

       Author:   cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=
       Producer: PyPDF2

2. **Decode it:**

       echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=' | base64 -d

> `exiftool confidential.pdf` shows the same field if `pdfinfo` isn't installed.

## Flag

    picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
