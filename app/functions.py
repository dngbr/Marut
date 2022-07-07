from app.models import Product_in_Quote,Quote


def findProduct(produs, nume, profil, deschidere, lungime, inaltime, culoare, sticla):
    condition1 = (nume == produs.nume)
    condition2 = (profil == produs.profil)
    condition3 = (deschidere == produs.deschidere)
    condition4 = (lungime == produs.lungime)
    condition5 = (inaltime == produs.inaltime)
    condition6 = (culoare == produs.culoare)
    condition7 = (sticla == produs.sticla)
    if condition1 and condition2 and condition3 and condition4 and condition5 and condition6 and condition7:
        return True
    return False
