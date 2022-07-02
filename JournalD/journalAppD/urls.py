
from django.urls import path
from .views import home, view_resources, update_resource

app_name = "journalAppD"

urlpatterns = [
    path('', home),
    path('resource', update_resource, name="create_resource"),
    path('resource/<int:resource_id>/', update_resource, name="update_resource"),
    path('resources', view_resources, name="view_resources"),

]
