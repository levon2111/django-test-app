from django.urls import path, re_path
from rest_framework import routers

from help_gamblers.apps.users.views import LoginAPIView, SignUpAPIView, ConfirmAccountAPIView, ForgotPasswordAPIView, \
    ResetPasswordAPIView, UsersViewSet, ReleaseAnnouncementAPIView, ReleaseAnnouncementFailedAPIView, \
    ConfirmAttendanceAPIView

router = routers.DefaultRouter()
router.register("users", UsersViewSet)

app_name = 'users'
urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('sign-up/', SignUpAPIView.as_view()),
    path('confirm-account', ConfirmAccountAPIView.as_view()),
    path('forgot-password', ForgotPasswordAPIView.as_view()),
    re_path(r'reset-password/(?P<reset_key_token>[\w-]+)/$', ResetPasswordAPIView.as_view()),
    path('send-invitations-success/', ReleaseAnnouncementAPIView.as_view()),
    path('send-invitations-failed/', ReleaseAnnouncementFailedAPIView.as_view()),
    re_path(r'confirm/(?P<reset_key_token>[\w-]+)/$', ConfirmAttendanceAPIView.as_view()),
]
