from django.urls import path
#from rest_framework.routers import DefaultRouter
from . import views
#from .views import LinkListApi, LinkCreateApi, LinkUpdateApi, LinkDeleteApi

app_name="links"

#router = DefaultRouter()
#router.register(r'links', LinkCreateApi, basename= 'link'  )

#urlpatterns = [] + router.urls

urlpatterns = [
    path("create/", views.LinkCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.LinkUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.LinkDeleteApi.as_view(), name="api_delete"),
    path("", views.LinkListApi.as_view(), name="api_list"),
]

#http://127.0.0.1:8000/links
