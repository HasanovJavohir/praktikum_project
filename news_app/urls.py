from django.urls import path
from .views import news_list, newsdetailview, IndexPageView, contactView, page404View, aboutPageView, LocalNewsView, \
    SportNewsView, TechnologyNewsView, ForeignNewsView

urlpatterns = [
    path('', IndexPageView.as_view(), name="home_page"),
    path('news/all/', news_list, name='all_news_list'),
    path('contact-us/', contactView, name='contact_page'),
    path('404page/', page404View, name='404_page'),
    path('about/', aboutPageView, name='about_page'),
    path('local/', LocalNewsView.as_view(), name='local_page'),
    path('sport/', SportNewsView.as_view(), name='sport_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_page'),
    path('<slug:news>/', newsdetailview, name='news_detail_page'),
]
