"""tutorial1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
#router.register(r'users',views.UserViewSet)
#router.register(r'groups',views.GroupViewSet)


urlpatterns = [
    #path('',include(router.urls)),
    #path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('',include('advisorapi.urls')),
    #path('',include('tutorialapi.tutorial1.snippets.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)