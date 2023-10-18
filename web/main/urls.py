from django.urls import path

from . import views

urlpatterns = [
	path('model/', views.model, name='model'),
	path('model_use/',views.model_use,name='model_use'),
	path('', views.first, name='first'),
	path('data', views.index, name='index'),
	path('<key>/', views.second, name='second'),
	path('<key>/<title>/', views.third, name='third'),
]