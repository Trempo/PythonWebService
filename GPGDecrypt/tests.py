from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import requests
import gnupg
import random
import string

from GPGDecrypt.logic import decryptUtil

gpg = gnupg.GPG(gnupghome='/home/felipebedoya/.gnupg', verbose=True)
input_data = gpg.gen_key_input(
    name_email='felipebedoya@protonmail.com',
    passphrase='my passphrase')
key = gpg.gen_key(input_data)


class DecryptTest(TestCase):
    def test_decrypt(self):
        randomEncryption = []
        answer = []
        for i in range(10):
            letters = string.ascii_lowercase
            randomString = ''.join(random.choice(letters) for i in range(10))
            answer.append(randomString)
            unencrypted_string = randomString
            encrypted_data = gpg.encrypt(unencrypted_string, 'felipebedoya@protonmail.com')
            encrypted_string = str(encrypted_data)
            randomEncryption.append(encrypted_string)

        for i in range(10):
            self.assertEqual(decryptUtil.decrypt(randomEncryption[i], "my passphrase").decode('utf-8'), answer[i])

