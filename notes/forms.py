from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_bootstrap5.bootstrap5 import FloatingField

from .models import Note


class NotesCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'content']

    def __init__(self, *args, **kwargs):
        super(NotesCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('title'),
            FloatingField('description'),
            Field('content', css_class="form-control rounded border-dark-subtle bg-body-tertiary mb-3", id="noteBox", placeholder="Write/paste your content"),
            Submit('submit', 'Save note', css_class='btn btn-success')
        )
