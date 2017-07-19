comment qu'on installe ?
c'est easy !
git clone https://github.com/kuroshinta/photomaton.git

les truc à installer :
* sudo apt-get install graphicsmagick
* pip install RPi.GPIO
	-> si pas encore pip
	-->wget https://bootstrap.pypa.io/get-pip.py
	-->python get-pip.py
* pip install tweepy

   pour ouvrir la carte SD depuis linux :
* ouvrir terminal
* sudo -i
*cd /
*cd media
*choisir ca carte SD ( souvent le grand truc ) cd 2***
*nautilus home/pi/photobooth

alors ce petit dossier est assez simple je vais vous donner un petit descriptif des éléments qu'il contient :

bob = la derniere photo qui a été prise
button = gére l'appuie du bouton et qui renvoie vers le script send qui fusionne les photos
logo = le logo qui sera fusionné sur la photo
send = le script qui prend et fusionne les photos
tweet = gére l'envoie du tweet

voila donc pour resumer si vous voulez changer le logo vous changer le fichier logo.png si vous voulez changé la phrase qui est twetter c'est dans tweet.py et pour changer de compte twitter c'est aussi dans tweet.py

le branchement du bouton sur le raspberry c'est entre la pin la 6 et 5 de la premiere colonne
