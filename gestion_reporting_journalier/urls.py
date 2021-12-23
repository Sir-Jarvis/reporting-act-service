from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('reporting_journalier_activites.endPoints')),
    path('schema/', get_schema_view(
    title="Reporting-Journalier-Activites-API",
    description="API pour les activités journaliers",
    version="1.0.0"
    ), name="reporting-journalier-activites-schema"),
    path('', include_docs_urls(
        title="OrganisationAPI",
        description="API pour les activités journaliers",
    ), name="reporting-journalier-activites-docs")
]
