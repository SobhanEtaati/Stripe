from django.urls import path
from .views import landing_page, checkout_session, success, cancel

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('checkout_session/', checkout_session, name = 'checkout_session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]
