import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import time

#Per un tutorial su come ottenere questi parametri vedi github:
#https://github.com/Dere-Wah/PassaportoBot
webhook_url = "DISCORD_WEBHOOK"
spid_token = "SPID_TOKEN"
spid_cookie = "SPID_COOKIE"
provincia = "BG"

def webhook_post(elemento, data):
	descrizione = elemento["descrizione"]
	infoUtente = elemento["infoUtente"]
	date_text = data.strftime("%A %d. %B %Y")
	webhook = DiscordWebhook(url=webhook_url)
			
	message_embed = DiscordEmbed(title="NUOVA DISPONIBILITA'", description=f"Il bot ha trovato una nuova disponibilità! In particolare:\n{descrizione}\n\n{date_text}", color='03fc45')
	message_embed.set_footer(text=infoUtente)
	webhook.content = "@everyone NUOVA DISPONIBILITA'\n\nhttps://passaportonline.poliziadistato.it/cittadino/a/sc/wizardAppuntamentoCittadino/sceltaComune"
	webhook.add_embed(message_embed)
	webhook.execute()
	
def webhook_notify(error):
	print(error)
	webhook = DiscordWebhook(url=webhook_url)
	message_embed = DiscordEmbed(title="ERRORE CONTROLLO DISPONIBILITA'", description=f"Probabilmente devi ri-effettuare l'accesso e rimettere i cookie. Dettaglio: {error}", color='fc0303')
	webhook.content = "ERRORE BOT @everyone"
	webhook.add_embed(message_embed)
	

	webhook.execute()


def controlla_disponibili(provincia):
	url = "https://passaportonline.poliziadistato.it/cittadino/a/rc/v1/appuntamento/elenca-sede-prima-disponibilita"

	payload = {
		"disponibilitaNonResidenti": False,
		"minorenne": False,
		"minorenneDodici": False,
		"comune": {
			"objectKey": "975",
			"persistenceStatus": "PERSISTED",
			"id": "975",
			"istatId": None,
			"denominazione": "ASTI SteamDeck",
			"codice": "975",
			"denominazioneEstera": None,
			"provincia": "DW",
			"provinciaQuestura": provincia,
			"new": False,
			"deleted": False
		},
		"pageInfo": {"maxResults": 5},
		"sortInfo": {"sortList": [
				{
					"sortDirection": 0,
					"sortProperty": "primaDisponibilitaResidente"
				}
			]}
	}
	headers = {
		"Accept": "application/json, text/plain, */*",
		"Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
		"Connection": "keep-alive",
		"Content-Type": "application/json",
		"Cookie": spid_cookie,
		"Origin": "https://passaportonline.poliziadistato.it",
		"Sec-Fetch-Site": "same-origin",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
		"X-CSRF-TOKEN": spid_token
	}
	response = requests.request("POST", url, json=payload, headers=headers)
	if(response.ok):
		i = 0
		print(f"--- DISPONIBILITA' A {provincia} ---")
		for sede in response.json()["list"]:
			if(sede["dataPrimaDisponibilitaResidenti"] != None):
				date = datetime.strptime(sede["dataPrimaDisponibilitaResidenti"], "%Y-%m-%dT%XZ")
				print(date.strftime("%A %d. %B %Y"))
				webhook_post(sede, date)
				i += 1
		if(i == 0):
			print("Non ho trovato disponibilità")
	else:
		webhook_notify(response.status_code)
	
	
last_attempt = None

print("PassaportoBot by Dere-Wah: https://github.com/Dere-Wah/PassaportoBot")

while True:
	now = datetime.now()
	if last_attempt != now.minute:
		last_attempt = now.minute
		controlla_disponibili(provincia)
	time.sleep(1)  # Check every minute
	
