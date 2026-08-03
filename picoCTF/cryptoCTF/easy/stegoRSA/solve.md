# StegoRSA

**Link**: https://play.picoctf.org/practice/challenge/719

**Difficulty**: easy

## Description

A message has been encrypted using RSA. The public key is gone… but someone might
have been careless with the private key. Can you recover it and decrypt the message?

## Resources

- **flag.enc**: the RSA-encrypted flag
- **image.jpg**: an image with the private key hidden in its metadata
- **private_key.pem**: the recovered key (produced during the solve)
- **file.dec**: the decrypted flag (produced during the solve)

## How to solve

1. **Inspect the image metadata.** The private key is stashed in the JPEG's
   `Comment` field as a hex string:

       exiftool image.jpg

   The `Comment` value is a long hex blob. Decoding its start (`2d2d2d2d2d…` =
   `-----`) shows it is a PEM private key:

       -----BEGIN PRIVATE KEY-----
       ...
       -----END PRIVATE KEY-----

2. **Rebuild the PEM file** from the hex. Copy the hex string into a variable (or
   pipe the `exiftool -b -Comment` output) and convert it back to bytes, then lock
   down its permissions so OpenSSL will accept it:

       exiftool -b -Comment image.jpg | xxd -r -p > private_key.pem
       chmod 600 private_key.pem

   (Equivalently: `echo <hexstring> | xxd -r -p > private_key.pem`.)

3. **Decrypt the ciphertext** with the recovered private key:

       openssl pkeyutl -decrypt -inkey private_key.pem -in flag.enc -out file.dec

4. **Read the flag:**

       cat file.dec

## Flag

    picoCTF{rs4_k3y_1n_1mg_26586619}
