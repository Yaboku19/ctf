# No FA

**Link**: https://play.picoctf.org/practice/challenge/765

**Difficulty**: medium

## Description

Seems like some data has been leaked! Can you get the flag?

## Resources

- **app.py**: the Flask backend
- **users.db**: the leaked SQLite user database
- **script.py**: decodes a Flask session cookie

## Key observations (from app.py)

- Only the **admin** user ever receives the flag:

      if session.get('username') == 'admin':
          flag = os.getenv('FLAG')

- Passwords are unsalted **SHA-256** (`hashlib.sha256(password).hexdigest()`), so
  they're crackable from the leaked DB.
- Admin (and only admin) has `two_fa = 1`, so logging in as admin triggers a
  one-time password step.
- **The bug:** the OTP is stored in the Flask `session`, and Flask's default session
  is a *signed but not encrypted* cookie. The client can read every value in it —
  including `otp_secret`:

      session['otp_secret']    = otp          # ends up readable in your cookie!
      session['otp_timestamp'] = time.time()

## How to solve

1. **Read the leaked DB** and find admin's hash:

       sqlite3 users.db 'SELECT username,email,password,two_fa FROM users;'

   Admin row:

       admin | iamadmin@nfs.com | c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67 | 1

2. **Crack the unsalted SHA-256** (e.g. [CrackStation](https://crackstation.net),
   or `hashcat -m 1400`):

       apple@123

3. **Log in** as `admin` / `apple@123`. Because 2FA is on, you're redirected to the
   OTP page — but the OTP was just written into your session cookie.

4. **Read the OTP out of the session cookie.** Copy the `session` cookie from your
   browser (DevTools → Application → Cookies) and decode it with `script.py`
   (Flask session = base64 parts joined by `.`, sometimes zlib-compressed):

       python3 script.py
       # {"logged":"false","otp_secret":"8914","otp_timestamp":..., "username":"admin"}

5. **Submit that `otp_secret`** on the 2FA page within the 120-second window. The
   session flips to `logged = 'true'` and the home page reveals the flag.

## Flag

    picoCTF{n0_r4t3_n0_4uth_2b765193}
