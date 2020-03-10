from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .forms import LinkForm
from shorter.models import Link


def index(request):
    form = LinkForm
    context = {
        'form': form,
        'path': request.path
    }
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = request.POST.get('url')
            if Link.objects.filter(url=url).exists():
                link = Link.objects.get(url=url)
            else:
                link = form.save()
                link.save()
            messages.info(request, f"Your URL was successfully created! 😍")
            context['url'] = request.build_absolute_uri() + link.code
            context['qr'] = link.qr.url
        else:
            messages.error(request, 'An error occured 😔')

    return render(request, 'shorter/index.html', context)


def link_redir(request, code):
    link = get_object_or_404(Link, code=code)
    return redirect(f'{link.url}')
