from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView, PasswordResetDoneView, \
    PasswordResetConfirmView

from . import views
from .forms import LoginForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'), # app_photo:signup, тепер ідемо в views
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm, redirect_authenticated_user=True), name='signin'), # app_photo:signin, тепер ідемо в views
    path('logout/', views.logout_view, name='logout'), # app_photo:logout, тепер ідемо в views

    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path("reset-password/done/", PasswordResetDoneView.as_view(template_name="app_auth/password_reset_done.html"), name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="app_auth/password_reset_confirm.html", success_url="/app_auth/reset-password/complete/"), name="password_reset_confirm"),
    path("reset-password/complete/", PasswordResetCompleteView.as_view(template_name="app_auth/password_reset_complete.html"), name="password_reset_complete"),
]