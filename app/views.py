from rest_framework import viewsets
from .models import Realisateur, Scenario, Film, Acteur, Jouer, Client, Emprunter
from .serializers import RealisateurSerializer, ScenarioSerializer, FilmSerializer, ActeurSerializer, JouerSerializer, \
    ClientSerializer, EmprunterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class RealisateurViewSet(viewsets.ModelViewSet):
    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ActeurViewSet(viewsets.ModelViewSet):
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
    queryset = Jouer.objects.all()
    serializer_class = JouerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class EmprunterViewSet(viewsets.ModelViewSet):
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

#
# class DirigeantViewSet(ModelViewSet):
#     serializer_class = SerializerDirigeant
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#
#         queryset = Dirigeant.objects.all()
#
#         nomparam = self.request.GET.get('nom')
#         prenomparam = self.request.GET.get('prenom')
#
#         if nomparam is not None:
#             queryset = queryset.filter(nom=nomparam)
#
#         if prenomparam is not None:
#             queryset = queryset.filter(style=prenomparam)
#
#         return queryset
#
#
# class MagasinViewSet(ModelViewSet):
#     serializer_class = SerializerMagasin
#
#     def get_queryset(self):
#
#         queryset = Magasin.objects.all()
#
#         nomparam = self.request.GET.get('nom')
#         adresseparam = self.request.GET.get('adresse')
#         dirigeant = self.request.GET.get('dirigeant')
#         ca = self.request.GET.get('ca')
#
#         if nomparam is not None:
#             queryset = queryset.filter(nom=nomparam)
#
#         if adresseparam is not None:
#             queryset = queryset.filter(style=adresseparam)
#
#         if dirigeant is not None:
#             queryset = queryset.filter(style=dirigeant)
#
#         if ca is not None:
#             queryset = queryset.filter(style=ca)
#
#         return queryset
#
#
# class MeubleViewSet(ModelViewSet):
#     serializer_class = SerializerMeuble
#
#     def get_queryset(self):
#
#         queryset = Meuble.objects.all()
#
#         nomparam = self.request.GET.get('nom')
#         etat = self.request.GET.get('etat')
#         magasin = self.request.GET.get('magasin')
#         prix = self.request.GET.get('prix')
#         statut = self.request.GET.get('statut')
#
#         if nomparam is not None:
#             queryset = queryset.filter(nom=nomparam)
#
#         if etat is not None:
#             queryset = queryset.filter(style=etat)
#
#         if magasin is not None:
#             queryset = queryset.filter(style=magasin)
#
#         if prix is not None:
#             queryset = queryset.filter(style=prix)
#
#         if statut is not None:
#             queryset = queryset.filter(style=statut)
#
#         return queryset
