from django.contrib import admin
from crime.models import Crime,Location,Suspect,Agent,Category

class CrimeAdmin(admin.ModelAdmin):
	list_display = ['category','timedate','suspect','location','status']

class AgentAdmin(admin.ModelAdmin):
	list_display = ['firstname','lastname','location']

class SuspectAdmin(admin.ModelAdmin):
	list_display = ['firstname','lastname','location']

class LocationAdmin(admin.ModelAdmin):
	list_display = ['barangay','city','country']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Crime,CrimeAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Suspect,SuspectAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Category,CategoryAdmin)
