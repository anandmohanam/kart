
from django.urls import path
from mycart import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_fun, name='login'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('accounts/<int:pk>/', views.accounts, name='accounts'),
    path('payment/', views.payment, name='payment'),
    path('payment_confirmation',views.payment_confirmation,name='payment_confirmation'),
    path('success/', views.success_page, name='success_page'),
    path('order/<int:pk>/', views.order, name='order'),
    path('mycarts/', views.mycarts, name='mycarts'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('logout/', views.logout_page, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)