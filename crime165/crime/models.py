import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Location(models.Model):
    def __unicode__(self):  
    	return self.country
    barangay = models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Agent(models.Model):
    def __unicode__(self):  
        return self.lastname
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    
class Suspect(models.Model):
    def __unicode__(self): 
    	return self.lastname
    firstname = models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    location = models.ForeignKey(Location)

class Category(models.Model):
    def __unicode__(self):  
    	return self.name
    name = models.CharField(max_length=200)
    

class Crime(models.Model):
    def __unicode__(self):  
    	return unicode(self.timedate)
            
    category = models.ForeignKey(Category)
    timedate = models.DateTimeField('Date and Time')
    location = models.ForeignKey(Location)
    suspect = models.ForeignKey(Suspect) #can be null if not yet solved, fix
    agent = models.ForeignKey(Agent) #can be many
    
    def was_published_recently(self):
    	return self.timedate >= timezone.now() - datetime.timedelta(days=1)
    #was_published_recently.admin_order_field = 'timedate'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'

class CrimeForm(ModelForm):
    class Meta:
        model = Crime

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class LocationForm(ModelForm):
    class Meta:
        model = Location

class AgentForm(ModelForm):
    class Meta:
        model = Agent

class SuspectForm(ModelForm):
    class Meta:
        model = Suspect
