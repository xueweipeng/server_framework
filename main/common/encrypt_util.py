import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self):
        self.bs = 16
        self.mode = AES.MODE_ECB

    def _pad(self, s):
        if isinstance(s, str):
            s = s.encode(encoding='utf-8')
        retain = (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        if isinstance(retain, str):
            retain = retain.encode(encoding='utf-8')
        return s + retain

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, key, message):
        message = self._pad(message)
        cipher = AES.new(key, self.mode)
        encrypted = cipher.encrypt(message)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, key, message):
        decoded = base64.b64decode(message)
        cipher = AES.new(key, self.mode)
        decrypted = cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')


if __name__ == '__main__':
    key = '`?.F(fHbN6XK|j!t'
    cipher = AESCipher()

    plaintext = '542#1504891440039'
    encrypted = cipher.encrypt(key, plaintext)
    print('Encrypted: %s' % encrypted)
    ciphertext = '5bgJqIqFuT8ACuvT1dz2Bj5kx9ZAIkODHWRzuLlfYV0='
    assert encrypted == ciphertext

    decrypted = cipher.decrypt(key, encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == plaintext
