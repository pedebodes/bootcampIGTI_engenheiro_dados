import json
from tweepy import OAuthHandler, Stream , StreamListener
from datetime import datetime

# Cadastra as chaves de acesso
# API key:  RrFDMtiYkCqbhb3IPFleRTsNm
# API secret key:  wWdYH8uXAVV8NQYWkEMZE5FvFtAgLA2OtKUrM5Pdg3Ja1JvmGc
# Access token:  24053778-gxFxEFaANl6MelEXH7LBnzGSJ7NGlqOgrYbvbgk1C
# Access token secret:    ahqhDKbSq8rOLV9adfKoGtMUkloDp1tfwgzUP4z1GqttM

consumer_key = 'RrFDMtiYkCqbhb3IPFleRTsNm'
consumer_secret = 'wWdYH8uXAVV8NQYWkEMZE5FvFtAgLA2OtKUrM5Pdg3Ja1JvmGc'
access_token = '24053778-gxFxEFaANl6MelEXH7LBnzGSJ7NGlqOgrYbvbgk1C'
access_token_secret = 'ahqhDKbSq8rOLV9adfKoGtMUkloDp1tfwgzUP4z1GqttM'

#definir arquivo de saida para armazenar os tweets coletados
# abrindo arquivo para escrita
data_hoje = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
out = open(f'collected_tweets{data_hoje}.txt', 'w')

#implementar classe para conexão com o tweeter
# fica escutando o tweeter
class MyListener(StreamListener): 
    def on_data(self,data):
#         print(data)
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self,status):
        print(status)
        
        
#implementar a função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    stream = Stream(auth,l)    
    stream.filter(track=['Lula','Bolsonaro'])