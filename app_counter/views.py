from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.db.models import F
from django.shortcuts import render, reverse, get_object_or_404
from app_counter.models import Counter


def index(request):
    counters = Counter.objects.filter(is_favorite=True)

    return render(
        request=request,
        template_name="app_counter/index.html",
        context={
            "counters": counters
        }
    )


@login_required()
def counter(request):
    counters = Counter.objects.filter(user=request.user)

    return render(
        request=request,
        template_name="app_counter/counter.html",
        context={
            "counters": counters
        }
    )


@login_required
def create_counter(request):
    counter = Counter.objects.create(
        user=request.user,
        name=f"Счетчик {Counter.objects.filter(user=request.user).count() + 1}"
    )
    counter.save()
    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def increase_counter(request, counter_id):
    counter = get_object_or_404(Counter, id=counter_id, user=request.user)
    counter.value = F('value') + 1
    counter.save()
    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def decrease_counter(request, counter_id):
    counter = get_object_or_404(Counter, id=counter_id, user=request.user)
    counter.value = F('value') - 1
    counter.save()
    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def set_favorite(request, counter_id):
    if request.method == "POST":

        Counter.objects.filter(user=request.user).update(is_favorite=False)


        counter = get_object_or_404(Counter, id=counter_id, user=request.user)
        counter.is_favorite = True
        counter.save()

        return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

    return HttpResponseBadRequest("Invalid request method")


@login_required
def remove_favorite(request):
    if request.method == "POST":

        Counter.objects.filter(user=request.user).update(is_favorite=False)
        return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

    return HttpResponseBadRequest("Invalid request method")


@login_required
def delete_counter(request, counter_id):
    if request.method == "POST":
        counter = get_object_or_404(Counter, id=counter_id, user=request.user)
        counter.delete()
        return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

    return HttpResponseBadRequest("Invalid request method")