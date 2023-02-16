from rest_framework import serializers
from .models import Realisateur, Scenario, Film, Acteur, Jouer


class RealisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisateur
        fields = ['id', 'nom', 'prenom', 'age', 'pays']


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id', 'titre', 'description']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'id_realisateur', 'id_scenario', 'titre', 'description', 'duree_minutes', 'genre']


class ActeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acteur
        fields = ['id', 'nom', 'prenom', 'age']


class JouerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jouer
        fields = ['id_film', 'id_acteur']
