# RED

**Link**: https://play.picoctf.org/practice/challenge/460

**Difficulty**: easy

## Description

RED, RED, RED, RED

## Resources

- **red.png**: a 128×128 solid-red PNG

## How to solve

Two stages: an acrostic hint in the metadata, then LSB steganography.

1. **Read the metadata** — there's a custom `Poem` field:

       exiftool red.png

   View it with line breaks preserved:

       exiftool -b -Poem red.png

       Crimson heart, vibrant and bold,
       Hearts flutter at your sight.
       Evenings glow softly red,
       Cherries burst with sweet life.
       Kisses linger with your warmth.
       Love deep as merlot.
       Scarlet leaves falling softly,
       Bold in every stroke.

2. **Read the acrostic** — the first letter of each line spells the next step:

       C H E C K   L S B   ->  "check lsb"

3. **Extract the LSB data** with `zsteg` (for PNGs):

       zsteg red.png

   The `b1,rgba,lsb,xy` channel holds a repeated Base64 string:

       cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==

4. **Decode it:**

       echo 'cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==' | base64 -d

> Install if needed: `gem install zsteg`. For a quick one-shot on the LSB plane you
> could also use `zsteg -E b1,rgba,lsb,xy red.png`.

## Flag

    picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
