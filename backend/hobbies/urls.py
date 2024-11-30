from django.urls import path
from .views import UserHobbyListView, UserHobbyDetailView, UpdateHobbyStatusView

urlpatterns = [
    path('my/', UserHobbyListView.as_view(), name='user_hobby_list'),
    path('<int:hobby_id>/', UserHobbyDetailView.as_view(), name='user_hobby_detail'),
    path('<int:hobby_id>/status/', UpdateHobbyStatusView.as_view(), name='update_hobby_status'),
]