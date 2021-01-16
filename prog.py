def sumaNaturales(cantidad):
    if cantidad == 0:
        return 0
    else:
        return cantidad + sumaNaturales(cantidad-1)