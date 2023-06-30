from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    AddEmailForm,
    ChangePasswordForm,
    ResetPasswordKeyForm,
    SetPasswordForm
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div
from crispy_bootstrap5.bootstrap5 import FloatingField

class NotesSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField("username"),
            FloatingField("email"),
            FloatingField("password1"),
            Submit('submit', 'Sign up', css_class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold")
        )

class NotesLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('login'),
            FloatingField('password'),
            Submit('submit', 'Log in', css_class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold"),
            Div(
                HTML('<a href="{% url "account_reset_password" %}" class="mb-4 link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"><strong>forgot password</strong></a>'),
                css_class="text-center"
            )
        )

class NotesResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('email'),
            Submit('submit', 'Send reset password link', css_class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold"),
        )

class NotesAddEmailForm(AddEmailForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('email'),
            HTML('<button name="action_add" class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold" type="submit">Add E-mail</button>')
        )

class NotesChangePasswordForm(ChangePasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('oldpassword'),
            FloatingField('password1'),
            FloatingField('password2'),
            HTML('<button type="submit" name="action" class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold">Change password</button>'),
            Div(
                HTML('<a href="{% url "account_reset_password" %}" class="mb-4 link-dark link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover"><strong>forgot password</strong></a>'),
                css_class="text-center"
            )
        )

class NotesResetPasswordKeyForm(ResetPasswordKeyForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('password1'),
            FloatingField('password2'),
            HTML('<button type="submit" name="action" class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold">Reset password</button>'),
        )

class NotesSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField('password1'),
            FloatingField('password2'),
            HTML('<button type="submit" name="action" class="w-100 btn btn-lg rounded-3 btn-dark mb-3 button-bold">Set password</button>'),
        )
