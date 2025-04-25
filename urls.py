from django.urls import path
from capture import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('user_form/', views.user_form, name='user_form'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('save_photo/', views.save_photo, name='save_photo'),
    path('logout/', views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
