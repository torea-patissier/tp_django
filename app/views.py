from rest_framework import viewsets
from .models import Realisateur, Scenario, Film, Acteur, Jouer, Client, Emprunter
from .serializers import RealisateurSerializer, ScenarioSerializer, FilmSerializer, ActeurSerializer, JouerSerializer, \
    ClientSerializer, EmprunterSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class RealisateurViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class FilmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ActeurViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Acteur.objects.all()
    serializer_class = ActeurSerializer

    @action(detail=True, methods=['get'])
    def films_joues(self, request, pk=None):
        acteur = self.get_object()
        films = Film.objects.filter(jouer__acteur=acteur)
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def ajouter_film(self, request, pk=None):
        acteur = self.get_object()
        film_id = request.data.get('film_id', None)
        if film_id:
            try:
                film = Film.objects.get(pk=film_id)
            except Film.DoesNotExist:
                return Response({'detail': 'Le film spécifié n\'existe pas.'}, status=400)
            if acteur.films.filter(pk=film_id).exists():
                return Response({'detail': 'L\'acteur joue déjà dans ce film.'}, status=400)
            Jouer.objects.create(film=film, acteur=acteur)
            return Response({'detail': 'L\'acteur a été ajouté au film avec succès.'}, status=201)
        else:
            return Response({'detail': 'L\'identifiant du film est requis.'}, status=400)

    @action(detail=True, methods=['post'])
    def supprimer_film(self, request, pk=None):
        acteur = self.get_object()
        film_id = request.data.get('film_id', None)
        if film_id:
            try:
                film = Film.objects.get(pk=film_id)
            except Film.DoesNotExist:
                return Response({'detail': 'Le film spécifié n\'existe pas.'}, status=400)
            if not acteur.films.filter(pk=film_id).exists():
                return Response({'detail': 'L\'acteur ne joue pas dans ce film.'}, status=400)
            Jouer.objects.filter(film=film, acteur=acteur).delete()
            return Response({'detail': 'L\'acteur a été supprimé du film avec succès.'}, status=200)
        else:
            return Response({'detail': 'L\'identifiant du film est requis.'}, status=400)


class JouerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Jouer.objects.all()
    serializer_class = JouerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class EmprunterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EmprunterSerializer
    queryset = Emprunter.objects.all()

    @action(detail=True, methods=['post'])
    def preter(self, request, pk=None):
        emprunt = self.get_object()
        serializer = self.get_serializer(emprunt, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def rendre(self, request, pk=None):
        emprunt = self.get_object()
        emprunt.est_rendu = True
        emprunt.save()
        serializer = self.get_serializer(emprunt)
        return Response(serializer.data)
