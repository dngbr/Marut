from app.models import Product_in_Quote


def run():
    Product_in_Quote.objects.all().delete()
