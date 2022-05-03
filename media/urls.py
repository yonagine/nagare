from django.urls import include, path
from .views import MediaCreate, MediaList, MediaDetail, MediaUpdate, MediaDelete

urlpatterns = [
    path('create/', MediaCreate.as_view(), name='create-media'),
    path('', MediaList.as_view()),
    path('<int:pk>/', MediaDetail.as_view(), name='retrieve-media'),
    path('update/<int:pk>/', MediaUpdate.as_view(), name='update-media'),
    path('delete/<int:pk>/', MediaDelete.as_view(), name='delete-media'),
]