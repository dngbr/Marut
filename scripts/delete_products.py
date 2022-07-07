from app.models import Product


def run():
    Product.objects.all().delete()
