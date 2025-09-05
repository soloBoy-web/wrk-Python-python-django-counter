from django.urls import path
from app_counter import views


app_name = "app_counter"

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="counter"),
    path("counter/create", views.create_counter, name="create_counter"),
    path("counter/<int:counter_id>/increase", views.increase_counter, name="increase_counter"),
    path("counter/<int:counter_id>/decrease", views.decrease_counter, name="decrease_counter"),
    path("counter/<int:counter_id>/set_favorite", views.set_favorite, name="set_favorite"),
    path("counter/<int:counter_id>/delete", views.delete_counter, name="delete_counter"),
    path("counter/remove_favorite", views.remove_favorite, name="remove_favorite"),

]