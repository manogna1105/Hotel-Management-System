from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime
from .models import Booking, RoomAvailability
from rooms.models import Room
from core.models import IndividualService, ServicePackage
from payments.models import BookingInfo, BookedRoom

@login_required
def booking(request):
    available_rooms = RoomAvailability.objects.filter(available_rooms__gt=0)
    individual_services = IndividualService.objects.all()
    service_packages = ServicePackage.objects.all()

    room_data = request.GET.get("room_ids", "")
    service_ids = request.GET.get("service_ids", "")
    package_ids = request.GET.get("package_ids", "")
    total_price = request.GET.get("total_price", "0")

    room_items = []
    if room_data:
        for item in room_data.split(","):
            if ":" in item:
                room_id, qty = item.split(":")
                room = get_object_or_404(Room, id=room_id)
                availability = get_object_or_404(RoomAvailability, room=room)
                qty = int(qty)
                room_items.append({
                    "room": room,
                    "availability": availability,
                    "quantity": qty,
                    "subtotal": qty * room.price
                })

    selected_services = []
    if service_ids:
        for sid in service_ids.split(","):
            if sid.strip():
                service = get_object_or_404(IndividualService, id=sid)
                selected_services.append(service)

    selected_packages = []
    if package_ids:
        for pid in package_ids.split(","):
            if pid.strip():
                package = get_object_or_404(ServicePackage, id=pid)
                selected_packages.append(package)

    return render(request, 'booking.html', {
        "available_rooms": available_rooms,
        "individual_services": individual_services,
        "service_packages": service_packages,
        "room_items": room_items,
        "services": selected_services,
        "packages": selected_packages,
        "total_price": total_price
    })

@login_required
def booking_success(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        special_requests = request.POST.get("special_requests", "")
        payment_method = request.POST.get("payment_method")
        card_number = request.POST.get("card_number")
        card_name = request.POST.get("card_name")
        expiry = request.POST.get("expiry")
        cvv = request.POST.get("cvv")
        total_price = request.POST.get("total_price")

        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        service_ids = request.POST.get("service_ids", "")
        package_ids = request.POST.get("package_ids", "")
        room_data = request.POST.get("room_ids", "")  # e.g. "2:1,4:2"

        if not check_in or not check_out:
            return HttpResponse("Check-in or check-out date missing.", status=400)

        checkin_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        checkout_date = datetime.strptime(check_out, '%Y-%m-%d').date()

        # Parse multiple rooms
        room_list = []
        if room_data:
            for item in room_data.split(","):
                if ":" in item:
                    room_id, qty = item.split(":")
                    room = get_object_or_404(Room, id=room_id)
                    room_list.append((room, int(qty)))

        if not room_list:
            return HttpResponse("No rooms selected in the booking.", status=400)

        # Save Booking using main room (for legacy field)
        main_room = room_list[0][0]
        booking = Booking.objects.create(
            user=user,
            room=main_room,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            country=country,
            special_requests=special_requests,
            payment_method=payment_method,
            card_number=card_number,
            card_name=card_name,
            expiry=expiry,
            cvv=cvv,
        )

        # Save BookingInfo
        booking_info = BookingInfo.objects.create(
            user=user,
            email=email,
            phone=phone,
            address=address,
            check_in=checkin_date,
            check_out=checkout_date,
            room=main_room,
            total_cost=total_price,
            services=service_ids,
            packages=package_ids
        )

        # Save multiple rooms
        for room, qty in room_list:
            BookedRoom.objects.create(
                booking_info=booking_info,
                room=room,
                quantity=qty
            )
        availability = RoomAvailability.objects.get(room=room)
        if availability.available_rooms >= qty:
            availability.available_rooms -= qty
            availability.save()
        else:
            return HttpResponse(f"Not enough rooms available for {room.name}.", status=400)
        
        # Split and fetch selected services/packages
    
        service_id_list = [s for s in service_ids.split(",") if s]
        package_id_list = [p for p in package_ids.split(",") if p]
        services = IndividualService.objects.filter(id__in=service_id_list)
        packages = ServicePackage.objects.filter(id__in=package_id_list)

        return render(request, "booking_success.html", {
            "booking_info": booking_info,
            "services": services,
            "packages": packages,
            "service_id_list": service_id_list,
            "package_id_list": package_id_list
        })

    return redirect('booking')