from django.contrib import admin

from .models import Categoria
from .models import Inventario
from .models import Venta
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Inventario)
admin.site.register(Venta)
