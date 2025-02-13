from django.urls import path
from .views import news_list, newsdetailview, IndexPageView, contactView, page404View, aboutPageView, LocalNewsView, \
    SportNewsView, TechnologyNewsView, ForeignNewsView, NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view, \
    SearchResultsView

urlpatterns = [
    path('', IndexPageView.as_view(), name="home_page"),
    path('news/create/', NewsCreateView.as_view(), name='create_page'),
    path('news/all/', news_list, name='all_news_list'),
    path('contact-us/', contactView, name='contact_page'),
    path('404page/', page404View, name='404_page'),
    path('about/', aboutPageView, name='about_page'),
    path('local/', LocalNewsView.as_view(), name='local_page'),
    path('sport/', SportNewsView.as_view(), name='sport_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_page'),
    path('news/<slug:news>/', newsdetailview, name='news_detail_page'),
    path('news/<slug>/edit', NewsUpdateView.as_view(), name='edit_page'),
    path('news/<slug>/delete', NewsDeleteView.as_view(), name='delete_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('search-results/', SearchResultsView.as_view(), name='search_results_page'),
]
