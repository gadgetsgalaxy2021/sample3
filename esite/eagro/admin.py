from django.contrib import admin

from eagro.models import signupUser,product,usercart

# Register your models here.

admin.site.register(signupUser)
admin.site.register(product)
admin.site.register(usercart)