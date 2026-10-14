from cypher import decrypt

def crack(message):
    results = []

    for shift in range(1, 26):
        decrypted = decrypt(message, shift)
        results.append((shift, decrypted))

    return results