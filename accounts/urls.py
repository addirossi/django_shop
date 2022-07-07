from django.urls import path


from .views import *


urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('activation/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', UpdateTokenView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('restore_password/', RestorePasswordView.as_view()),
    path('restore_complete/', RestorePasswordCompleteView.as_view()),
    path('change_password/', ChangePasswordView.as_view())
]
