from .models import Bike

def menu_links(request):
    linkes = Bike.objects.all()
    return{'links':links}
