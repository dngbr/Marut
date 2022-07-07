from email import header
from app.models import Product
import csv


def run():
    with open('marut/PRODUSE.csv') as file:
        reader = csv.reader(file)
        next(reader)
        Product.objects.all().delete()
        for row in reader:
            print(row)
            product = Product(
                nume=row[0],
                profil=row[1],
                deschidere=row[2],
                lungime=row[3],
                inaltime=row[4],
                culoare=row[5],
                sticla=row[6],
                pret=row[7],
                imagine=row[8],
            )
            product.save()
