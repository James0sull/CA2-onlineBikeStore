from .models import Brand

def menu_links(request):
    links = Brand.objects.all()
    return {'links':links}