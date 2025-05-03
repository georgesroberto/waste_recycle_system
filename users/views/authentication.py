from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView, 
    PasswordResetView, 
    PasswordResetConfirmView,
    PasswordResetDoneView
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from users.forms import CustomUserCreationForm


# ------------------- Register View -------------------
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your account has been created successfully! You can now log in."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error with your registration. Please check the form and try again."
        )
        return super().form_invalid(form)


# ------------------- Login View -------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(
            self.request,
            "Welcome back! You have successfully logged in."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Invalid username or password. Please try again."
        )
        return super().form_invalid(form)


# ------------------- Logout View -------------------
def user_logout(request):
    logout(request)
    messages.info(
        request,
        "You have been logged out successfully."
    )
    return redirect('users:login')


# ------------------- Password Reset Views -------------------
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    form_class = PasswordResetForm

    def form_valid(self, form):
        messages.success(
            self.request,
            "Password reset link has been sent to your email."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Error in resetting password. Please try again."
        )
        return super().form_invalid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = SetPasswordForm

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your password has been successfully reset. You can now log in."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Passwords do not match or do not meet security requirements."
        )
        return super().form_invalid(form)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


