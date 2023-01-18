from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from polls import views
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"books", views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]