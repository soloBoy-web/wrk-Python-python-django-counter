from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_accounts.urls')),

    path('', include('app_counter.urls'))
]
