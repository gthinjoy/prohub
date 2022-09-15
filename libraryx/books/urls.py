from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from  . import views
app_name= 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.detail, name="detail"),
    path('add/', views.add_book, name="add_book"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)