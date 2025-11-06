# Hidden in plainsight

**Link**: https://play.picoctf.org/practice/challenge/524

**Difficulty**: easy

## Description

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

## Resources

**img.jpg**: an image

## How to solve

Search for the metadata

    exiftool img.jpg

The output will be:

    ExifTool Version Number         : 12.76
    File Name                       : img.jpg
    Directory                       : .
    File Size                       : 74 kB
    File Modification Date/Time     : 2025:11:04 17:46:06+00:00
    File Access Date/Time           : 2025:11:04 17:46:08+00:00
    File Inode Change Date/Time     : 2025:11:04 17:46:06+00:00
    File Permissions                : -rw-rw-r--
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    JFIF Version                    : 1.01
    Resolution Unit                 : None
    X Resolution                    : 1
    Y Resolution                    : 1
    Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
    Image Width                     : 640
    Image Height                    : 640
    Encoding Process                : Baseline DCT, Huffman coding
    Bits Per Sample                 : 8
    Color Components                : 3
    Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
    Image Size                      : 640x640
    Megapixels                      : 0.410

The `Comment` field looks like Base64. Decode it:

    echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d

The output will be:

    steghide:cEF6endvcmQ=u

Decode the second part:

    echo 'cEF6endvcmQ=u' | base64 -d

The output will be:

    pAzzword

The comment reveals `steghide:pAzzword`. Use `steghide` with that password:

    steghide info img.jpg -p pAzzword

The output will be:

    "img.jpg":
      format: jpeg
      capacity: 4.0 KB
      embedded file "flag.txt":
        size: 34.0 Byte
        encrypted: rijndael-128, cbc
        compressed: yes

Extract the hidden file:

    steghide extract -sf img.jpg -p pAzzword

The output will be:

    wrote extracted data to "flag.txt".

Read the flag:

    cat flag.txt

The output will be:

    picoCTF{h1dd3n_1n_1m4g3_871ba555}

