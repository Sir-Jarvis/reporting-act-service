from django.http import Http404
from .models import *
from rest_framework import serializers



class CollaborateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaborateur
        fields = "__all__"

class CommentaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentaire
        fields = "__all__"


class OutilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outil
        fields = "__all__"


class TacheSerializer(serializers.ModelSerializer):
    outil = OutilSerializer(many=True,read_only=True)

    class Meta:
        model = Tache
        fields = "__all__"
      



class ActiviteSerializer(serializers.ModelSerializer):
    tache = TacheSerializer(many=True,read_only=True)

    class Meta:
        model = Activite
        fields = "__all__"


class ProjetSerializer(serializers.ModelSerializer):
    activite = ActiviteSerializer(many=True)
    collaborateurs = CollaborateurSerializer(many=True)
    
    class Meta:
        model = Projet
        fields = ('id','activite','nom','description','user_creator','collaborateurs')



class ProjetCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projet
        fields = "__all__"

    def get_collaborateur(self,id):
        """get it from users"""
        pass
    
    def get_user_creator(self,id):
        """get it from users"""
        pass

    def create(self,validated_data):
        collaborateurs = validated_data.pop('collaborateurs')
        projet = Projet.objects.create(**validated_data)
        for collabo in collaborateurs:
            projet.collaborateurs.add(collabo)
            projet.save()
        return projet


class ActiviteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activite
        fields = "__all__"

    def create(self,validated_data):
        activite = Activite.objects.create(**validated_data)
        activite.save()
        return activite


class TacheCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tache
        fields = "__all__"

    def create(self,validated_data):
        tache = Tache.objects.create(**validated_data) 
        return tache



class OutilCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outil
        fields = "__all__"

    def create(self,validated_data):
        outil = Outil.objects.create(**validated_data) 
        return outil


class CommentaireCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentaire
        fields = "__all__"

    def create(self,validated_data):
        commentaire = Commentaire.objects.create(**validated_data)
        return commentaire


    

