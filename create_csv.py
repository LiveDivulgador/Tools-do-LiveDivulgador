# Se tivermos o dotenv instalado importamos e setamos
try:
	from dotenv import load_dotenv
	load_dotenv()

except:
	pass


import pandas as pd
import requests
import os


client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")


def getOAuth():
	# Get Oauth Token
	url = "https://id.twitch.tv/oauth2/token"
	param = {
		"client_id": client_id,
		"client_secret": client_secret,
		"grant_type": "client_credentials"
	}

	r = requests.post(url, data=param)

	access_token = r.json()["access_token"]
	header = {"Client-ID": client_id, "Authorization":"Bearer "+ access_token}

	return access_token, header



def getStreamerId(streamer, header):

	# Get streamer's id
	url = "https://api.twitch.tv/helix/users"
	param = {"login": streamer}

	r = requests.get(url, params=param, headers=header).json()
	

	return r["data"][0]



def createCSV():
	""" Com o CSV do bot do twitter cria um novo com as infos para o site """
	
	access_token, header = getOAuth()
	
	df = pd.read_csv("streamers.csv")

	df_new = pd.DataFrame([], columns=["Id", "Nome", "Twitch", "Descr", "Avatar"])

	print("ENTER")
	for streamer in df.loc[:, "Nome"].values:
		streamer_data = getStreamerId(streamer, header)

		if streamer_data["description"] == "":
			streamer_data["description"] = "Descrição Indisponível"

		df_new = df_new.append({
			"Id": streamer_data["id"],
			"Nome": streamer_data["display_name"],
			"Twitch": "https://www.twitch.tv/"+streamer_data["login"],
			"Descr": streamer_data["description"],
			"Avatar": streamer_data["profile_image_url"]
		}, ignore_index=True)


	df_new.to_csv("streamers_new.csv", index=False)

	print("DONE")



if __name__ == "__main__":
	# Criar o novo CSV
	createCSV()