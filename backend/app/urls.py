from django.urls import path
from app.views import MovieDetail,StreamPlateform,StreamPlateformD,MovieListView
from app.test import StreamPlatformAV,StreamDetailAV,ReviewListView,ReviewDetailAV,MovieDetailAV
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:id>', MovieDetail, name='movie'),
    path('streamlist/', StreamPlatformAV.as_view(), name='streamlist'),
    path('movie/<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-detail'),

    path('reviews/', ReviewListView.as_view(), name='reviews'),
    path('movie/review/<int:pk>', ReviewDetailAV.as_view(), name='review-detail'),



]
app_name = 'app'