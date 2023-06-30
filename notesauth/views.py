from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from notes.models import Note

# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account_login')
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Note.objects.filter(author=self.request.user)
        context['notes_count'] = len(obj)
        return context
