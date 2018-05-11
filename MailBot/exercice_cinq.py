#! /usr/bin/env python
import smtplib, sys    ## Importation du module

serveur = smtplib.SMTP('smtp.gmail.com', 587)    # Connexion au serveur sortant (en précisant son nom et son port)
serveur.ehlo()
serveur.starttls(None)    # Spécification de la sécurisation
serveur.login(sys.argv[1], sys.argv[2])    # Authentification
message = """From: Shadow_Hacker <shadow_hacker@domain.com> 
To: {}
Subject: Hacking system installing

A virus has been detected on your email chat box, so we let it go in your mail :)""".format(sys.argv[1], sys.argv[3])   # Message à envoyer
serveur.sendmail(sys.argv[1], sys.argv[3], message)    # Envoie du message
serveur.quit()    # Déconnexion du serveur
