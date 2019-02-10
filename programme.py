from argparse import ArgumentParser

from pathlib import Path

from libprogramme import lecture, conversion, ecriture

parser = ArgumentParser(description = 'Générateur de site statique')

# Argument positionnel
parser.add_argument('convert', help = "Lance la conversion du markdown en html") 

# Arguments optionnels
parser.add_argument("-i", "--input_directory", 
                    help = "Chemin du dossier de fichiers source (contenant les fichiers markdown", 
                    default = './md')
parser.add_argument("-o", "--output_directory", 
                    help = "Chemin du dossier où seront mis les fichiers générés pour le site statique", 
                    default = './html')
parser.add_argument("-t", "--template_directory", 
                    help = "Dossier contenant des modèles de pages web à compléter", 
                    default = './template')

args = parser.parse_args()

if args.input_directory:
    print(f'Le chemin du dossier de fichiers source : {args.input_directory}')
if args.output_directory:
    print(f'Le chemin du dossier avec les fichiers créés : {args.output_directory}')
if args.template_directory:
    print(f'Le chemin du dossier contenant des modèles de pages web : {args.template_directory}')

p = Path('.')
files_md = sorted(p.glob(args.input_directory + '/*.md'))
files_temp = sorted(p.glob(args.template_directory + '/*.html'))

for md in files_md:
    lignes = lecture(md)
    lignes_modif = conversion(lignes)
    contenu = ('\n').join(lignes_modif)
    chemin = args.output_directory + '/' + str(md)[3:-3]
    for temp in files_temp:
        template = './' + ('/').join(str(temp).split('\\'))
        ecriture(chemin, contenu, template)
    
