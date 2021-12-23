from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Collaborateur)
class CollaborateurAdmin(admin.ModelAdmin):
    lost_display = ('user',)

@admin.register(Outil)
class OutilAdmin(admin.ModelAdmin):
    list_display = ('nom','tache')


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('nom','stagiaireAttribue','dateDeb','dateFin','dateValidation','activite')

@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('nom','description','projet')

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom','description','user_creator')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('content','user','dateComment','tache')






