import os
from argparse import *
from libprog import *

parser = ArgumentParser(description = 'Générateur de site statique')

parser.add_argument('convert', help = "Lance la conversion du markdown en html")
parser.add_argument("-i", "--input_directory", help = "Chemin du dossier de fichiers source (contenant les fichiers markdown", default = './md')
parser.add_argument("-o", "--output_directory", help = "Chemin du dossier où seront mis les fichiers générés pour le site statique. Si le dossier existe déjà il sera remplacé.", default = './html')
parser.add_argument("-t", "--template_directory", help = "Dossier contenant des modèles de pages web à compléter")

args = parser.parse_args()

if args.input_directory:
    print(f'Le chemin du dossier de fichiers source : {args.input_directory}')

if args.output_directory:
    print(f'Le chemin du dossier avec les fichiers créés : {args.output_directory}')

if args.template_directory:
    print(f'Le chemin du dossier contenant des modèles de pages web : {args.template_directory}')

files_md = os.listdir(args.input_directory)
print(files_md)


for md in files_md:
    start(args.input_directory + '/' + md, args.output_directory)
