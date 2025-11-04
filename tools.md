# Tools

A quick reference of useful tools and commands for CTF challenges.

---

## 1. Connection

### SSH
```bash
ssh -p <port> <user>@<domain>
```

### Netcat

```bash
nc <domain> <port>
```

---

## 2. Decrypt / Decode

### Base64
```bash
 base64 -d 
```
Example:
```bash
echo 'c3RyaW5n' | base64 -d
```

### Base32
```bash 
base32 -d 
```
Example:
```bash
echo 'c3RyaW5n' | base32 -d
```

### Hexadecimal
```bash
xxd -r -p <in.txt> > <out.bin>
strings <out.bin>
cat <out.bin>
```
Example:
```bash
echo '7069636f' > hex.txt && xxd -r -p hex.txt > out.bin && strings out.bin
```

---

## 3. Search Files (find / grep)

### Find files by name (case-insensitive)
```bash
find . -type f -iname '*picoCTF*'
```

### Grep recursively for text inside files (exclude .git)
```bash
grep -RIn --exclude-dir='.git' 'picoCTF' .
```

Notes:
- Use the find command to locate files whose names contain 'picoCTF'.
- Use grep -RIn to search contents recursively (shows file:line:match).
- If you need to search inside binaries too, see the Strings section below.

---

## 4. Strings (find readable text in binaries)
```bash
strings <file>
```

Examples:
```bash
strings image.png | grep picoCTF
strings binaryfile | grep -i flag
```
---

## 5. Metadata

### ExifTool
```bash
exiftool <file>
```
Example:
```bash
exiftool image.png
```

---

## 6. Steganography / File Extraction

### Check embedded data
```bash
steghide info -sf <file> -p <password>
```

### Extract embedded data
```bash
steghide extract -sf <file> -p <password>
```
Example:
```bash
steghide info -sf target.jpg
steghide extract -sf target.jpg -p pAzzword
```

---

## 7. Text Transformation

### tr
The tr command translates or deletes characters from input text streams.

#### ROT13 example
```bash
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

#### Convert lowercase to uppercase
```bash
echo "hello" | tr 'a-z' 'A-Z'
```

#### Remove digits
```bash
echo "abc123" | tr -d '0-9'
```

Usage:
```bash
tr <set1> <set2> — replaces each character in <set1> with the corresponding character in <set2>.
```
