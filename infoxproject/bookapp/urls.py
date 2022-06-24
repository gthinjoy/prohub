from django.conf import settings
from django.conf.urls.static import static
from  .  import views
from django.urls import path
app_name= 'bookapp'
urlpatterns = [
      path('', views.books, name='books'),
      path('movie/<int:book_id>/', views.details, name='detail'),
    path('add/', views.add_books, name='add_books'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)