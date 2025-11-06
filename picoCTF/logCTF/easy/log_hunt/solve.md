# Log Hunt

**Link**: https://play.picoctf.org/practice/challenge/527

**Difficulty**: easy

## Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?
Download the logs and figure out the full flag from the fragments.

## Resources

**server.log**: The log of the server

## How to solve

Start by searching the log for anything already containing the `picoCTF` prefix:

    grep "picoCTF" server.log

The output shows several repeated fragments:

    [1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:04:29] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:04:37] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:19:23] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:19:29] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:19:32] INFO FLAGPART: picoCTF{us3_

Each partial flag appears next to the tag `FLAGPART`, so extract all lines containing it:

    grep "FLAGPART" server.log

This reveals all parts of the flag appearing throughout the log:

    [1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
    [1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
    [1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
    [1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
    [1990-08-09 10:10:58] INFO FLAGPART: cedfa5fb}
    [1990-08-09 10:11:06] INFO FLAGPART: cedfa5fb}
    [1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:04:29] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:04:37] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 11:09:16] INFO FLAGPART: y0urlinux_
    [1990-08-09 11:09:19] INFO FLAGPART: y0urlinux_
    [1990-08-09 11:12:40] INFO FLAGPART: sk1lls_
    [1990-08-09 11:12:45] INFO FLAGPART: sk1lls_
    [1990-08-09 11:16:58] INFO FLAGPART: cedfa5fb}
    [1990-08-09 11:16:59] INFO FLAGPART: cedfa5fb}
    [1990-08-09 11:17:00] INFO FLAGPART: cedfa5fb}
    [1990-08-09 12:19:23] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:19:29] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:19:32] INFO FLAGPART: picoCTF{us3_
    [1990-08-09 12:23:43] INFO FLAGPART: y0urlinux_
    [1990-08-09 12:23:45] INFO FLAGPART: y0urlinux_
    [1990-08-09 12:23:53] INFO FLAGPART: y0urlinux_
    [1990-08-09 12:25:32] INFO FLAGPART: sk1lls_
    [1990-08-09 12:28:45] INFO FLAGPART: cedfa5fb}
    [1990-08-09 12:28:49] INFO FLAGPART: cedfa5fb}
    [1990-08-09 12:28:52] INFO FLAGPART: cedfa5fb}

From these repeated segments, the full flag can be reconstructed in order:

    picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
