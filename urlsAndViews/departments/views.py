import json

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


def view_with_name(request, variable):  # should be named the same way as in the urls
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {'variable': variable}, status=200)


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args} Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    return JsonResponse({"pk": pk})


def view_with_slug(request, pk, slug):
    # OPTION 1 for 404
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


def redirect_to_view(request):
    # return redirect(http://127.0.0.1:8000) breaks abstraction
    # return redirect(index)  breaks single responsibility if view is from another app
    return redirect('home', status=302)  # best option
