from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # request on http: [GET]
    path('articles/', views.ArticleApiView.as_view(), name='articles'),

    # request on http: [POST,PUT,DELETE,GET/pk]
    path('articles/<slug:key>/', views.ArticleApiView.as_view(), name='articles-key'),
]
