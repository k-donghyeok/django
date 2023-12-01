from django.urls import path,include
from . import views
from .views import IndexView,DetailView,ResultsView,vote
from django.contrib import admin
app_name = 'polls'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    #path('',views.index,name='index'),
    #path('<int:question_id>/',views.detail,name='detail'),
    #path('admin/',admin.site.urls),
    #path('polls/',include('polls.urls')),
    #path('books/',include('books.urls')),
    #path('',views.name,name='name'),
    #path('',views.index, name='index'),
    #path('<int:question_id>/',views.detail,name='detail'),
    #path('<int:question_id>/results/',views.results,name='results'),

    ]