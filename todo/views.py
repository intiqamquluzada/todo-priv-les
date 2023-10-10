from django.shortcuts import render

#VIEW


def index_view(request):
    context = {
    }
    return render(request, "index.html", context)


