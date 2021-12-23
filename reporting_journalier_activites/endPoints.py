from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'institution', InstitutionViewSet, basename='institution')


# urlpatterns = router.urls 
# urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('projets',ProjetAPIView.as_view()),
    path('projets/<int:id>',ProjetDetailAPIView.as_view()),
    path('projet/<int:id>/activites',ActiviteAPIView.as_view()),
    path('activites/<int:id>',ActiviteDetailAPIView.as_view()),
    path('activites/<int:id>/taches',TacheAPIView.as_view()),
    path('taches/<int:id>',TacheDetailAPIView.as_view()),
    path('taches/<int:id>/outils',OutilAPIView.as_view()),
    path('outils/<int:id>',OutilDetailAPIView.as_view()),
    path('tache/<int:id>/comments',CommentaireAPIView.as_view()),
    path('comments/<int:id>',CommentaireDetailAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
