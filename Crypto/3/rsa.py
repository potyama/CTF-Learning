from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def enc(m, n, e):
    return pow(m, e, n)

def dec(c, p, q, e):
    n = p * q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    return pow(c, d, n)

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537

m = b"CSL24{RSA_is_very_important}"
m_int = bytes_to_long(m)

c = enc(m_int, n, e)
print(f"p:{p},\nq:{q},\ne: {e},\nEncrypted message: {c}")

decrypted_m_int = dec(c, p, q, e)
decrypted_m = long_to_bytes(decrypted_m_int)
print(f"Decrypted message: {decrypted_m.decode()}")
