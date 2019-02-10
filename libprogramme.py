
# Lecture du contenu du md

def lecture(fichier): # fichier = pathlib
    '''
    Cette fonction permet de lire le fichier markdon passé en paramètre.
    Elle renvoie un liste des lignes contenues dans ce fichier.
    '''
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
    '''
    Cette fonction va parcourir une liste de lignes.
    Elle déterminera s'il faut modifier ces lignes en les regardant une par une.
    Elle renvoie une liste de lignes modifiées, soit converties en html.
    '''
    global nb_li
    nb_li = 0 # Nb de balises <li>
    lignes_modif = list()
    n_ligne = 0
    c = '#####'
    for ligne in lignes:
        n = 0

        while ligne[n] == ' ':
            try:
                ligne[n + 1]
                n += 1
            except IndexError:
                continue
        ligne = ligne[n:]
        n = 0
       
        # Titres
        if ligne[n] == '#':
            n_c = n
            while ligne[n_c] == '#':
                n_c += 1
            n_c -= n
            ligne = ligne.replace(c[:n_c], '<h' + str(n_c) + '>', 1)
            ligne += '</h' + str(n_c) + '>'
        
        # Listes
        elif ligne[n] == '*':
            if ligne.count('*') % 2 != 0:
                nb_li += 1
                if nb_li == 1:
                    ligne = '<ul><li> ' + ligne[1:] + ' </li>'
                else:
                    ligne = '<li> ' + ligne[1:] + ' </li>'
                try:
                    ind = 0
                    while lignes[n_ligne + 1][ind] == ' ':
                        ind += 1
                    if lignes[n_ligne + 1][ind] != '*':
                        ligne += ' </ul>'
                        nb_li = 0
                except IndexError:
                    ligne += ' </ul>'
                    nb_li = 0

        # URL
        mots = ligne.split(' ')
        for i, l in enumerate(mots):
            if l[:7] == 'http://' or l[:8] == 'https://':
                mots[i] = '<a href="' + mots[i] + '">' + mots[i] + '</a>'
        ligne = ' '.join(mots) + '\n'

        # Emphase
        if ligne.count('*') % 2 == 0:
            while '*' in ligne:
                ligne = ligne.replace('*', '<em>', 1)
                ligne = ligne.replace ('*', '</em>', 1)      
        
        
        lignes_modif.append(ligne)

        n_ligne += 1
    return lignes_modif


# Création des fichiers html

def ecriture(chemin, contenu, template):
    '''
    Cette fonction écrit la chaîne de caractère 'contenu' dans des fichiers html générés à partir des templates.
    Pour chaque fichier elle va généré un fichier html pour chacun des templates.
    '''
    modele = ''
    with open(template, 'r') as f:
        modele = f.read()
        # Requirements
        contenu = modele.replace('REPLACE-ME', contenu, 1) 
        contenu = contenu.replace('TITLE', chemin.split('/')[-1])
        contenu = contenu.replace('href=STYLE', 'href=".' + template[:-4] + 'css"')
    list_temp = template.split('/')
    nom_temp = list_temp[-1]
    nom_html = chemin + '_' + nom_temp
    with open(nom_html, 'w') as f:
       f.write(contenu)
    print(f'Le fichier {nom_html} a été créé !')