from django.db import models


class Realisateur(models.Model):
    nom = models.CharField(max_length=255, null=False)
    prenom = models.CharField(max_length=255, null=False)
    age = models.IntegerField()
    pays = models.CharField(max_length=255)


class Scenario(models.Model):
    titre = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)


class Film(models.Model):
    id_realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE, null=False)
    id_scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=False)
    titre = models.CharField(max_length=255, null=False)
    description = models.TextField()
    duree_minutes = models.IntegerField()
    genre = models.CharField(max_length=255)


class Acteur(models.Model):
    nom = models.CharField(max_length=255, null=False)
    prenom = models.CharField(max_length=255, null=False)
    age = models.IntegerField()


class Jouer(models.Model):
    id_film = models.ForeignKey(Film, on_delete=models.CASCADE, null=False)
    id_acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE, null=False)


class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateCreationCompte = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Emprunter(models.Model):
    id_film = models.ForeignKey(Film, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_pret = models.DateField()
    date_retour = models.DateField()
    est_rendu = models.BooleanField(default=False)
