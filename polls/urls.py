from django.urls import path

from polls import views

# urlpatterns = [
#     re_path(r'^$', views.index, name='index'),
#     re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
