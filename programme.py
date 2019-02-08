from argparse import ArgumentParser
from pathlib import Path

from libprogramme import *

parser = ArgumentParser(description = 'Générateur de site statique')

parser.add_argument('convert', help = "Lance la conversion du markdown en html") # Argument positionnel
parser.add_argument("-i", "--input_directory", help = "Chemin du dossier de fichiers source (contenant les fichiers markdown", default = './md')
parser.add_argument("-o", "--output_directory", help = "Chemin du dossier où seront mis les fichiers générés pour le site statique. Si le dossier existe déjà il sera remplacé.", default = './html')
parser.add_argument("-t", "--template_directory", help = "Dossier contenant des modèles de pages web à compléter", default = './template')

args = parser.parse_args()

# Arguments optionnels
if args.input_directory:
    print(f'Le chemin du dossier de fichiers source : {args.input_directory}')
if args.output_directory:
    print(f'Le chemin du dossier avec les fichiers créés : {args.output_directory}')
if args.template_directory:
    print(f'Le chemin du dossier contenant des modèles de pages web : {args.template_directory}')

p = Path('.')
files_md = sorted(p.glob(args.input_directory + '/*.md'))

for md in files_md:
    lignes = lecture(md)
    lignes_modif = conversion(lignes)
    chemin = args.output_directory + '/' + str(md)[3:-3] + '.html'
    ecriture(chemin, lignes_modif)
    
