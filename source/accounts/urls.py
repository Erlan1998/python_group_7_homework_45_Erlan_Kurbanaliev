from django.urls import path
from accounts.views import register_view, MyLogoutView, BookingView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('registration/', register_view, name='register'),
    path('booking/', BookingView.as_view(), name='booking'),
    # path('<int:id>/', UserDetailView.as_view(), name='all_accounts'),
    # path('profile/', UserUpdateView.as_view(), name='update_user'),
    # path('profile/change-password', UserChangePasswordView.as_view(), name='change_password'),
]