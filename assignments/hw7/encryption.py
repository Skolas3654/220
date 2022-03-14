def encode(message, key):
    encoded_message = []

    for i in message:
        encoder = chr(ord(i) + key)
        #encoder = chr(encoder)
        encoded_message.append(encoder)

    encoded_message.remove(encoded_message[-1])
    encoded_message = "".join(encoded_message)
    return  encoded_message

def encoder_better(string, key):
    key = key * 26
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(k[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))