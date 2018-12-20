import requests
import wikipedia


#Primeira questão

#API 1

# Api para procurar coisas no wikipedia

d = str(input('Digite sua busca: '))
l = wikipedia.search(d)
l1 = wikipedia.summary(l[0], sentences=1)
print(l1)

#API 2

#Api que procura por musicas,albuns ou artistas


api_key = '2573b6924d7f594eb61735a7dde4bb40'
url = 'http://ws.audioscrobbler.com/2.0/?method=album.search&album=Alivio imediato&api_key={0}&format=json'.format(api_key)

response = requests.get(url).json()

print(response)


#API 3

# Api do firebase usando um post

url = 'https://projeto-scrum.firebaseio.com/message_list.json'
dadosJson  = {"user_id" : "jack", "text" : "Ahoy!"}

response = requests.post(url,json=dadosJson)

print(response)




