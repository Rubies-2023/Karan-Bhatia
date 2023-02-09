from django.urls import path
from . import views
#from mysite.mysite import settings
from mysite.settings import *
from django.contrib.auth.decorators import login_required


app_name = 'polls'
# urlpatterns  = [
#     path('',views.index.as_view(),name='index'),
#     path('<int:question_id>/',views.detail,name='detail'),
#     path('<int:question_id>/result/',views.results,name='result'),
#     path('<int:question_id>/vote/',views.vote,name='vote'),
# ]
app_name = 'polls'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('vote/<int:question_id>/<int:answer_id>/', views.vote, name='vote'),

]
# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root= STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)