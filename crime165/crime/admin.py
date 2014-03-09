from django.contrib import admin
from crime.models import Crime,Location,Suspect,Agent,Category

admin.site.register(Crime)
admin.site.register(Agent)
admin.site.register(Suspect)
admin.site.register(Location)
admin.site.register(Category)
