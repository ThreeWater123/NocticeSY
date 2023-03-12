from django.urls import path
from . import views
app_name='catalog'

urlpatterns = [
    path('',views.group_list.as_view(),name='group' ),
    path('groups/<int:pk>',views.group_detail.as_view(),name="group_detail"),
    path('groups/<int:pk>/update',views.group_UpdateNotice.as_view(),name="update"),
]