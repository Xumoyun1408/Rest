"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from new_app.views import TravelView, MehmonhonaView, KlassView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/travel/',TravelView.as_view()),
    path('api/v1/travel/<int:pk>/',TravelView.as_view()),
    path('api/v2/mehmonhona/',MehmonhonaView.as_view()),
    path('api/v2/mehmonhona/<int:pk>/',MehmonhonaView.as_view()),
    path('api/v3/class/',KlassView.as_view()),
    path('api/v3/class/<int:pk>/',KlassView.as_view()),
]
