# Corrupted File

**Link**: https://play.picoctf.org/practice/challenge/519

**Difficulty**: easy

## Description

This file seems broken... or is it? Maybe a couple of bytes could make all the
difference. Can you figure out how to bring it back to life?

## Resources

- **file**: the corrupted file
- **img.jpeg**: the repaired image (produced during the solve)

## How to solve

1. **Inspect the header.** File type detection relies on "magic bytes" at the very
   start of a file. Dump the first bytes:

       hexdump -C -n 8 file

   Output:

       00000000  5c 78 ff e0 00 10 4a 46   |\x....JF|

2. A real JPEG must start with `FF D8` (and here we can already see `FF E0 … JF`
   from the JFIF marker just after). Instead the file begins with the literal ASCII
   `\x` (bytes `5c 78`) — the correct `FF D8` magic was replaced with the text
   `\x`. Overwrite those first two bytes in place:

       printf '\xFF\xD8' | dd of=file bs=1 count=2 conv=notrunc

   - `conv=notrunc` keeps the rest of the file intact.
   - `count=2` overwrites exactly the two bad bytes.

3. Give it a `.jpeg` name and open it:

       cp file img.jpeg
       xdg-open img.jpeg      # or just view it

   The flag is written inside the image.

## Flag

    picoCTF{r3st0r1ng_th3_by73s_684e09bc}
