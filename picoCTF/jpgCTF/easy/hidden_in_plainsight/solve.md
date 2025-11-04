# Hidden in plainsight

**Difficulty**: easy

## Description

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

## Resources

**img.jpg**: an image

## How to solve

Search for the metadata

```bash
exiftool img.jpg
```

The output will be:

```bash
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
```

The comment section looks encrypted in base64.

So, by running:

```bash
echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d
```

The output wil be

```bash
steghide:cEF6endvcmQ=u
```

There still looks like that the second part of the string is still encrypted.

By running

```bash
echo 'cEF6endvcmQ=u' | base64 -d
```

The output wil be

```bash
pAzzword
```

so the comment section decrypted is saying ```steghide:pAzzword```

steghide is a tool for getting hidden informations inside a file.

By running

```bash
steghide info img.jpg -p pAzzword
```

The output will be

```bash
"img.jpg":
  format: jpeg
  capacity: 4.0 KB
  embedded file "flag.txt":
    size: 34.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
There is a file called ```flag.txt``` hidden inside the file.

By running

```bash
steghide extract -sf img.jpg -p pAzzword
```

The output will be

```bash
wrote extracted data to "flag.txt".
```

It created a file called ```flag.txt``` with the hidden information inside.

By running 

```bash
cat flag.txt
```

The output will be the flag 

```
picoCTF{h1dd3n_1n_1m4g3_871ba555}
```