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
            link = form.save()
            link.save()
            messages.info(request, f"Link został utworzony")
            context['url'] = link.code
        else:
            messages.error(request, 'Wystąpił błąd')

    return render(request, 'shorter/index.html', context)


def link_redir(request, code):
    link = get_object_or_404(Link, code=code)
    return redirect(f'{link.url}')
