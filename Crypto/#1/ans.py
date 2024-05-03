import base64
from Crypto.Util.number import *


def decrypt( text, original, decode ):
  result = ''
  for letter in text:
    index = original.index( letter )
    result += decode[index]
  return result

def main():
  #1
  # ASCII
  ascii_bytes = [87, 101, 108, 99, 111, 109, 101]
  ascii_string = ''.join(chr(b) for b in ascii_bytes)

  # HEX
  hex_string = '5F746F5F437279'
  hex_decoded_string = bytes.fromhex(hex_string).decode('utf-8')

  # BASE64
  base64_string = 'cHRvZ3JhcGh5X3dvcg=='
  base64_decoded_string = base64.b64decode(base64_string).decode('utf-8')

  # Bytes
  byte_string = 119177308348705
  bytes_decoded_string = long_to_bytes(byte_string).decode('utf-8')

  print("CSL{" + ascii_string + hex_decoded_string + base64_decoded_string + bytes_decoded_string + "}")

  #2
  plain_alphabet  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.'
  cipher_alphabet = 'zyxwvutsrqponmlkjihgfedcba,.ZYXWVUTSRQPONMLKJIHGFEDCBA'

  cipher_text = "VivzgVivzgAAAJrnkovJfyhgrgfgrlmZrksviThVllwAAAA"
  decode_text = decrypt( cipher_text, cipher_alphabet, plain_alphabet )
  print("CSL{" + decode_text + "}" )

if __name__ == "__main__":
    main()