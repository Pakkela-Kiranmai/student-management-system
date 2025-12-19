from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('view-students/', views.view_students, name='view_students'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('about/', views.about, name='about'),

    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='students/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='students/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='students/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='students/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
    template_name='students/change_password.html',
    success_url='/dashboard/'
), name='password_change'),
    path('attendance/', views.attendance, name='attendance'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('view-marks/', views.view_marks, name='view_marks'),


]
