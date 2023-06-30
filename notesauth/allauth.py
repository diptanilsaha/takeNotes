from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class NotesAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('notes_list')

    def get_logout_redirect_url(self, request):
        return reverse('notes_landing')
