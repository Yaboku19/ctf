# Shared Secrets

**Link**: https://play.picoctf.org/practice/challenge/715

**Difficulty**: easy

## Description

A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?

## Resources
**message.txt**: all the informations of the encrypted message.

**encription.py**: script with how they encoded the flag.

## How to solve

From the python script we can see that the flag is xored with a shared variable

    enc = bytes([x ^ (shared % 256) for x in flag])

So if we can retrieve shared than we will be easy able to get the flag. Shared from the code is created as follow

    shared = pow(A, b, p)

And A, b, and p can be found in the message.txt file, as well as the enc value. So by running

    flag = bytes([x ^ (shared % 256) for x in bytes.fromhex(enc)])

The flag can be easly retrieved.

