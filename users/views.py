from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from payments.models import BookingInfo
from .models import CustomUser


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect('guest_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = authenticate(request, username=username, password=password)

        if user is None:
            try:
                user = CustomUser.objects.create(
                    username=username,
                    password=make_password(password),
                    role=role
                )
            except Exception:
                return render(request, 'login.html', {'error': 'User creation failed. Check inputs.'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            elif user.role == 'guest':
                return redirect('guest_dashboard')
            else:
                return render(request, 'login.html', {'error': 'Unknown role'})
        else:
            return render(request, 'login.html', {'error': 'Login failed'})

    return render(request, 'login.html')


from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login_view')



from core.models import BookingIndividualService, BookingService
from bookings.models import Booking
from payments.models import BookingInfo

@login_required
def guest_dashboard(request):
    user = request.user
    latest_booking_info = BookingInfo.objects.filter(user=user).order_by('-id').first()

    if latest_booking_info:
        # Try to get latest Booking by user only (no total_cost filter)
        matching_booking = Booking.objects.filter(user=user).order_by('-id').first()

        if matching_booking:
            individual_services = BookingIndividualService.objects.filter(booking=matching_booking)
            package_services = BookingService.objects.filter(booking=matching_booking)

            latest_booking_info.service_list = [s.service.name for s in individual_services]
            latest_booking_info.package_list = [p.package.name for p in package_services]
        else:
            latest_booking_info.service_list = []
            latest_booking_info.package_list = []
    else:
        latest_booking_info = None

    return render(request, 'guest_dashboard.html', {
        'latest_booking': latest_booking_info,
        'user': user,
    })

def booking_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('guest_dashboard')
    else:
        return redirect('login_view')
