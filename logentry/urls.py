
from django.urls import include, path
from .views import ReadingLogEntryCreate, ReadingLogEntryList, ReadingLogEntryDetail, ReadingLogEntryUpdate, ReadingLogEntryDelete
from .views import ListeningLogEntryCreate, ListeningLogEntryList, ListeningLogEntryDetail, ListeningLogEntryUpdate, ListeningLogEntryDelete

urlpatterns = [
    path('logs/reading/create/', ReadingLogEntryCreate.as_view(), name='create-reading-log'),
    path('logs/reading/', ReadingLogEntryList.as_view()),
    path('logs/reading/<int:pk>/', ReadingLogEntryDetail.as_view(), name='retrieve-reading-log'),
    path('logs/reading/update/<int:pk>/', ReadingLogEntryUpdate.as_view(), name='update-reading-log'),
    path('logs/reading/delete/<int:pk>/', ReadingLogEntryDelete.as_view(), name='delete-reading-log'),

    path('logs/listening/create/', ListeningLogEntryCreate.as_view(), name='create-listening-log'),
    path('logs/listening/', ListeningLogEntryList.as_view()),
    path('logs/listening/<int:pk>/', ListeningLogEntryDetail.as_view(), name='retrieve-listening-log'),
    path('logs/listening/update/<int:pk>/', ListeningLogEntryUpdate.as_view(), name='update-listening-log'),
    path('logs/listening/delete/<int:pk>/', ListeningLogEntryDelete.as_view(), name='delete-listening-log'),
]