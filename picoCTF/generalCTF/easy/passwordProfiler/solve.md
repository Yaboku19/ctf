# Password Profiler

**Link**: https://play.picoctf.org/practice/challenge/712

**Difficulty**: easy

## Description

We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.

## Resources

**userinfo**: Contains the personal details. 

**hash**: Contains the SHA-1 hash of the password.

**check_password.py**: Script to test passwords against the hash.

## How to solve

There is an hint in the `check_password.py` script

    # wordlist that was generated using CUPP

That hint us to use cupp and create a passwords.txt file with all the possible string related to the user using its personal informations. Use it by running

    cupp -i

You will receive a questionaire and you will have to complete it with the informations of the user. Once finished it will create a file and you will have to use it for the ptyhon script.

