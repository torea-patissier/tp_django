from django.db import models
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.pop('refresh')
        access_token = response.data.pop('access')
        response.data['token'] = access_token
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        return response


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)


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
