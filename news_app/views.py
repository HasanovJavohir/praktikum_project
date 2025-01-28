from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.objects.filter(status="PB")
    context = {
        "news_list": news_list,
    }

    return render(request, "news/news_list.html", context=context)


def newsdetailview(request, news):
    news = get_object_or_404(News, slug=news, status="PB")
    context = {
        "news": news,
    }

    return render(request, "news/news_detail_view.html", context=context)


# def indexView(request):
#     categories = Category.objects.all()
#     news_list = News.objects.all().order_by('-published_time')[:10]
#     # for LOCAL news
#     local_news = News.objects.all().filter(category__name="Mahalliy").order_by('-published_time')[1:7]
#     main_local_news = News.objects.filter(category__name="Mahalliy").order_by('-published_time')[0]
#
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "local_news": local_news,
#         "main_local_news": main_local_news,
#     }
#
#     return render(request, "news/index.html", context=context)


class IndexPageView(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-published_time')[:6]
        # LOCAL news
        context['local_news'] = News.objects.all().filter(category__name="Mahalliy").order_by('-published_time')[0:7]
        # TECHNOLOGY news
        context['technology_news'] = News.objects.all().filter(category__name="Texnologiya").order_by('-published_time')[0:7]
        # SPORT news
        context['sport_news'] = News.objects.all().filter(category__name="Sport").order_by('-published_time')[:7]
        # WORLD news
        context['world_news'] = News.objects.all().filter(category__name="Xorij").order_by('-published_time')[:7]

        return context


def contactView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Biz bilan bog'langaningiz uchun tashakkur!!!")
    context = {
        "form": form,
    }
    return render(request, "news/contact.html", context=context)


# class ContactPageView(TemplateView):
#     template_name = "news/contact.form"
#
#     def get(self, request, *args, **kwargs):
#         form = ContactForm()
#         context = {
#             "form": form,
#         }
#         return render(request, "news/contact.html", context=context)
#
#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#         if request.method == "POST" and form.is_valid():
#             form.save()
#             return HttpResponse("<h2>Biz bog'langaningiz uchun tashakkur!</h2>")
#         context = {
#             "form": form,
#         }
#         return render(request, "news/contact.html", context=context)


def page404View(request):
    context = {}
    return render(request, 'news/404.html', context=context)


def aboutPageView(request):
    context = {}
    return render(request, 'news/about.html', context=context)


class LocalNewsView(ListView):
    model = News
    template_name = "news/local_news.html"
    context_object_name = "local_news"

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Mahalliy")
        return news


class SportNewsView(ListView):
    model = News
    template_name = "news/sport_news.html"
    context_object_name = "sport_news"

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Sport")
        return news


class TechnologyNewsView(ListView):
    model = News
    template_name = "news/technology_news.html"
    context_object_name = "technology_news"

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Texnologiya")
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = "news/foreign_news.html"
    context_object_name = "foreign_news"

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Xorij")
        return news
