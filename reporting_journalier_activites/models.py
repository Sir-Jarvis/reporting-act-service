from django.db import models

# Create your models here.

class Collaborateur(models.Model):
    user = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name = ("Collaborateur")
        verbose_name_plural = ("Collaborateurs")

    def __str__(self):
        return str(self.user)



class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    collaborateurs = models.ManyToManyField(Collaborateur,blank=True)
    user_creator = models.IntegerField() 
    

    class Meta:
        verbose_name = ("Projet")
        verbose_name_plural = ("Projets")

    def __str__(self):
        return self.nom

class Activite(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)  
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="activite")  

    class Meta:
        verbose_name = ("Activites")
        verbose_name_plural = ("Activites")

    def __str__(self):
        return self.nom



class Tache(models.Model):
    nom = models.CharField(max_length=50)
    stagiaireAttribue = models.IntegerField(null=True,blank=True)
    dateDeb = models.DateField(blank=True)
    dateFin = models.DateField(blank=True)
    dateValidation = models.DateTimeField(null=True,blank=True,default=None)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE,related_name="tache")
    

    class Meta:
        verbose_name = ("Tache")
        verbose_name_plural = ("Taches")

    def __str__(self):
        return self.nom



class Outil(models.Model):
    nom = models.CharField(max_length=50)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE,related_name="outil",blank=True,null=True)

    class Meta:
        verbose_name = ("Outil")
        verbose_name_plural = ("Outils")

    def __str__(self):
        return self.nom



class Commentaire(models.Model):
    content = models.TextField()
    user = models.IntegerField()
    dateComment = models.DateField(auto_now_add=True)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE,related_name="commentaire")

    class Meta:
        verbose_name = ("Commentaire")
        verbose_name_plural = ("Commentaires")

    def __str__(self):
        return self.content






