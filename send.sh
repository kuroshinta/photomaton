#script qui prend fusionne et poste les photos
sudo gphoto2 --force-overwrite --capture-image-and-download --filename bob.jpg #prend la photo et la télécharge sur le raspberry
sudo gm composite logo.png bob.jpg bob.jpg #fusionne avec le logo, http://www.graphicsmagick.org/composite.html pour avoir des infos sur les options
python tweet.py #envoie du tweet

