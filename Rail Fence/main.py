def rail_fence_cipher(plaintext, rails):
    fence = [[''] * len(plaintext) for _ in range(rails)]
    rail, direction = 0, 1

    for char in plaintext:
        fence[rail][fence[rail].index('')] = char
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction = -direction

    ciphertext = ''.join(''.join(row) for row in fence)
    return ciphertext


def rail_fence_decipher(ciphertext, rails):
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    rail, direction = 0, 1

    for i in range(len(ciphertext)):
        fence[rail][fence[rail].index('')] = '*'
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction = -direction

    index = 0
    for rail in fence:
        for i in range(len(rail)):
            if rail[i] == '*':
                rail[i] = ciphertext[index]
                index += 1

    rail, direction = 0, 1
    plaintext = ''
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][0]
        rail += direction
        fence[rail].pop(0)

        if rail == rails - 1 or rail == 0:
            direction = -direction

    return plaintext
