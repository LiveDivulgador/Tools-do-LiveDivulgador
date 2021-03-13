# Se tivermos o dotenv instalado importamos e setamos
try:
	from dotenv import load_dotenv
	load_dotenv()
except:
	pass


from tweepy import OAuthHandler, API
import tweepy
import os
import sys
import threading
import pandas as pd


MSG = f"""Coloque sua mensagem aqui"""


def twitter_OAuth(streamer_type):
	""" Função que faz OAuth na conta correta"""

	CONSUMER_KEY = os.environ["CONSUMER_KEY_C"]
	CONSUMER_SECRET = os.environ["CONSUMER_SECRET_C"]
	ACCESS_TOKEN = os.environ["ACCESS_TOKEN_C"]
	ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET_C"]

	if streamer_type == "art":
		CONSUMER_KEY = os.environ["CONSUMER_KEY_A"]
		CONSUMER_SECRET = os.environ["CONSUMER_SECRET_A"]
		ACCESS_TOKEN = os.environ["ACCESS_TOKEN_A"]
		ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET_A"]

	try:
		auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.secure = True
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	except BaseException as e:
		print("Error in dm_twitter.py", e)
		sys.exit(1)

	return api


def main():
    df = pd.read_csv("streamers_mod.csv", usecols=["Twitter", "Tipo"])

    # Api para os coders
    api_code = twitter_OAuth("code")

    # Api para os artistas
    api_art = twitter_OAuth("art")


    for tt, tp in zip(df["Twitter"], df["Tipo"]):
        
        # Se tem twitter
        if not isinstance(tt, float):
            
            # Escolher conta para enviar a DM
            api = api_code

            if tp == "art":
                api = api_art
            
            # Obter o id do user
            idt = api.get_user(tt).id

            try:
                api.send_direct_message(idt, MSG)
                print("Mensagem enviada a: " + tt)

            except tweepy.error.TweepError as e:
                print("Algo deu errado com: " + tt)
                print(e)
            
            #api.send_direct_message(idt, MSG)
        
        else:
            print("Não tem Twitter")

def threaded(job):

    # Função para correr a main em modo threading
    thread = threading.Thread(target=job)
    thread.start()

    # Esperar pela thread terminar
    thread.join()

if __name__ == "__main__":
    threaded(main)