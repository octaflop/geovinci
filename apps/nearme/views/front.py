from django.shortcuts import render


def index(request):
    ctx = {}
    ctx['demo'] = "index"
    template_name = "nearme/front/index.html"
    return render(request, template_name, ctx)
