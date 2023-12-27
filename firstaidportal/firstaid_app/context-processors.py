from.models import Category

def context(request):
    link=Category.objects.all()
    return dict(link=link)
