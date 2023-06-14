def decode_caesar(ciphertext):
    frequency = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
        'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
        'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
        'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
        'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
        'y': 0.01974, 'z': 0.00074
    }

    def calculate_score(text):
        score = sum(frequency.get(char.lower(), 0) for char in text if char.isalpha())
        return score

    def decode_char(char, key):
        if char.isalpha():
            is_uppercase = char.isupper()
            decoded_char = chr((ord(char.lower()) - 97 + key) % 26 + 97)
            return decoded_char.upper() if is_uppercase else decoded_char
        else:
            return char

    max_score = float("-inf")
    decoded = ""

    for key in range(26):
        decoded_text = ''.join(decode_char(char, key) for char in ciphertext)
        score = calculate_score(decoded_text)
        
        if score > max_score:
            max_score = score
            decoded = decoded_text

    return decoded

ciphertext = "	L'p uhdoob orrnlqj iruzdug wr sdvvlqj wklv vhphvwhu, vr sohdvh dffhsw wklv vkruw frgh dqg ohw ph sdvv, Brxu Ghdu Vwxghqw Eduwhn"    
decoded_text = decode_caesar(ciphertext)
print("Decoded text: ", decoded_text)
