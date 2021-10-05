from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='login_url'),name="logout"),
    path('create/', views.create_product, name='create_product'),
    path('create/orders', views.create_order, name='create_order'),

    path('create/products', views.create_products, name='create_products'),
    path('create/stores', views.create_stores, name='create_stores'),
    path('delete/<str:product_name>', views.delete_product, name='delete_product'),
    path('search/', views.search_product, name='search_product'),
    path('update/<str:product_name>', views.update_product, name='update_product'),
    path('add_products/<str:product_id>', views.add_product, name='add_product')

]