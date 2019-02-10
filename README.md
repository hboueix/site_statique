# Générateur de site statique

## Génerer un site statique
Les fichiers compris par un navigateur internet sont aux formats HTML/CSS/JavaScript. Vous n'avez peut-être pas envie de taper du HTML quand vous écrivez un blog. Il serait pratique de générer les pages web à partir d'un format textuel simple, comme le markdown, langage utilisé pour écrire le document que vous lisez actuellement.

## Projet
Le but était de réaliser un outil convertissant un dossier de fichiers markdown en un autre dossier contenant les fichiers d'un site statique. Du HTML est généré à partir du markdown, cet HTML est mélangé avec des modèles de pages web pour générer des pages toutes conformes au même modèle.

## Réalisation d'une interface en ligne de commande
Pour ce faire, nous avons réaliser un outil en ligne de commande. Il prend plusieurs paramètres :
* `convert` : **seul paramètre positionnel** (obligatoire) pour lancer la conversion
* `-i ./un_dossier` ou `--input_directory ./un_dossier` : le chemin du dossier de fichiers source (contenant les fichiers markdown)
* `-o ./un_dossier` ou `--output_directory ./un_dossier` : le chemin du dossier où seront mis les fichiers générés pour le site statique
    * si le dossier existe déjà, les fichiers générés efface les anciens seulement s'ils portent le même nom
    * le nom du fichier généré est fonction du nom du fichier source mardown suivi d'un underscore puis du nom du template
* `-t ./un_dossier` ou `--template-directory ./un_dossier` : le chemin du dossier contenant les modèles de pages web à complèter (le nom du modèle html et le nom du modele css doivent être le même, excepté l'xtension bien sûr)
* `-h` ou `--help` : pour afficher de l'aide pour expliquer les paramètres de la commande

## Rendu sur Github
Dans ce repository vous trouverez un fichiers `libprogramme.py` contenant les fonctions utiles pour notre outil et un fichier `programme.py` qui utilise donc ces fonctions. C'est ce dernier fichier qu'il faut appeler avec les paramètres pour lancer notre outil.  
  
Un exemple de ligne de commande :  
  
`python .\programme.py --input-directory ./dossier_md -o ./dossier_html -t ./dossier_template`  
  
A noter que vous pouvez télécharger le dossier en entier et utilisez les dossier */md*, */html*, et */template* qui sont déjà en paramètres par défaut. Votre commande serait donc simplement :  
  
`python .\programme.py convert`