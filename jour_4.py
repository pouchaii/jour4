import requests ##import de la fonction requests
from bs4 import BeautifulSoup ## import de la fonction request
url = "https://asuratoon.com/" # inserez l'url qu'on veut scrapper
response = requests.get(url)#envoyer sa requette au  site
##print(response) ## aficher la reponse
content = response.content ## recuperer le contenu de la requette 
##print(content)
soup = BeautifulSoup(content,'html.parser')
##print(soup)
##img = soup.find('div class="bsx"')
##print(img)
img = soup.find_all('a') #jai chercher la classe ou se trouvais les img
#avec la commande fand_all je trouve meme les class 
print(img)
manga_sorti = soup.find_all('a href')
print(manga_sorti)

#recuperer toute la soup html pour pouvoir la trier
##img = soup.find('img') #trouver la balise qui nous interresse 
##print(img)# afficher le truc qu'on veut

