## INSSET-Steganographie
<blockquote><i>Repository created by students for educational purpose</i></blockquote>

----------
# Présentation de la stéganographie

A l'instare du cryptage, la stéganographie a pour vocation de dissimuler une information. Mais plutôt que de la rendre illisible par une tierce personne, la stéganographie rend l'information invisible, ou du moins cherche à le faire. Si il est necessaire de passer beaucoup de temps à analyser les messages pour casser le code utilisé en cryptographie, il en est de même pour comprendre la structure du message en stéganographie. <br>
A ceci près qu'il faille déjà qu'un message soit dissimulé. En effet, puisque le message est caché, il n'y a presque aucun moyen de savoir si un message est présent tant que l'on ne l'a pas trouvé. Des messages peuvent passer sous vos yeux sans que vous ne les voyez, ou alors vous pouvez vous mettre à chercher un message innexistant.<br>
Voilà toute la puissance de la stéganographie !

## Des méthodes simples

Il existe des moyens simples en informatique pour réaliser de la stéganographie. Nous allons vous présenter deux cas parmis les plus simples qu'il soit: les images au format Bitmap et au format PNG.

### Bitmap

Commençons par les images au format bitmap. 
Pour ce format, chaque pixel de l'image peut être codé autant sur 1 bit que sur 24, soit <strong>entre 2 et 16,8 millions de couleurs !</strong><br>
Vous pensez bien que sur 16 millions de nuances, il y en a beacoup qui se ressemblent !<br>
D'où l'idée suivante: cachez un message sur le bit de poids faible. En effet, le bit de poids faible ne vaut que 1, donc vous aurez du mal à voir la diférence entre du rouge 255 et du rouge 254. Et comme les images contienent de plus en plus de pixel, je vous laisse imaginer combien d'espace nous avons maintenant pour y cacher des informations.
![bitmap_exemple](https://cloud.githubusercontent.com/assets/16888022/12569462/71e0efac-c3cf-11e5-9146-8985719811c8.png)

### PNG

Maintenant passons aux images PNG. 
Le principe est un peu différent: plutôt que de noter la valeur de chaque pixel, quitte à avoir des doublons, on écrit la valeur d'une couleur dans une table et on donne l'index correspondant à la couleur aux pixels concernés.<br>
L'avantage est que sur des images simples, le poids est grangement réduit. Mais en ce qui nous concerne, c'est surtout la table qui nous interesse.<br>
Il suffit d'écrire des valeurs dans la table qui ne sont pas utilisé dans l'image et le tour est joué ! plutôt simple, non ?
![png_exemple](https://cloud.githubusercontent.com/assets/16888022/12570186/b593e780-c3d5-11e5-9f33-93627991e877.png)
Le format PNG accept même un codage sur 48 bits, soit<strong> environs 281.000 milliard de valeurs !</strong><br>
Le seul inconvéniant, c'est que si vous avez une petite image avec seulement dix couleurs différentes qui pèse 1 Mo, c'est tout de suite suspect et il est facile de voir qu'il y a des couleurs non utilisées, donc il faut savoir doser la quantité d'information à injecter.

## Des outils libres

La communautée open source pronant la libérté, et la stéganographie permettant dans certain pays de passer outre la censure, il n'est pas surprenant de trouver un certain nombre d'outils libres sur le sujet.<br>
On trouve par exemple le packet **`steghide`** qui permet très simplement de dissimuler du texte dans une image, ou un fichier audio dans un autre ou dans une vidéo. Par exemple: <br>
`steghide embed --embedfile MonSecret.png --coverfile MonCamouflage.png`<br>
L'image MonSecret.png est cachée dans une autre image qui s'appelle MonCamouflage.png.

Voici un exemple concret:<br>
Nous avons une image lambda et une image à cacher.
![tmp1](https://cloud.githubusercontent.com/assets/16888022/12570847/a6d5b29a-c3db-11e5-85e9-c5bbb24c3345.PNG)
![tmp3](https://cloud.githubusercontent.com/assets/16888022/12570875/d8b3a9de-c3db-11e5-8aa5-5898242c6871.PNG)

On obtient alors l'image suivante:
![tmp2](https://cloud.githubusercontent.com/assets/16888022/12570899/0e8eea8c-c3dc-11e5-9cb4-494baf14d9be.PNG)

Si vous arrivez à voir une différence à l'oeil nu, je veux bien manger mon chapeau !


Il est également possible de trouver une variété de librairies dans de nombreux langages pour réaliser facilement un programme de stéganographie. Vous pouvez par exemple employer le module `Image` la librairie `PIL` de Python pour reproduire les techniques que j'ai montré au début !<br>
```
from PIL import Image

secret_stream = []; contient le message bit à bit
j = 0; index de secret_stream

I = Image.open( "facade.jpg" );
matrice = list( I.getdata() ); on récupère la liste des pixels
width, height = matrice.size; on récupère les dimensions de l'image

for y in range(height) :
  for x in range(width) :
    matrice[x,y] = matrice[x,y] - ( matrice[x,y] % 2 ) + secret_stream[j]; écrit le message bit à bit
    j++;
```

Il y a une multitude de possibilité pour dissimuler un message: il suffit d'être créatif !

