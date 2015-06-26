from django.conf.urls import url
from .views import AuthorListView, AuthorDetailView

urlpatterns = [
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(),
        name='author-detail'),
]
