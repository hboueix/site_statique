from argparse import *

parser = ArgumentParser(description = 'Générateur de site statique')

parser.add_argument("-i", "--input_directory", help = "Chemin du dossier de fichiers source (contenant les fichiers markdown")
parser.add_argument("-o", "--output_directory", help = "Chemin du dossier où seront mis les fichiers générés pour le site statique. Si le dossier existe déjà il sera remplacé.")
parser.add_argument("-t", "--template_directory", help = "Dossier contenant des modèles de pages web à compléter")

args = parser.parse_args()

if args.input_directory:
    print(f'Le chemin du dossier de fichiers source : {args.input_directory}')

if args.output_directory:
    print(f'Le chemin du dossier avec les fichiers créés : {args.output_directory}')

if args.template_directory:
    print(f'Le chemin du dossier contenant des modèles de pages web : {args.template_directory}')
