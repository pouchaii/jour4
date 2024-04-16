import requests ##import de la fonction(librairie) requests
from bs4 import BeautifulSoup ## import de la fonction request
#url = "https://asuratoon.com/" # inserez l'url qu'on veut scrapper
url = "https://asuratoon.com/genres/adventure/"
response = requests.get(url)#envoyer sa requette au  site
##print(response) ## aficher la reponse
content = response.content ## recuperer le contenu de la requette 
#print(content)
soup = BeautifulSoup(content,'html.parser')#parser pour transformer en code html
##print(soup)
##img = soup.find('div class="bsx"')
##print(img)
img = soup.find_all('a') #jai chercher la classe ou se trouvais les img
#avec la commande fand_all je trouve meme les class 
#print(img)
manga_sorti = soup.find_all('a', attrs= {'class':"series"}) 
#chercher dans une classe un element specifique 

rating = soup.find_all('div',attrs={'itemprop':"ratingValue"})
#print(rating)
barre_recherche_gauche = soup.find_all('div', attrs= {'id':"sidebar"})
#print(barre_recherche_gauche)
#soup.find_all pour chercher un element dans la soup
release_week = soup.find_all('div',attrs={'class':'serieslist pop wpop wpop-weekly'})
#print(release_week)
#creer un tableau poru stocker les release_week
tableau_week = []
for e in release_week:
    tableau_week.append(e.text .upper())
print(tableau_week)


note = soup.find_all('div',attrs={'class': "rt"})
#print(note)
#recuperer toute la soup html pour pouvoir la trier
##img = soup.find('img') #trouver la balise qui nous interresse 
##print(img)# afficher le truc qu'on veut
image_scan = soup.find_all(attrs={'div class':'imgseries'})
#print(image_scan)
tout_les_notes = soup.find_all('div',attrs={'class':"numscore"})
#print(tout_les_notes)
## je veux selectionner la liste des mangas du week-end et leurs notes 
rating =[]
serie_liste_gauche = soup.find('div',attrs={'class':"leftseries"})
#je cherche les notes de la liste
list_gauche = serie_liste_gauche.find(class_="numscore")
#b = serie_liste_gauche.find_all()
for e in list_gauche:

    petite_list= e.text
     #j'ai remarqué que la note etait le debut d'un nouveau manga, faudrais que je retire /n avant et apres chaque /n
     # solution une fonction qui des que je vois un chiffre je supprime le /n avant et apres
    rating.append(e)
print(rating)
print("bonjour")

#for e in list:
        #si e  est egale a un chiffre alors je remove le /n jusqu'a ce que e= chaine de caractere
        #probleme si le chiffre est de type string
        #faudrais peut etre specifier que si e = [0-9] r strip, jusqu'a ce que j'ai e =! [0-9]
        #si 

       # if 
    #e = e.get_(strip="\n")
    #e.replace("\n"," ")
    #ici je prends la liste des nom et leur note j'add a mon tableau
    
    

    

b= []

#print(e.text)#afficher le text 

list_serie = soup.find_all('a',attrs={'rel':"tag"})
#for e in list_serie:
    #(e.text)
tableau_nom =  []
for e in list_serie:
    tableau_nom.append(e.text)
print(tableau_nom)



