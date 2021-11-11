# P10_SoftDesk

## Présentation

Ce programme est une version beta d'un site internet permettant suivi des problèmes pour les trois plateformes web, Android et iOS. 


, 
Les trois applications exploiteront les points de terminaison d'API qui serviront les données. aux utilisateurs de pouvoirs poster et obtenir des avis sur des livres.

Les objectifs de ce programme sont les suivants:
L'application permettre aux utilisateurs:

 * de creer divers projets
 * d'ajouter des utilisateurs à des projets spécifiques
 * de créer des problèmes au sein des projets
 * d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme.

## Pré-requis

* Python 3 installé [Télécharger Python](https://www.python.org/downloads/)
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel. Pour cela, ci dessous les étapes à suivre:

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/JM-Duval/P10_SoftDesk.git```
    

Vous devez voir (depuis votre explorateur) les dossiers suivants: 

 * comment/
 * contributor/
 * issue/
 * project/
 * softdesk_project/
 * user/

Et les fichiers suivants:

 * .gitignore
 * README.md
 * manage.py
 * requirements.txt

2. **Creer un environnement virtuel.**

Depuis windows/mac/linux: ```python3 -m venv env```

3. **Activer l'environnement.**

Depuis windows: ```env\Scripts\activate.bat```

Depuis mac/linux: ```source env/bin/activate```

Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
[Documentation Python](https://www.python.org/doc/)

4. **Installer les paquets.**

```pip install -r requirements.txt```

En executant la commande: pip freeze, vous devez voir apparaitre cette liste: 
 - asgiref==3.4.1
 - Django==3.2.8
 - django-debug-toolbar==3.2.2
 - djangorestframework==3.12.4
 - djangorestframework-simplejwt==4.8.0
 - PyJWT==2.1.0
 - pytz==2021.3
 - sqlparse==0.4.2


5. **Lancement du programme.**

A l'endroit ou se situe votre dossier, exécuter la commande suivante:

```./manage.py runserver```

Losque vous allez lancer le programme depuis le terminal, vous allez voir apparaitre le texte ci dessous:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 11, 2021 - 16:14:35
Django version 3.2.8, using settings 'softdesk_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Copiez l'adresse ```http://127.0.0.1:8000/``` dans la barre de votre navigateur web. Vous devez accèder directement sur le site internet concerné.


## Fabriqué avec
[PyCharm Community Edition 2020.2.3 x64](https://pycharm-community-edition.fr.softonic.com/) - Editeur de textes


## Auteurs

* **JM Duval** 

