import gmpy2
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def enc(m, n, e):
    return pow(m, e, n)

def dec(c, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = int(gmpy2.invert(e, phi))
    return pow(c, d, n)

n = 97139961312384239075080721131188244842051515305572003521287545456189235939577
e = 65537
c = 50826727040874016806840751525243675163767614205602835883600078854382143980528

p = 299681192390656691733849646142066664329
q = 324144336644773773047359441106332937713

m = b"CSL24{use_factordb}"
m_int = bytes_to_long(m)

c = enc(m_int, n, e)
print(f"n: {n},\ne: {e},\nEncrypted message: {c}")

decrypted_m_int = dec(c, p, q, e)
decrypted_m = long_to_bytes(decrypted_m_int)
print(f"Decrypted message: {decrypted_m.decode()}")
