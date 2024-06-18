
from django.urls import path
from mycart import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_fun, name='login_fun'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('payment', views.payment, name='payment'),
    path('mycarts/', views.mycarts, name='mycarts'),
    path('order/<int:pk>/', views.order, name='order'),
    path('logout_page/', views.logout_page, name='logout_page'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)