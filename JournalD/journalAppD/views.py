from django.http import HttpResponse
from django.shortcuts import render
# import to make use of the database table Resource
from journalAppD.forms import ResourceForm
from journalAppD.models import Resource


# Create your views here.

def home(request):
    return HttpResponse("Hello World!")


def view_resources(request):
    # gets all the objects in the database
    resources = Resource.objects.all().order_by("-date_created")

    return render(request, 'resources.html', {
        'resource_list': resources, })


def update_resource(request, resource_id=None):
    resource = None
    if resource_id:
        # Load existing object
        resource = Resource.objects.get(id=resource_id)
    if request.method == "POST":
        # Save form
        resource_form = ResourceForm(request.POST, instance=resource)
        new_resource = resource_form.save(commit=False)
        new_resource.save()
        resource_form = ResourceForm(request.POST, instance=new_resource)
    else:
        # Load blank form
        resource_form = ResourceForm(instance=resource)
    return render(request, 'resource.html', {
        'resource_form': resource_form, })

