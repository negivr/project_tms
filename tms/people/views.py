from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import People


class PeopleListView(ListView):
    model = People
    template_name = 'people_list.html'
    context_object_name = 'people'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trucks'] = 'kamioni'
        return context


def people_list_view(request):
    queryset = People.objects.all()
    context = {
        'people': queryset,
        'trucks': 'avioni',
    }
    return render(request, 'people/people_list.html', context)


class PeopleDetailView(DetailView):
    model = People
    context_object_name = 'object'
    template_name = 'people/people_detail.html'


def people_detail_view(request, pk=None):
    instance = get_object_or_404(People, pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'people/people_detail.html', context)

