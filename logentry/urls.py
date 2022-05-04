
from django.urls import include, path
from .views import ReadingLogEntryCreate, ReadingLogEntryList, ReadingLogEntryDetail, ReadingLogEntryUpdate, ReadingLogEntryDelete
from .views import ListeningLogEntryCreate, ListeningLogEntryList, ListeningLogEntryDetail, ListeningLogEntryUpdate, ListeningLogEntryDelete

urlpatterns = [
    path('reading/create/', ReadingLogEntryCreate.as_view(), name='create-reading-log'),
    path('reading/', ReadingLogEntryList.as_view()),
    path('reading/<int:pk>/', ReadingLogEntryDetail.as_view(), name='retrieve-reading-log'),
    path('reading/update/<int:pk>/', ReadingLogEntryUpdate.as_view(), name='update-reading-log'),
    path('reading/delete/<int:pk>/', ReadingLogEntryDelete.as_view(), name='delete-reading-log'),

    path('listening/create/', ListeningLogEntryCreate.as_view(), name='create-listening-log'),
    path('listening/', ListeningLogEntryList.as_view()),
    path('listening/<int:pk>/', ListeningLogEntryDetail.as_view(), name='retrieve-listening-log'),
    path('listening/update/<int:pk>/', ListeningLogEntryUpdate.as_view(), name='update-listening-log'),
    path('listening/delete/<int:pk>/', ListeningLogEntryDelete.as_view(), name='delete-listening-log'),
]