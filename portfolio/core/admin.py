from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(RecentWork)
admin.site.register(ServiceModel)
admin.site.register(AboutModel)
admin.site.register(Client)