
# Lecture du contenu du md

def lecture(fichier): # fichier = pathlib
    lignes = list()
    with fichier.open() as f:
        contenu = f.read()
        list_lignes = contenu.split('\n')
        for ligne in list_lignes:
            if ligne != '':
                lignes.append(ligne)
        return lignes


# Conversion du md vers html

def conversion(lignes): # lignes = liste
    global nb_li
    nb_li = 0 # Nb de balises <li>
    lignes_modif = list()
    n_ligne = 0
    c = '#####'
    for ligne in lignes:
        n = 0

        # Titres
        if ligne[n] == '#':
            while ligne[n] == '#':
                n += 1
            ligne = ligne.replace(c[:n], '<h' + str(n) + '>', 1)
            ligne += '</h' + str(n) + '>'
        
        # Listes
        elif ligne[n] == '*':
            if ligne.count('*') % 2 != 0:
                nb_li += 1
                if nb_li == 1:
                    ligne = '<ul><li>' + ligne[1:] + '</li>'
                else:
                    ligne = '<li>' + ligne[1:] + '</li>'
                try:
                    if lignes[n_ligne + 1][0] != '*':
                        ligne += '</ul>'
                        nb_li = 0
                except IndexError:
                    ligne += '</ul>'
                    nb_li = 0

        # URL


        # Emphase


        # Paragraphes
        else:
            ligne = '<p>' + ligne + '</p>'
        
        lignes_modif.append(ligne)

        n_ligne += 1
    return lignes_modif


# Création des fichiers html

def ecriture(chemin, contenu):
    print(chemin)
    with open(chemin, 'w') as f:
       f.write(('\n').join(contenu))