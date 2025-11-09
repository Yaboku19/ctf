# RED

**Link**: https://play.picoctf.org/practice/challenge/460?page=2

**Difficulty**: easy

## Description

RED, RED, RED, RED

## Resources

**red.png**: the image for the challenge8

## How to solve

By running 

    exiftool red.png

The output will be

    ExifTool Version Number         : 12.76
    File Name                       : red.png
    Directory                       : .
    File Size                       : 796 bytes
    File Modification Date/Time     : 2025:11:07 21:30:40+00:00
    File Access Date/Time           : 2025:11:08 21:34:43+00:00
    File Inode Change Date/Time     : 2025:11:07 21:30:40+00:00
    File Permissions                : -rw-rw-r--
    File Type                       : PNG
    File Type Extension             : png
    MIME Type                       : image/png
    Image Width                     : 128
    Image Height                    : 128
    Bit Depth                       : 8
    Color Type                      : RGB with Alpha
    Compression                     : Deflate/Inflate
    Filter                          : Adaptive
    Interlace                       : Noninterlaced
    Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
    Image Size                      : 128x128
    Megapixels                      : 0.016

To view the poem with proper line breaks, run:

    exiftool -b -Poem red.png

The output will be

    Crimson heart, vibrant and bold,
    Hearts flutter at your sight.
    Evenings glow softly red,
    Cherries burst with sweet life.
    Kisses linger with your warmth.
    Love deep as merlot.
    Scarlet leaves falling softly,
    Bold in every stroke.

Looking at the first letter of every line gives:

    check lsb

This suggests checking the least significant bits of the PNG. By running

    zsteg red.png

The output will be

    meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
    b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
    b1,rgba,msb,xy      .. file: OpenPGP Public Key
    b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
    b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
    b2,bgr,msb,xy       .. file: OpenPGP Public Key
    b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
    b2,rgba,msb,xy      .. text: "CIkiiiII"
    b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
    b2,abgr,msb,xy      .. text: "iiiaakikk"
    b3,rgba,msb,xy      .. text: "#wb#wp#7p"
    b3,abgr,msb,xy      .. text: "7r'wb#7p"
    b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped

There is a repeated base64 string:

    cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==

Decode it by running:

    echo cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== | base64 -d

The output will be:

    picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
