def base64_encode(data):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    if isinstance(data, str):
        data = data.encode('utf-8')

    print("1. Convert string to binary")
    bit_string = ''.join(format(byte, '08b') for byte in data)
    print(bit_string)
    print("2. Divided into 6 bits each")
    padded_length = len(bit_string) + (6 - len(bit_string) % 6) % 6
    bit_string = bit_string.ljust(padded_length, '0')
    print(bit_string)
    print("3. Converted to text by conversion table")
    encoded_string = ''
    for i in range(0, len(bit_string), 6):
        index = int(bit_string[i:i+6], 2)
        encoded_string += base64_chars[index]
    print(encoded_string)
    print("4. Add padding as needed")
    padding_length = -len(data) % 3
    encoded_string += '=' * padding_length
    print(encoded_string)
    return encoded_string

def main():
    base64_chars = input("Enter text:")
    print("base64 encode", base64_encode(base64_chars))

if __name__ == "__main__":
    main()