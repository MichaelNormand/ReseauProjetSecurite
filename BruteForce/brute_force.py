def append_char():
    fichier = open('dicitonnary.txt', 'r')
    string = None
    nombre_ligne = 0
    for ligne in fichier:
        nombre_ligne = nombre_ligne + 1
    fichier.close()
    for x in range(0, nombre_ligne):
        fichier = open('dicitonnary.txt', 'r')
        if x != 0:
            for y in range(0, x):
                string = fichier.readline()
        else:
            string = fichier.readline()
        fichier.close()
        fichier = open('dicitonnary.txt', 'a')
        for y in range(33, 126):
            write = string + (chr(y))
            fichier.write(write)
        fichier.close()


file = open('dicitonnary.txt', 'w')
for x in range(33, 126):
    file.write(chr(x) + '\n')
file.close()
# longueur du tableau : 93

for x in range(0, 7):
    append_char()
