
# Chat criptata con Python e gnupg

Questo script permette di scambiare messaggi cifrati con un'altra persona usando la crittografia a chiave pubblica. Il modulo gnupg viene usato per generare, esportare, importare, cifrare e decifrare le chiavi. Il modulo socket viene usato per creare una connessione di rete tra le due persone.

## Requisiti

Per eseguire questo script, devi avere installato Python 3 e il modulo gnupg. Puoi installare il modulo gnupg con il comando:

`pip install python-gnupg`

## Uso

Per avviare lo script, salva il file con estensione .py, ad esempio chatgpg.py, e rendilo eseguibile con il comando:

`chmod a+x chatgpg.py`

Poi esegui il comando:

`./chatgpg.py`

Se sei la persona che ha aperto la porta 1234, aspetta che l'altra persona si connetta a te.

Se sei la persona che si vuole connettere, modifica lo script e sostituisci la riga `sock.bind(('', 1234))` con `sock.connect((<indirizzo IP>, 1234))`, dove <indirizzo IP> è l'indirizzo IP della persona che ha aperto la porta.

Quando la connessione è stabilita, vedrai il messaggio "Connesso con" seguito dall'indirizzo dell'altra persona. Poi potrai scrivere un messaggio da inviare all'altra persona e premere Invio. Il messaggio verrà cifrato con la chiave pubblica dell'altra persona e inviato. Riceverai il messaggio cifrato dall'altra persona e lo vedrai decifrato. Per terminare la chat, scrivi "quit" e premi Invio.
