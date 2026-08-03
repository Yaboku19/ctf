# Log Hunt

**Link**: https://play.picoctf.org/practice/challenge/527

**Difficulty**: easy

## Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are
scattered and sometimes repeated. Can you reconstruct the original flag?

## Resources

- **server.log**: the server log containing the scattered flag fragments

## How to solve

1. **Find the marker.** Grepping for the flag prefix shows the pieces are tagged
   `FLAGPART`:

       grep "picoCTF" server.log

2. **Pull every fragment** using that tag:

       grep "FLAGPART" server.log

   The log repeats each of four fragments several times, but the **timestamps** give
   the correct order within each run:

       [10:00:10] FLAGPART: picoCTF{us3_
       [10:02:55] FLAGPART: y0urlinux_
       [10:05:54] FLAGPART: sk1lls_
       [10:10:54] FLAGPART: cedfa5fb}

3. **Reconstruct in timestamp order**, deduplicating the repeats:

   `picoCTF{us3_` + `y0urlinux_` + `sk1lls_` + `cedfa5fb}`

> One-liner to strip the prefixes and stitch unique parts in order:
>
>     grep -oP 'FLAGPART: \K.*' server.log | awk '!seen[$0]++' | tr -d '\n'; echo

## Flag

    picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
