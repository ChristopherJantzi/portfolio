from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('news_item/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_item/new/', views.news_new, name='news_new'),
    path('news_item/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('resume/', views.resume, name='resume'),
    path('feedback/', views.feedback, name='feedback'),
    path('blog_entries/2026-problem-of-time', views.article, name='2026-problem-of-time'),
]

'''
Patterns are all like this:
    path('<page>', views.<view_name>, name='view_name'),
        <page> is the address extension from the website
        <view_name> is the function name in the VIEWS.PY file
        'view_name' is the way this path is referred to later? I'm not sure, honestly
'''