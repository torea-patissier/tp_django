## TP django
Ce projet est un système de gestion de films, permettant d'ajouter, de modifier, de supprimer et de rechercher des films, des réalisateurs, des scénarios et des acteurs, ainsi que de gérer les locations.

### Installation

- Cloner le dépôt à partir de GitHub :

`git@github.com:torea-patissier/tp_django.git`

-  Installer les dépendances en utilisant pip :

`pip install -r requirements.txt`

-  Effectuer les migrations de la base de données :

`python manage.py migrate`

### Execution

- Lancer le serveur de développement :

`python manage.py runserver`

### S'authentifier

`http://127.0.0.1:8000/admin/`
- Login : torea
- PWD: Azerty123&

### Documentation POSTMAN
[ Cliquer ici](https://documenter.getpostman.com/view/18685609/2s93CGQFZH)

J'ai choisi POSTMAN pour la documentation car c'est un outil qui me permet de:
- Tester toutes mes routes
- Pouvoir collaborer si besoin en équipe
- Documenter mes routes avec l'URL  / la requête / la réponse attendu
- Partager cette documentation sur internet

### Les routes
- `http://127.0.0.1:8000/api/realisteur/`
- `http://127.0.0.1:8000/api/scenario/`
- `http://127.0.0.1:8000/api/film/`
- `http://127.0.0.1:8000/api/acteur/`
- `http://127.0.0.1:8000/api/jouer/`


### Fonctionnalités

Ajouter, modifier, supprimer et rechercher des films, des réalisateurs, des scénarios et des acteurs
Rechercher les acteurs ayant joué dans au moins un film avec un réalisateur donné (par l'ID)
Ajouter et supprimer des acteurs à un film
Gérer les locations de films : ajouter, supprimer, prêter, rendre et afficher les films prêtés et non rendus


### Contributeur

Toréa Patissier
