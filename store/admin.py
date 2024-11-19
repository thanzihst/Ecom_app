from django.contrib import admin
from store.models import Tag,Product,Category,Brand,Size

from store.models import User
# Register your models here.
admin.site.register(User)

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
