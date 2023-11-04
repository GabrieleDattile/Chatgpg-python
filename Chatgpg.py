# Importo il modulo gnupg per usare il servizio GPG
import gnupg

# Creo un'istanza di GPG
gpg = gnupg.GPG()

# Genero una coppia di chiavi pubblica e privata per ogni persona
key1 = gpg.gen_key(gpg.gen_key_input(name_email='persona1@example.com'))
key2 = gpg.gen_key(gpg.gen_key_input(name_email='persona2@example.com'))

# Esporto le chiavi pubbliche in formato ASCII
pubkey1 = gpg.export_keys(key1.fingerprint)
pubkey2 = gpg.export_keys(key2.fingerprint)

# Importo le chiavi pubbliche nell'anello delle chiavi di GPG
gpg.import_keys(pubkey1)
gpg.import_keys(pubkey2)

# Definisco una funzione per cifrare un messaggio con la chiave pubblica del destinatario
def encrypt_message(message, recipient):
    return str(gpg.encrypt(message, recipient))

# Definisco una funzione per decifrare un messaggio con la propria chiave privata
def decrypt_message(message, passphrase):
    return str(gpg.decrypt(message, passphrase=passphrase))

# Apro una porta per comunicare con l'altra persona
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 1234))
sock.listen(1)

# Accetto la connessione dall'altra persona
conn, addr = sock.accept()
print('Connesso con', addr)

# Invio la mia chiave pubblica all'altra persona
conn.sendall(pubkey1.encode())

# Ricevo la chiave pubblica dell'altra persona
pubkey2 = conn.recv(1024).decode()
gpg.import_keys(pubkey2)

# Scrivo un messaggio da inviare all'altra persona
message = input('Scrivi un messaggio: ')

# Cifro il messaggio con la chiave pubblica dell'altra persona
encrypted_message = encrypt_message(message, 'persona2@example.com')

# Invio il messaggio cifrato all'altra persona
conn.sendall(encrypted_message.encode())

# Ricevo il messaggio cifrato dall'altra persona
encrypted_message = conn.recv(1024).decode()

# Decifro il messaggio con la mia chiave privata
decrypted_message = decrypt_message(encrypted_message, 'persona1@example.com')

# Stampo il messaggio decifrato
print('Messaggio ricevuto:', decrypted_message)

# Chiudo la connessione
conn.close()
