# Caesar Cipher

A simple Python tool to encrypt, decrypt, and brute-force crack Caesar ciphers.

## Usage

```bash
python caesar.py
```

```
1. Encrypt
2. Decrypt
3. Crack
0. Exit
```

- **Encrypt** – enter a message and a shift amount
- **Decrypt** – enter an encrypted message and the shift used
- **Crack** – enter an encrypted message and see it decrypted with all 25 possible shifts

Upper and lower case are preserved, and anything that isn't a letter (spaces, numbers, punctuation) is left unchanged.

## Example

```
Enter message: Hello, World!
Position shift: 3

Encrypted: Khoor, Zruog!
```

## Files

| File | Purpose |
|------|---------|
| `caesar.py` | Menu / entry point |
| `cypher.py` | `encrypt()` and `decrypt()` functions |
| `cracker.py` | Brute-force `crack()` function |

## Requirements

Python 3.6+ — no external packages.

## License

[MIT](LICENSE)
