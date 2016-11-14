#!/usr/bin/env python2.7
# tweetpic.py take a photo with the Pi camera and tweet it
# by Alex Eames http://raspi.tv/?p=5918
import tweepy
from subprocess import call
from datetime import datetime

i = datetime.now()               #take time and date for filename
now = i.strftime('%Y%m%d-%H%M%S')
# photo_name = now + '.jpg'
# cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name 
# call ([cmd], shell=True)         #shoot the photo

# Consumer keys and access tokens, used for OAuth
######## C'est ici qu'on renseigne les éléments du compte twitter faite un tour sur https://apps/twitter.com pour créer une application et avoir ces informations #######
consumer_key = '8s8hK4A8EeOjIpxAam1tRH5D9'
consumer_secret = 'hb44lvHvd2KLHvzGSuCDcBQvUMzwGlxuzac5w89Wu5RkvMFBPF'
access_token = '3395381020-29gJxAId2wYntZWMvNFLam8Po3ZzhxeNoRSiDF8'
access_token_secret = 'FfvYr1sOyWHntf8TIq9H4CZKjXSSq0SU22lcTyd09lDfR'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Send the tweet with photo
photo_path = '/home/pi/photobooth/bob.jpg' # la photo qui sera envoyé
# origine > status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S')
status = 'le Clik-Clak des petit deb est en marche! venez le tester' # Texte qui est tweeté
api.update_with_media(photo_path, status=status)

