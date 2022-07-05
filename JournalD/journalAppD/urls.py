
from django.urls import path
from .views import home, view_resources, update_resource, delete_resource, resources_pdf, search_resources

app_name = "journalAppD"

urlpatterns = [
    path('', view_resources),
    path('resource', update_resource, name="create_resource"),
    path('resource/<int:resource_id>/', update_resource, name="update_resource"),
    path('resources', view_resources, name="view_resources"),
    path('delete_resource/<int:resource_id>/',delete_resource, name="delete_resource"),
    path('resources_pdf', resources_pdf, name="resources_pdf"),
    path('search_resources', search_resources, name="search_resources"),

]
