from django.shortcuts import render, redirect
from todo.models import Todo


def index_view(request):
    todos = Todo.objects.all()

    context = {
        "objects": todos,
    }
    return render(request, "index.html", context)


def add_view(request):
    add_value = request.POST.get("addValue")

    if add_value:
        my_obj = Todo.objects.create(
            name=add_value
        )
        my_obj.save()
        return redirect("/")


    context = {}
    return render(request, "add.html", context)


def detail_view(request, id):
    my_obj = Todo.objects.get(id=id)
    context = {
        "myobj": my_obj
    }
    return render(request, "detail.html", context)

