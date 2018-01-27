from django.shortcuts import render, get_object_or_404  # ovo je potrebno za fbv koji su dole stavljeni pod coment
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import People


class PeopleListView(ListView):
    model = People
    template_name = 'people_list.html'
    context_object_name = 'people'

    # def get_context_data(self, *, object_list=None, **kwargs):  # ovokoristis ako zelis da dodas neto u context
    #     context = super().get_context_data(**kwargs)
    #     context['trucks'] = 'kamioni'
    #     return context


'''
sledeci code radi isto sto i prethodni class PeopleListView(ListView):

def people_list_view(request):
    queryset = People.objects.all()
    context = {
        'people': queryset,
        'trucks': 'avioni',
    }
    return render(request, 'people/people_list.html', context)
'''


class PeopleDetailView(DetailView):
    model = People
    context_object_name = 'people_detail'
    template_name = 'people/people_detail.html'

'''
sledeci code radi isto sto i prethodni class PeopleDetailView(DetailView):

def people_detail_view(request, pk=None):
    instance = get_object_or_404(People, pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'people/people_detail.html', context)
'''


class PeopleCreateView(CreateView):
    fields = '__all__'
    model = People
    success_url = reverse_lazy('people:people_list')


class PeopleUpdateView(UpdateView):
    fields = '__all__'
    model = People
    template_name = 'people/people_form.html'


class PeopleDeleteView(DeleteView):
    model = People
    success_url = reverse_lazy('people:people_list')
    template_name = 'people/people_confirm_delete.html'

