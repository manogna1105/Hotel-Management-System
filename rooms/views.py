from django.shortcuts import render,get_object_or_404

from .models import Room

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms': rooms})

# Room detail page
def room_detail_view(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    return render(request, 'rooms/room_detail.html', {
        'room': room
    })

def rooms_view(request):
    rooms = Room.objects.all()

    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    guests = request.GET.get('guests')

    if guests:
        try:
            guest_int = int(guests)
            rooms = rooms.filter(guest_capacity__gte=guest_int)
        except (ValueError, TypeError):
            pass

    context = {
        'rooms': rooms,
        'checkin': checkin,
        'checkout': checkout,
        'guest_count': guests,
    }
    return render(request, 'rooms/rooms.html', context)
