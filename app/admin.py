from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(EngagementPost)

admin.site.register(EngagementPostContent)


admin.site.register(EngagementPostProduct)

admin.site.register(Collection)

admin.site.register(EngagementPostCollection)

