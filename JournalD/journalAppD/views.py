from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# import to make use of the database table Resource
from django.urls import reverse

from journalAppD.forms import ResourceForm
from journalAppD.models import Resource

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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


def delete_resource(request, resource_id):
    global resource
    try:
        resource = Resource.objects.get(id=resource_id)
        resource.delete()
        resources = Resource.objects.all().order_by("-date_created")
        return render(request, 'resources.html', {
            'resource_list': resources, })
    except resource.DoesNotExist:

        resources = Resource.objects.all().order_by("-date_created")
        return render(request, 'resources.html', {
            'resource_list': resources, })


def resources_pdf(request):
    # Create BytesStream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Choose the model
    resources = Resource.objects.all().order_by("-date_created")

    # Add some lines of text
    lines = []

    for resource in resources:
        lines.append("Date : " + str(resource.date_created))
        lines.append("Title : " + resource.title)
        lines.append("Content :")
        lines.append(resource.content)
        lines.append(" ")
        lines.append(
            "------------------------------------------------------------------------------------------------------------ ")
        lines.append(
            "------------------------------------------------------------------------------------------------------------ ")
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="Journal.pdf")


def single_resource_pdf(request, resource_id):
    # Create BytesStream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Choose the model
    resource = Resource.objects.get(id=resource_id)

    # Add some lines of text
    lines = []


    lines.append("Date : " + str(resource.date_created))
    lines.append("Title : " + resource.title)
    lines.append("Content :")
    lines.append(resource.content)
    lines.append(" ")
    lines.append(
        "------------------------------------------------------------------------------------------------------------ ")
    lines.append(
        "------------------------------------------------------------------------------------------------------------ ")
    lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="Journal.pdf")


def search_resources(request):
    if request.method == "POST":
        searched = request.POST['searched']
        resources = Resource.objects.filter(title__icontains=searched)
        return render(request, 'search_resources.html', {'searched': searched, 'resources': resources})
    else:
        return render(request, 'search_resources.html', {})
