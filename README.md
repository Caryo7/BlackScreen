# Bienvenue dans le BlackScreen wiki !

Ce programme a été développé pour les professeurs qui utilisent un tableau blanc pour écrire, et projeter depuis un ordinateur. Les couleurs et les formes sont parfois problématiques pour une bonne lecture des élèves, c'est pourquoi ce logiciel permet de faire une fenêtre noir, et de masquer les images.
> [!CAUTION]
> Le programme n'est fonctionnel **uniquement** sous **Windows** !

## Utilisation
Vous pouvez utiliser le logiciel facilement. Une fois lancé, une fenêtre noir apparait en plein écran. Cette dernière **n'est pas au premier plan** ! Vous pouvez donc en mettre au dessus sans problèmes.

## Fonction pratique
Pour voir sous la fenêtre noire, utilisez la touche Majuscule. Cette dernière rend le programme transparent pour laisser apparaitre le contenu de l'écran. Vous saurez donc où se trouvent vos autres fenêtres. 

## Zones transparentes
Pour créer une zone transparente, utiliser la souris : enfoncez le bouton gauche, déplacez le curseur jusqu'à la position voulue, et relachez le bouton.

> [!TIP]
> Cette fonction a été développée pour une utilisation d'un écran tactile.

Si la fenêtre ne vous convient pas, utilisez le bouton Poubelle (icone dans un coin de la zone transparente) pour la supprimer.
> [!IMPORTANT]
> Une fois la zone transparente créée, vous ne pouvez plus la modifier.

> [!TIP]
> Vous pouvez maintenir la touche majuscule en même temps que vous déplacez le curseur de la souris pour voir sous la fenêtre en temps réel.

## Fermeture
Pour fermer la fenêtre, utilisez le raccourcis clavier Alt + F4, ou cliquez sur la croix en haut à gauche de la fenêtre (en rougeà.

## Configuration
Pour configurer le programme, vous devez ouvrir le fichier `{app dir}\config\default.ini`. Voici la structure du fichier
```
[app]
transparentcolor = green  ; Couleur à retirer sur la fenêtre pour la rendre transparente (ne pas l'utiliser pour les autres, sinon vous ne verrez plus rien)
bordercolor = red         ; Couleur des bords de zone transparentes
alphakey = shift          ; Touche qui rend la fenêtre transparente
drawingcolor = blue       ; Couleur de la zone transparente pendant l'édition

[cross]
size = 20                 ; Taille de la croix de fermeture
color = red               ; Couleur de la croix de fermeture

[window]
size = 15                 ; Taille du rond de suppression de la zone transparente
```

## Execution depuis le code
Pour lancer le programme depuis le code source, lancez `blackscreen.py` avec un éditeur python.
Packages requirement:
 - tkinter
 - configparser
 - pyinstaller
Programmes de compilation d'installateurs : Inno Setup Scripts

## Compilation
Utilisez le script `compile.bat` pour compiler le programme, ou exécutez les commandes suivantes
```
> pyinstaller blackscreen.spec
> iscc compilation.iss
```
Les fichiers de sortis sont dans `/dist/blackscreen/` pour le programme version mobile, et `/releases/` pour le script d'installation. Veillez à changer le numéro de version pour ne pas écraser les installateurs !

> [!IMPORTANT]
> Merci de ne pas modifier le fichier `blackscreen.spec` ou du moins, de ne pas en re-créer un avec `pyinstaller blackscreen.py`. Cela le rendrait inopérant sur la copie des fichiers de configuration.
