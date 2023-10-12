from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import DjangoObtainToken, sign_up


urlpatterns = [
    path(r'token/', DjangoObtainToken.as_view(), name='sign_in'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'signup/', sign_up, name='sign_up'),

]
