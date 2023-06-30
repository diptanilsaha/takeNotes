from django.views.generic import ListView, DetailView, DeleteView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden

from .models import Note
from .forms import NotesCreateForm

# Create your views here.
class NotesLandingView(TemplateView):
    template_name = 'notes/landing.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('notes_list'))
        return super(NotesLandingView, self).get(request, *args, **kwargs)

class NotesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Note
    paginate_by = 6
    template_name = 'notes/notes.html'
    ordering = ['-date_created']

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(author=self.request.user)

class NotesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = Note
    form_class = NotesCreateForm
    template_name = 'notes/notes_add.html'
    success_message = "<strong>%(title)s</strong> note created successfully."
    success_url = reverse_lazy('notes_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, title=self.object.title)

class NotesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['content'] = [" " if x == '' else x for x in obj.content.split('\r\n')]
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes_list')

    def form_valid(self, form, *args, **kwargs):
        obj = self.get_object()
        if obj.author == self.request.user:
            messages.add_message(self.request, messages.SUCCESS, f"<strong>{obj.title}</strong> deleted successfully.")
            return super(NotesDeleteView, self).delete(self.request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You can delete those nodes which was created by you.')
