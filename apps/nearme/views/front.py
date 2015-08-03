from django.shortcuts import render


def index(request):
    ctx = {}
    template_name = "nearme/front/index.html"
    return render(request, template_name, ctx)
