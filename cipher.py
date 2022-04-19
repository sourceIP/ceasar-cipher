def cipher (text, shift):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        
    return result

text = 'Hello World'
shift = 13
print('Encrypted Word: ' + cipher(text, shift))