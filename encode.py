#-*- coding:Latin-1 -*-

from PIL import Image
im = Image.open("image.png")
#on récupère les dimensions de l'image
w,h=im.size
#On extrait les quatre composantes (rouge vert bleu alpha)
r,g,b,a=im.split()
#on transforme l'image en liste
r=list(r.getdata())

#on stock le message à cacher
c="Test micro: un, deux, un, deux..."
#on note la longueur de la chaine et on la convertis en binaire
u=len(c)
v=bin(len(c))[2:].rjust(8,"0")
#on convertis la chaine en une chaine binaire
ascii=[bin(ord(x))[2:].rjust(8,"0") for x in c]
l=''.join(ascii)
#on code la longueur de la liste dans les 8 premiers pixels rouges
for j in range(8):
    r[j]=2*int(r[j]//2)+int(v[j])

#on cche la chaine dans les pixels suivants
for i in range(8*u):
    r[i+8]=2*int(r[i+8]//2)+int(l[i])
#on recrée l'image rouge 
#nr = Image.new("L",(16*p,16*q))
nr = Image.new("L",(w,h))
nr.putdata(r)
#fusion des trois nouvelles images
imgnew = Image.merge('RGB',(nr,g,b)) 
imgnew.save("cover.png") 
