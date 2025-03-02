from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,\
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import user_login, dashboard_view, user_register, SignUpView, edit_user, UserEditView
urlpatterns = [
    # path('login/', user_login, name='login_page'),
    path('signup/', user_register, name='user_register_page'),
    # path('signup/', SignUpView.as_view(), name='user_register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change_page'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done_page'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard/', dashboard_view, name='profile_page'),
    path('profile/edit/', UserEditView.as_view(), name='profile_edit_page'),
]
