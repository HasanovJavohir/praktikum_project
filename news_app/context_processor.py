from .models import News, Category


def latest_news(request):
    latest_news = News.objects.all().order_by('-published_time')[:10]
    categories_names = Category.objects.all()

    context = {
        "latest_news": latest_news,
        "categories_names": categories_names,
    }
    return context
