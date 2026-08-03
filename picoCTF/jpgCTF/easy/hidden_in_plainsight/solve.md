# Hidden in Plainsight

**Link**: https://play.picoctf.org/practice/challenge/524

**Difficulty**: easy

## Description

You're given a seemingly ordinary JPG image. Something is tucked away out of sight
inside the file. Your task is to discover the hidden payload and extract the flag.

## Resources

- **img.jpg**: the image with an embedded, password-protected file
- **flag.txt**: the extracted flag (produced during the solve)

## How to solve

The trick is two-layered: the metadata tells you **which tool and password** to use,
and the actual flag is embedded with `steghide`.

1. **Read the metadata:**

       exiftool img.jpg

   The `Comment` field is Base64:

       Comment : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9

2. **Decode the comment** — it points at `steghide` and gives a second Base64 blob:

       echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d      # -> steghide:cEF6endvcmQ=

3. **Decode that inner part** to get the steghide password:

       echo 'cEF6endvcmQ=' | base64 -d                       # -> pAzzword

4. **Extract with steghide** using password `pAzzword`:

       steghide info    img.jpg -p pAzzword      # shows embedded flag.txt (34 bytes)
       steghide extract -sf img.jpg -p pAzzword  # writes flag.txt
       cat flag.txt

## Flag

    picoCTF{h1dd3n_1n_1m4g3_871ba555}
