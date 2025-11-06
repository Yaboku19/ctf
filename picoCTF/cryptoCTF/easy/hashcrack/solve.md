# Hashcrack

**Link**: https://play.picoctf.org/practice/challenge/475

**Difficulty**: easy

## Description

A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

## Resources

## How to solve

Connect to the server with the command

    nc verbal-sleep.picoctf.net <port>

And the output will be a series of three different hashes

    Welcome!! Looking For the Secret?
    We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
    Enter the password for identified hash: 

For this you can use different hash crack tools like [crackstation](https://crackstation.net)

The correct passwords are

    password123
    letmein
    qwerty098

Then you will get the flag

    picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}

