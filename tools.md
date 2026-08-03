# Tools

A quick reference of useful tools and commands for CTF challenges.

## Contents

1. [Connection](#1-connection) — `ssh`, `nc`
2. [Web / HTTP](#2-web--http) — `curl`
3. [Encoding & Decoding](#3-encoding--decoding) — `base64`, `base32`, `xxd`
4. [Raw Bytes & File Repair](#4-raw-bytes--file-repair) — `hexdump`, `dd`
5. [Searching Files](#5-searching-files) — `find`, `grep`, `strings`
6. [Metadata](#6-metadata) — `exiftool`, `pdfinfo`
7. [Steganography](#7-steganography) — `steghide`, `zsteg`
8. [Archives & Disk Images](#8-archives--disk-images) — `gunzip`
9. [Databases](#9-databases) — `sqlite3`
10. [Cryptography](#10-cryptography) — `openssl`, hash cracking
11. [Text Transformation](#11-text-transformation) — `tr`
12. [Password Wordlists](#12-password-wordlists) — `cupp`
13. [Network Shares](#13-network-shares) — `smbclient`
14. [Version Control](#14-version-control) — `git`
15. [Binary Exploitation](#15-binary-exploitation) — `pwntools`, `gdb`
16. [Blockchain / Ethereum](#16-blockchain--ethereum) — `cast` (Foundry), JSON-RPC

---

## 1. Connection

### SSH
```bash
ssh -p <port> <user>@<domain>
```

### Netcat
```bash
nc <domain> <port>
```

---

## 2. Web / HTTP

### Curl
```bash
# simple GET
curl -sS http://example.com/

# save headers + body
curl -sS -D headers.txt http://example.com/ -o body.html

# POST JSON
curl -s -X POST http://example.com/api -H "Content-Type: application/json" -d '{"k":"v"}'

# add/modify header
curl -s -H "X-Dev-Access: yes" http://example.com/

# save/reuse cookies
curl -s -c cookies.txt -X POST http://example.com/login -d "u=a&p=b"
curl -s -D - -c cookies.txt 'site'
curl -s -b cookies.txt http://example.com/dashboard

# verbose / follow redirects
curl -v -L http://example.com/

# ignore TLS (dev/CTF)
curl -k https://example.com/

# extract JSON field (requires jq)
curl -s http://example.com/api | jq -r '.flag // .message // "No flag"'
```

---

## 3. Encoding & Decoding

### Base64
```bash
echo 'c3RyaW5n' | base64 -d
```

### Base32
```bash
echo 'ONXW4===' | base32 -d
```

### Hexadecimal
Convert a hex string back to raw bytes, then read it:
```bash
xxd -r -p <in.txt> > <out.bin>
strings <out.bin>
cat <out.bin>
```
Example:
```bash
echo '7069636f' > hex.txt && xxd -r -p hex.txt > out.bin && strings out.bin
```

---

## 4. Raw Bytes & File Repair

### hexdump
Display the raw bytes of a file in hex + ASCII (great for checking magic bytes).
```bash
# first 16 bytes in canonical hex+ASCII format
hexdump -C -n 16 file

# full hex dump
hexdump -C file

# hex only, no ASCII
hexdump -v -e '1/1 "%02x "' file
```

### dd
Copy, extract, or overwrite specific bytes in a file.
```bash
# overwrite the first 2 bytes (e.g. fix a JPEG magic to FF D8)
printf "\xFF\xD8" | dd of=file bs=1 count=2 conv=notrunc

# extract a specific byte range
dd if=file of=chunk.bin bs=1 skip=100 count=50

# raw copy
dd if=input.bin of=output.bin
```
Notes:
- `bs=1` → operate byte-by-byte
- `skip=` → number of bytes to skip
- `count=` → number of bytes to read
- `conv=notrunc` → do not truncate the output file (critical when editing headers)

---

## 5. Searching Files

### find — locate files by name (case-insensitive)
```bash
find . -type f -iname '*picoCTF*'
```

### grep — search text inside files recursively (exclude .git)
```bash
grep -RIn --exclude-dir='.git' 'picoCTF' .
```

### strings — find readable text in binaries
```bash
strings <file>
```
Examples:
```bash
strings image.png    | grep picoCTF
strings binaryfile   | grep -i flag
strings disk.dd      | grep -i pico
```

---

## 6. Metadata

### ExifTool — image/media metadata
```bash
exiftool <file>

# dump one field raw (keeps line breaks, decodes to a file, etc.)
exiftool -b -Comment image.jpg
```

### pdfinfo — PDF metadata
```bash
pdfinfo confidential.pdf
```
Tip: interesting fields (Author, Producer, Keywords) often hide Base64.

---

## 7. Steganography

### steghide — hidden data in JPEG/BMP/WAV
```bash
steghide info    -sf <file> -p <password>    # show embedded file
steghide extract -sf <file> -p <password>    # extract it
```
Example:
```bash
steghide extract -sf target.jpg -p pAzzword
```

### zsteg — LSB stego in PNG/BMP
```bash
zsteg <file.png>                 # scan all bit planes / channels
zsteg -E b1,rgba,lsb,xy file.png # extract a specific plane
```

---

## 8. Archives & Disk Images

### gunzip — decompress .gz files
```bash
gunzip disko-1.dd.gz    # produces disko-1.dd
```

---

## 9. Databases

### sqlite3 — read leaked .db files
```bash
sqlite3 users.db '.schema'                 # show table structure
sqlite3 users.db 'SELECT * FROM users;'    # dump a table
```

---

## 10. Cryptography

### openssl — RSA decryption with a recovered key
```bash
openssl pkeyutl -decrypt -inkey private_key.pem -in flag.enc -out flag.dec
cat flag.dec
```
Note: a PEM key with wrong permissions is rejected — `chmod 600 private_key.pem`.

### Hash cracking
Identify the hash by length (MD5 = 32 hex, SHA-1 = 40, SHA-256 = 64), then crack:
- Online: [CrackStation](https://crackstation.net) — good for unsalted, common passwords.
- Local wordlist attack: pair a wordlist with the target hash (see also `cupp`).

---

## 11. Text Transformation

### tr — translate/delete characters
```bash
# ROT13
echo "cvpbPGS{...}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

# lowercase -> uppercase
echo "hello" | tr 'a-z' 'A-Z'

# remove digits
echo "abc123" | tr -d '0-9'
```

---

## 12. Password Wordlists

### cupp — generate a targeted wordlist from OSINT
```bash
cupp -i        # interactive: answer with the target's personal details
```
Feed it names, nicknames, birthdates, partner/child names → it outputs a custom
`<name>.txt` you can use as a wordlist for hash cracking.

---

## 13. Network Shares

### smbclient — enumerate and pull files from SMB shares
```bash
# list shares (null session, no password)
smbclient -L //<host> -p <port> -N

# connect to a share
smbclient //<host>/<share> -p <port> -N
```
Inside the `smb: \>` prompt: `ls`, then `get <file>` to download, then `exit`.

---

## 14. Version Control

### git — recover data from a repo's history
```bash
git log                 # commit messages / notes
git log --all --oneline
git reflog              # find lost commits
git stash list          # stashed changes
git show <hash>         # inspect a specific commit
```

---

## 15. Binary Exploitation

### pwntools — Python exploitation framework
```python
from pwn import *

context.binary = ELF('./vuln')       # sets arch/bits/endianness automatically
elf = context.binary

io = process('./vuln')               # local
# io = remote('host.picoctf.net', 1234)   # remote

io.recvuntil(b'prompt: ')
io.sendline(b'payload')
print(io.recvall().decode())

# useful helpers
elf.symbols['win']                   # symbol address (defeats PIE with a leak)
```

### gdb — debugger (via pwntools)
```python
io = gdb.debug('./vuln', gdbscript='''
b main
continue
''')
```
Convention: run the exploit as `python3 solver.py` (local), `GDB` (debug), or
`REMOTE` (remote host/port).

---

## 16. Blockchain / Ethereum

For Solidity/Ethereum challenges you interact with a smart contract over the
network. Two pieces: **`cast`** (Foundry) to encode/sign, and the node's
**JSON-RPC** to read/broadcast.

### Install Foundry (gives you `cast`, `forge`, `anvil`)
```bash
curl -L https://foundry.paradigm.xyz | bash
source ~/.bashrc
foundryup                 # downloads the binaries
cast --version
```

### What cast does
- **Offline (local, no network):**
  - `cast calldata "balances(address)" 0xYou` → build the call `data` (4-byte
    selector + encoded args).
  - `cast mktx <to> "deposit(uint256)" 123 --private-key 0x.. --chain <id> --nonce <n> --gas-limit 120000 --gas-price 2000000000 --legacy`
    → build **and sign** a transaction, prints the raw hex. (curl can't sign — this
    is the step that needs cast.)
  - `cast abi-decode "getFlag()(string)" 0x..`, `cast --to-ascii`, `cast to-dec`,
    `cast keccak` → decode/convert.
- **Network (JSON-RPC):**
  - `cast call <addr> "sig()(type)" args --rpc-url <RPC>` → read a contract.
  - `cast send <addr> "sig()" args --private-key 0x.. --rpc-url <RPC>` → sign+send.
  - `cast chain-id / balance / nonce / block --rpc-url <RPC>` → query state.

### Reading a contract via raw JSON-RPC (curl)
Useful when the node rejects cast's request format (see the note below). A read is
`eth_call` with a single `data` field:
```bash
RPC=http://host:port
BANK=0xContract
curl -s -X POST $RPC -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"'"$BANK"'","data":"'"$(cast calldata "balances(address)" 0xYou)"'"},"latest"]}'
```
Other handy methods: `eth_getBalance` (ETH for gas), `eth_getTransactionCount`
(nonce), `eth_gasPrice`, `eth_chainId`, `eth_sendRawTransaction` (broadcast a signed
tx), `eth_getTransactionReceipt`.

### Sending a signed transaction via curl
`eth_sendRawTransaction` takes one signed hex string, so it works even on picky
nodes:
```bash
RAW=$(cast mktx $BANK "deposit(uint256)" 123 \
  --private-key $PK --chain 31337 --nonce 0 \
  --gas-limit 120000 --gas-price 2000000000 --legacy)

curl -s -X POST $RPC -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_sendRawTransaction","params":["'"$RAW"'"]}'
```

### Gotcha: `duplicate field data`
Some older challenge nodes reject `cast call` / `cast send` with:
```
error -32602: duplicate field `data`
```
Modern cast sends both `input` and `data` in every RPC request and the old node
refuses it. Downgrading cast does **not** fix it. Workaround: use cast only for the
**offline** parts (`cast calldata`, `cast mktx`) and do the **network** parts with
curl (`eth_call`, `eth_sendRawTransaction`) as shown above.

Notes:
- `--gas-price` is **decimal wei** (e.g. `2000000000` = 2 gwei), not hex.
- `--nonce` increments per transaction from the same account: 0, 1, 2, …
- Contract read results for `string`/`bytes` are ABI-encoded (offset + length +
  data) — decode with `cast abi-decode`.
