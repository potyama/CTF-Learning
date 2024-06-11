from urllib.parse import urlparse, quote, urlunparse

def url_encode(string_utf8, safe='/'):
    print("1. Encoded in UTF-8")
    string_bytes = string_utf8.encode('utf-8')
    print(string_bytes)
    print("2. Convert to hexadecimal with '%' prefix")
    url_encode = []
    for b in string_bytes:
        char = chr(b)
        if char in safe or char.isascii():
            url_encode.append(char)
        else:
            url_encode.append('%{:02x}'.format(b))
    print(url_encode)
    return ''.join(url_encode)


    return encoded_string

def encode_url_path(url):
    parsed_url = urlparse(url)
    encoded_path = url_encode(parsed_url.path)
    new_url = parsed_url._replace(path=encoded_path)
    return urlunparse(new_url)


def main():
    choice = input("Choose an operation:\n1. URL Encode characters\n2. Encode URL path\nEnter 1 or 2: ")

    if choice == '1':
        characters_encode = input("Enter the characters to encode: ")
        print("Encoded characters:", url_encode(characters_encode))
    elif choice == '2':
        url = input("Enter the URL to encode: ")
        print("Encoded URL:", encode_url_path(url))
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()