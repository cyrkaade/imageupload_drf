from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_app.viewsets import UploadImageViewSet
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = DefaultRouter()
router.register(r'imageupload', UploadImageViewSet)

urlpatterns = [
    re_path(r'^',include(router.urls)),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)