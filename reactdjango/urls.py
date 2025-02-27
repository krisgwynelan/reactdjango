from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('reactdjango/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('reactdjango/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrive-update'),

]