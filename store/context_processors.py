from .models import Bike

def menu_links(request):
    links = Bike.objects.all()
    return{'links':links}
