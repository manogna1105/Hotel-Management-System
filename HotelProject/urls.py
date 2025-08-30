"""HotelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from rooms import views as room_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import login_view,guest_dashboard,logout_view
from bookings.views import booking,booking_success
from users.views import login_view, guest_dashboard, logout_view, booking_redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('rooms/', room_views.rooms, name='rooms'),
    path('about/',views.about,name='about'),
    path('rooms/<int:room_id>/', room_views.room_detail_view, name='room_detail'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('booking/',booking, name='booking'),
    path('guest/booking/success/',booking_success, name='booking_success'),
    path('login/', login_view, name='login_view'),
    path('guest/', guest_dashboard, name='guest_dashboard'),
    path('logout/', logout_view, name='logout_view'),
    path('', booking_redirect_view, name='booking_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)