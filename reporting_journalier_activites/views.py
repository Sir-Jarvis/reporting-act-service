from django.shortcuts import render
from rest_framework import status, permissions,viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser
import json
from rest_framework import generics


@permission_classes((permissions.AllowAny,))
class ProjetAPIView(APIView):

    def get(self,request,*args, **kwargs):
        projets = Projet.objects.all()
        serializer = ProjetSerializer(projets,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,formate=None,*args, **kwargs):       
        serializer = ProjetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        projet = serializer.save()
        return Response(ProjetSerializer(projet).data, status=status.HTTP_201_CREATED)


@permission_classes((permissions.AllowAny,))
class ProjetDetailAPIView(APIView):

    def get_projet(self,id):
        try:
            return Projet.objects.get(id=id)
        except Projet.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        projet = self.get_projet(id=id)
        if not projet:
            return Response({"reponse":"Ce projet n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjetSerializer(projet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id,*args, **kwargs):
        projet = self.get_projet(id=id)
        if not projet:
            return Response({"reponse":"Ce projet n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)

        serializer = ProjetCreateSerializer(instance=projet,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        projet = serializer.save()
        return Response(ProjetSerializer(projet).data, status=status.HTTP_201_CREATED)


    def delete(self,request,id,*args, **kwargs):
        projet = self.get_projet(id=id)
        if not projet:
            return Response({"reponse":"Ce projet n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        projet.delete()
        return Response({"reponse": "Suppression reussie!"},status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class ActiviteAPIView(APIView):
    def get_projet(self,id):
        try:
            return Projet.objects.get(id=id)
        except Projet.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        projet = self.get_projet(id=id)
        if not projet:
            return Response({"reponse":"Ce projet n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        activites = Activite.objects.filter(projet=id)
        serializer = ActiviteSerializer(activites,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,formate=None,*args, **kwargs):       
        serializer = ActiviteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        activite= serializer.save()
        return Response(ActiviteSerializer(activite).data, status=status.HTTP_201_CREATED)


@permission_classes((permissions.AllowAny,))
class ActiviteDetailAPIView(APIView):
    def get_activite(self,id):
        try:
            return Activite.objects.get(id=id)
        except Activite.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        activite = self.get_activite(id=id)
        if not activite:
            return Response({"reponse":"Cette activite n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        serializer = ActiviteSerializer(activite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id,*args, **kwargs):
        activite = self.get_activite(id=id)
        if not activite:
            return Response({"reponse":"Cette acivite n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)

        serializer = ActiviteCreateSerializer(instance=activite,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        projet = serializer.save()
        return Response(ActiviteSerializer(activite).data, status=status.HTTP_201_CREATED)

    def delete(self,request,id,*args, **kwargs):
        activite = self.get_projet(id=id)
        if not activite:
            return Response({"reponse":"Cette activite n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        activite.delete()
        return Response({"reponse": "Suppression reussie!"},status=status.HTTP_200_OK)

    

class TacheAPIView(APIView):

    def get_activite(self,id):
        try:
            return Activite.objects.get(id=id)
        except Activite.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        activite = self.get_activite(id=id)
        if not activite:
            return Response({"reponse":"Cette activite n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        taches = Tache.objects.filter(activite=id)
        serializer = TacheSerializer(taches,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,formate=None,*args, **kwargs): 
        serializer = TacheCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tache = serializer.save()
        return Response(TacheSerializer(tache).data, status=status.HTTP_201_CREATED)


class TacheDetailAPIView(APIView):

    def get_tache(self,id):
        try:
            return Tache.objects.get(id=id)
        except Tache.DoesNotExist:
            return None


    def get(self,request,id,*args, **kwargs):
        tache = self.get_tache(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        serializer = TacheSerializer(tache)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self,request,id,*args, **kwargs):
        tache = self.get_tache(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)

        serializer = TacheCreateSerializer(instance=tache,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        tache = serializer.save()
        return Response(TacheSerializer(tache).data, status=status.HTTP_201_CREATED)

    def delete(self,request,id,*args, **kwargs):
        tache = self.get_projet(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        tache.delete()
        return Response({"reponse": "Suppression reussie!"},status=status.HTTP_200_OK)



class OutilAPIView(APIView):

    def get_tache(self,id):
        try:
            return Tache.objects.get(id=id)
        except Tache.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        tache = self.get_tache(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        outils = Outil.objects.filter(tache=id)
        serializer = OutilSerializer(outils,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request,formate=None,*args, **kwargs): 
        serializer = OutilCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        outil = serializer.save()
        return Response(OutilSerializer(outil).data, status=status.HTTP_201_CREATED)


class OutilDetailAPIView(APIView):

    def get_outil(self,id):
        try:
            return Outil.objects.get(id=id)
        except Outil.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        outil = self.get_outil(id=id)
        if not outil:
            return Response({"reponse":"Cet outil n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        serializer = OutilSerializer(tache)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id,*args, **kwargs):
        outil = self.get_outil(id=id)
        if not outil:
            return Response({"reponse":"Cet outil n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)

        serializer = OutilCreateSerializer(instance=outil,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        outil = serializer.save()
        return Response(OutilSerializer(outil).data, status=status.HTTP_201_CREATED)

    def delete(self,request,id,*args, **kwargs):
        outil = self.get_outil(id=id)
        if not outil:
            return Response({"reponse":"Cette outil n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        outil.delete()
        return Response({"reponse": "Suppression reussie!"},status=status.HTTP_200_OK)


class CommentaireAPIView(APIView):

    def get_tache(self,id):
        try:
            return Tache.objects.get(id=id)
        except Tache.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        tache = self.get_tache(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        commentaire = Commentaire.objects.filter(tache=id)
        serializer = CommentaireSerializer(commentaire,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,formate=None,*args, **kwargs): 
        serializer = CommentaireCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        commentaire = serializer.save()
        return Response(CommentaireSerializer(commentaire).data, status=status.HTTP_201_CREATED)


class CommentaireDetailAPIView(APIView):
    def get_tache(self,id):
        try:
            return Tache.objects.get(id=id)
        except Tache.DoesNotExist:
            return None

    def get_commentaire(self,id):
        try:
            return Commentaire.objects.get(id=id)
        except Commentaire.DoesNotExist:
            return None

    def get(self,request,id,*args, **kwargs):
        tache = self.get_tache(id=id)
        if not tache:
            return Response({"reponse":"Cette tache n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        commentaire = Commentaire.objects.get(id=id)
        serializer = CommentaireSerializer(commentaire,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self,request,id,*args, **kwargs):
        commentaire = self.get_commentaire(id=id)
        if not commentaire:
            return Response({"reponse":"Cette commentaire n'existe pas!"},status=status.HTTP_400_BAD_REQUEST)
        commentaire.delete()
        return Response({"reponse": "Suppression reussie!"},status=status.HTTP_200_OK)

    

    

    


    

        









# class ProjetCreateView(generics.ListCreateAPIView):
    
#     queryset = Projet.objects.all()
#     serializer_class = ProjetSerializer
#     name = "Projet-list"


