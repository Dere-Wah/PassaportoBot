# PassaportoBot
Un bot che controlla ogni minuto se c'è disponibilità per fare il passaporto sul sito della polizia e ti notifica su discord.

## Funzionamento
Il bot invia una richiesta API periodicamente all'endpoint https://passaportonline.poliziadistato.it/cittadino/a/rc/v1/appuntamento/elenca-sede-prima-disponibilita, che viene usato normalmente per mostrare le sedi disponibili quando si prova a fare richiesta manualmente.

Una volta trovata disponibilità viene inviato un messaggio tramite webhook su discord, notificando @everyone. Poiché notifica everyone consiglio di impostare il webhook in un canale privato.

![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/ab18a8d4-20c8-40da-998f-43067b424907)

![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/bd7e8ed0-8279-468c-afc2-fe8511f4a3a3)

## Setup
Librerie necessarie:
- requests
- discord-webhook (https://pypi.org/project/discord-webhook/)
- datetime
- time

Parametri da impostare:
- provincia: il codice della provincia in cui state cercando disponibilità. Ad esempio BG per Bergamo o MI per Milano.
- webhook_url: l'URL del webhook di discord a cui inviare le notifiche. Per creare un webhook:
      .1 Vai sul server discord contenente la chat in cui desideri ricevere le notifiche. Devi avere i poteri di amministratore per poter creare un webhook.
      .2 Vai nelle impostazioni del server > Integrazioni
      .3 Clicca su Crea Webhook / Visualizza Webhook + Nuovo Webhook
      .4 Una volta creato puoi modificare l'immagine, il nome ed il canale in cui verranno inviate le notifiche. Una volta selezionato il tutto clicca su copia URL webhook.
      .5 Incolla l'URL del webhook nel codice python.
  ![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/dac01d6c-581d-4093-acad-b09fa984ff58)

I parametri sopra sono da impostare soltanto la prima volta. I seguenti qui sotto sono inerenti alla sessione di autenticazione SPID, quindi potresti dover aggiornare questi token periodicamente poiché hanno una scadenza.

spid_cookie & spid_token

Vai al [sito](https://passaportonline.poliziadistato.it/cittadino/a/sc/wizardAppuntamentoCittadino/sceltaComune) per prenotare il passaporto normalmente, e arriva al passo 2. (Quello dove vedi la lista delle sedi disponibili)
![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/03ca6758-10a4-486e-9557-eeae7d934c24)

Premi tasto destro + ispeziona elemento e vai nella sezione Network.
![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/6ad4e387-41ef-4152-b7e5-28d6416b4b93)

Aggiorna la pagina e clicca sulla voce "elenca-sede-prima-disponibilita"
![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/017d8d95-824b-408e-8680-794c1d3ebccc)

Si aprirà una sezione con delle voci come "Headers", "Payload", "Preview", etc. rimani su Headers. Scorri giù fino alla voce "Request Headers", e copia i seguenti valori:

![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/97aabb13-01b1-4cd6-8919-a755152f1f5b)

(sì, tutta sta stringa lunghissima) -> INCOLLA in spid_cookie

![image](https://github.com/Dere-Wah/PassaportoBot/assets/160314410/a06246c6-d81e-4083-afa1-51a2bbc47ddf)
-> INCOLLA in spid_token

Una volta fatto ciò potete eseguire il bot e inizierete a ricevere notifiche ogni volta che vengono trovate disponibilità!




