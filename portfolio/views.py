from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsItem
from .forms import NewsItemForm

def landing_page(request):
    """News Feed
        Pulls all the news items and passes them to the landing page
    """
    news = NewsItem.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'portfolio/landing_page.html', {'news': news})

def article(request):
    """Article
        For now, displays the one article . . . 
    """
    return render(request, 'portfolio/blog_entries/2026-problem-of-time.html', {})

def resume(request):
    """Resume
        Simply displays my resume (temporary page?)
    """
    return render(request, 'portfolio/resume.html', {})

def news_detail(request, pk):
    """News - Single Story
        Pulls a specific news item and passes it to a "detail" page
    """
    news_item = get_object_or_404(NewsItem, pk=pk)
    return render(request, 'portfolio/news_detail.html', {'news_item': news_item})

def news_new(request):
    """News - Create a story
        If I just pressed submit, save the info to a post
        else give me a blank form to make a new news item
    """
    if request.method == "POST":
        form = NewsItemForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.author = request.user
            news_item.published_date = timezone.now()
            news_item.save()
            return redirect('news_detail', pk=news_item.pk)
    else:
        form = NewsItemForm()
    return render(request, 'portfolio/news_edit.html', {'form': form})

def news_edit(request, pk):
    """News - Edit a story
        Same as new story, but auto populates the fields with the item you want to edit
    """
    news_item = get_object_or_404(NewsItem, pk=pk)
    if request.method == "POST":
        form = NewsItemForm(request.POST, instance=news_item)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.author = request.user
            news_item.published_date = timezone.now()
            news_item.save()
            return redirect('news_detail', pk=news_item.pk)
    else:
        form = NewsItemForm(instance=news_item)
    return render(request, 'portfolio/news_edit.html', {'form': form})