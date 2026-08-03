# Password Profiler

**Link**: https://play.picoctf.org/practice/challenge/712

**Difficulty**: easy

## Description

We intercepted a suspicious file from a system, but instead of the password itself,
it only contains its SHA-1 hash. Using OSINT techniques, you are provided with
personal details about the target. Your task is to leverage this information to
generate a custom password list and recover the original password by matching its
hash.

## Resources

- **userinfo.txt**: the target's personal details (OSINT)
- **hash.txt**: the SHA-1 hash to crack (`968c2349040273dd57dc4be7e238c5ac200ceac5`)
- **check_password.py**: tests every line of `passwords.txt` against the hash
- **passwords.txt**: the CUPP-generated wordlist (produced during the solve)

## How to solve

1. **Read the hint in `check_password.py`:**

       WORDLIST_FILE = "passwords.txt"   # wordlist that was generated using CUPP

   So the intended path is to build a **targeted** wordlist with
   [CUPP](https://github.com/Mebus/cupp) from the victim's personal info rather
   than brute-forcing a generic list.

2. **Feed CUPP the details from `userinfo.txt`:**

       First Name:     Alice
       Surname:        Johnson
       Nickname:       AJ
       Birthdate:      15-07-1990
       Partner's Name: Bob
       Child's Name:   Charlie

   Run the interactive profiler and answer each prompt with the values above:

       cupp -i

   It writes a file like `alice.txt`. Rename/copy it to `passwords.txt`:

       cp alice.txt passwords.txt

3. **Crack the hash** — `check_password.py` SHA-1s each candidate and compares it
   to `hash.txt`, printing the match already wrapped as the flag:

       python3 check_password.py

   Output:

       Password found: picoCTF{Aj_15901990}

   (The winning password is `Aj_15901990` — nickname + reversed/segmented
   birth-year digits, exactly the kind of mutation CUPP generates.)

## Flag

    picoCTF{Aj_15901990}
