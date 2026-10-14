def encrypt(message, shift):
    conv_message = [ord(x) for x in message]
    shift = shift % 26

    shifted = []

    for n in conv_message:
        new_n = n + shift

        if 65 <= n <= 90:
            if new_n > 90:
                new_n = new_n - 26

        elif 97 <= n <= 122:
            if new_n > 122:
                new_n = new_n - 26

        else:
            new_n = n

        shifted.append(new_n)

    encrypted = "".join(chr(n) for n in shifted)

    return(encrypted)


def decrypt(message, shift):
    conv_message = [ord(x) for x in message]
    shift = shift % 26

    shifted = []

    for n in conv_message:
        new_n = n - shift

        if 65 <= n <= 90:
            if new_n < 65:
                new_n = new_n + 26

        elif 97 <= n <= 122:
            if new_n < 97:
                new_n = new_n + 26

        else:
            new_n = n

        shifted.append(new_n)

    decrypted = "".join(chr(n) for n in shifted)

    return(decrypted)
