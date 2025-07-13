from .cart import Cart

def cart(request):
    try:
        return {'cart': Cart(request)}
    except Exception:
        return {}  # Безопасно — ничего не вернёт, если session не доступна
