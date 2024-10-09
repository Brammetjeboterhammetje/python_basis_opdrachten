import rsa

# Generate public and private keys
publicKey, privateKey = rsa.newkeys(512)

def encrypt_message(message):
    return rsa.encrypt(message.encode(), publicKey)

def decrypt_message(enc_message):
    return rsa.decrypt(enc_message, privateKey).decode()

def main():
    choice = input("Wil je encrypten of decrypten? (e/d): ").lower()
    
    if choice == 'e':
        message = input("Geef de tekst die je wilt encrypten: ")
        enc_message = encrypt_message(message)
        print("Original string: ", message)
        print("Encrypted string: ", enc_message)
    elif choice == 'd':
        enc_message = input("Geef de tekst die je wilt decrypten (in bytes): ")
        try:
            enc_message = bytes.fromhex(enc_message)
            dec_message = decrypt_message(enc_message)
            print("Decrypted string: ", dec_message)
        except ValueError:
            print("Ongeldige invoer. Zorg ervoor dat de versleutelde tekst in hexadecimale vorm is.")
    else:
        print("Ongeldige keuze. Kies 'e' voor encrypten of 'd' voor decrypten.")

if __name__ == "__main__":
    main()