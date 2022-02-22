import gnupg

gpg = gnupg.GPG(gnupghome='/root/.gnupg', verbose=True)

input_data = gpg.gen_key_input(
    name_email='felipebedoya@protonmail.com',
    passphrase='my passphrase')
key = gpg.gen_key(input_data)


def decrypt(data, passphrase):
    encrypted_string = str(data)
    decrypted_data = gpg.decrypt(encrypted_string, passphrase=passphrase)

    print('ok: ', decrypted_data.ok)
    print('status: ', decrypted_data.status)
    print('stderr: ', decrypted_data.stderr)
    print('decrypted string: ', decrypted_data.data)
    return decrypted_data.data
