from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from todo.models import Todo
from django.db.models import Q


def index_view(request):
    todos = Todo.objects.all()
    my_search_value = request.GET.get("searchValue")
    if my_search_value:
        if my_search_value.isdigit():
            todos = todos.filter(id=my_search_value)
        else:
            todos = todos.filter(Q(name__icontains=my_search_value) |
                                 Q(status=my_search_value),
                                 )

    paginator = Paginator(todos, 2)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {
        "objects": todos,
        "p": p,
        "search": my_search_value,
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


CHOICES = (
    ("Hələ başlanmayıb", "not"),
    ("Davam edir", "progress"),
    ("Bitib", "finish")
)


def edit_view(request, id):
    edit_obj = Todo.objects.get(id=id)
    task_name = request.POST.get("task")
    task_status = request.POST.get("status")
    if request.method == "POST":
        if task_name:
            edit_obj.name = task_name
        if task_status:
            edit_obj.status = task_status

        edit_obj.save()
        return redirect("/")

    context = {
        "edit_obj": edit_obj,
        "choices": CHOICES,
    }
    return render(request, "update.html", context)
