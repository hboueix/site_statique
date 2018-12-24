import os

cwd = os.getcwd()
balises = ['<', '</', '>']
lignes_md = []
lignes_html = ['<!DOCTYPE html>', '<html>', '<head></head>', '<body>']
nb_fichier = 0
fileName, fileExtension = 0, 0

def start(file_md, dir_html):
    global fileName, fileExtension
    fileName, fileExtension = os.path.basename(file_md).split('.')
    lecture(file_md)
    ecriture(dir_html)

def lecture(file_md):
    global lignes_md, lignes_html
    os.chdir(cwd)
    with open(file_md, 'r') as fichier:
        contenu = fichier.read()
        lignes_md = contenu.split('\n')
        print(lignes_md) # Test
    nv_lignes = []
    for ligne in lignes_md:
        nv_lignes.append(detect(ligne))
    lignes_html += nv_lignes + ['</body>', '</html>']
    print(lignes_html) # Test

def ecriture(dossier):
    os.chdir(dossier)
    with open(fileName + '.html', 'w') as fichier:
        fichier.write(('\n ').join(lignes_html))

def detect(ligne):
    try:
        c = ligne[0]
    except IndexError:
        if ligne == '':
            return ligne
    else:
        if c == '#':
            return titres(ligne)
        #if c == '*' or c == '+':
        #   return listes(ligne)
        else:
            return '<p>' + ligne + '</p>'
    
def titres(ligne):
    c = '#'
    n = 0
    bal = 'h'
    while ligne[n] == c:
        n += 1
    bal += str(n) 
    return balises[0] + bal + balises[2] + ligne[n:] + balises[1] + bal + balises[2]

def listes(ligne):
    c = ('*', '+', '-')
    ul = 'ul'
    li = 'li'



